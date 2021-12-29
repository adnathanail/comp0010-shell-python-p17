import re
from collections import deque
from typing import List
from glob import glob
from antlr4 import InputStream, CommonTokenStream

from commands import Command, Pipe, Seq, Call
from parser.CommandLexer import CommandLexer
from parser.CommandParser import CommandParser
from parser.CommandVisitor import CommandVisitor


class Converter(CommandVisitor):

    # Visit a parse tree produced by CommandParser#command.
    def visitCommand(self, ctx: CommandParser.CommandContext) -> Command:
        # get contexts
        callCtx = ctx.call()
        pipeCtx = ctx.callPipe()
        seqCtx = ctx.commandSeq()
        # converting to proper commands
        command = self.visitCall(callCtx)
        if pipeCtx:
            command = self.visitCallPipe(pipeCtx, command)
        if seqCtx:
            # init with first call or callPipe
            command = Seq(command)
            # add other existing commands to Seq command
            self.visitCommandSeq(seqCtx, command)
        return command

    # Visit a parse tree produced by CommandParser#commandSeq.
    def visitCommandSeq(
        self,
        ctx: CommandParser.CommandSeqContext,
        commandSeq: Seq
    ):
        # get contexts
        callCtx = ctx.call()
        pipeCtx = ctx.callPipe()
        seqCtx = ctx.commandSeq()
        # add subcmd to commandSeq
        subcmd = self.visitCall(callCtx)
        if pipeCtx:
            subcmd = self.visitCallPipe(pipeCtx, subcmd)
        commandSeq.add_command(subcmd)
        # continue traversing seq if there are cmds
        if seqCtx:
            self.visitCommandSeq(seqCtx, commandSeq)

    # Visit a parse tree produced by CommandParser#callPipe.
    def visitCallPipe(
        self,
        ctx: CommandParser.CallPipeContext,
        call: Command
    ) -> Pipe:
        pipe = Pipe(call, self.visitCall(ctx.call()))
        if ctx.callPipe():
            return self.visitCallPipe(ctx.callPipe(), pipe)
        else:
            return pipe

    # Visit a parse tree produced by CommandParser#call.
    def visitCall(self, ctx: CommandParser.CallContext) -> Call:
        args = []
        # check for first arg, cmd subs. sensitive
        self.visitArgument(ctx.argument(), args)
        app_name = args.pop(0)  # rest args are saved
        # get contexts
        redirectionCtx = ctx.redirection()
        atomCtx = ctx.atom()
        # Redirections and arguments from atom
        redirect_from, redirect_to = [], []
        for redirection in redirectionCtx:
            self.visitRedirection(redirection, redirect_from, redirect_to)
        self.visitAtom(atomCtx, args, redirect_from, redirect_to)
        return Call(app_name, args, redirect_from, redirect_to)

    # Visit a parse tree produced by CommandParser#atom.
    def visitAtom(
        self,
        ctx: CommandParser.AtomContext,
        args: List,
        input: List,
        output: List
    ):
        for el in ctx:
            if el.redirection() is not None:
                input_new, output_new = [], []
                self.visitRedirection(el.redirection(), input_new, output_new)
                input.extend(input_new)
                output.extend(output_new)
            else:
                # amend args list in visitArgument
                self.visitArgument(el.argument(), args)

    # Visit a parse tree produced by CommandParser#argument.
    def visitArgument(self, ctx: CommandParser.ArgumentContext, args: List):
        # to be used ONLY with arguments outside redirections
        do_globbing = False
        arguments = ""
        for el in ctx.getChildren():
            if isinstance(el, CommandParser.QuotedContext):
                arguments += self.visitQuoted(el)
            else:  # unquoted content
                s = el.getText()
                if "*" in s:
                    do_globbing = True
                arguments += s
        if do_globbing:
            arguments = glob(arguments)  # gives a list
        else:
            arguments = arguments.split(" ")
        args.extend(arguments)

    # Visit a parse tree produced by CommandParser#redirection.
    def visitRedirection(
        self, ctx: CommandParser.RedirectionContext, input: List, output: List
    ):
        sign = ctx.getChild(0).getText()
        filename = ctx.argument().getText()
        if sign == "<":
            input.append(filename)
        else:
            output.append(filename)

    # Visit a parse tree produced by CommandParser#quoted.
    def visitQuoted(self, ctx: CommandParser.QuotedContext) -> str:

        # method to be used ONLY with quoted arguments outside redirections
        def evaluateSubCmd(s: str) -> str:
            lexer = CommandLexer(InputStream(s))
            stream = CommonTokenStream(lexer)
            parser = CommandParser(stream)
            tree = parser.command()
            subcmd = tree.accept(Converter())  # I will invoke new instance
            out = deque()
            subcmd.eval(output=out)
            return "".join(out).strip()

        if ctx.SINGLE_QUOTED():  # treat as one argument
            return str(ctx.SINGLE_QUOTED())[1:-1]

        elif ctx.BACKQUOTED():
            backquoted_cmd = str(ctx.BACKQUOTED())[1:-1]
            new_args = evaluateSubCmd(backquoted_cmd)
            new_args = new_args.replace("\n", " ")
            new_args = new_args.strip()
            return new_args

        else:  # ctx.DOUBLE_QUOTED():
            # do cmd subs. if needed, then treat as single arg
            doublequoted = str(ctx.DOUBLE_QUOTED())[1:-1]
            # search for backquoted parts
            matches = re.findall("`[^`]*`", doublequoted)
            if len(matches) > 0:  # do cmd subs.
                for match in matches:
                    match_cmd = match[1:-1]
                    new_args = evaluateSubCmd(match_cmd)
                    # replace 1st occurence of match with its evaluation
                    doublequoted = doublequoted.replace(match, new_args, 1)
            # after substituting potential subcmds, treat as single arg
            return doublequoted
