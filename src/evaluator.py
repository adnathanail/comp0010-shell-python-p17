from typing import List
from parser.python.CommandLexer import CommandLexer
from parser.python.CommandParser import CommandParser
from parser.python.CommandVisitor import CommandVisitor
from antlr4 import *
from commands import Command, Pipe, Seq, Call
import re
from collections import deque


class Evaluator(CommandVisitor):

    # Visit a parse tree produced by CommandParser#command.
    def visitCommand(self, ctx: CommandParser.CommandContext) -> Seq:
        # get contexts
        callCtx = ctx.call()
        pipeCtx = ctx.callPipe()
        seqCtx = ctx.commandSeq()
        # converting to proper commands
        command = None
        if callCtx:
            command = self.visitCall(callCtx)
        if pipeCtx:
            command = self.visitCallPipe(pipeCtx, command)
        # treat single call or pipeline as 1-length cmd sequence
        command = Seq(command)
        if seqCtx:
            self.visitCommandSeq(seqCtx, command)
        return command

    # Visit a parse tree produced by CommandParser#commandSeq.
    def visitCommandSeq(self, ctx: CommandParser.CommandSeqContext, commandSeq: Seq):
        # get contexts
        callCtx = ctx.call()
        pipeCtx = ctx.callPipe()
        seqCtx = ctx.commandSeq()
        # add subcmd to commandSeq
        subcmd = None
        if callCtx:
            subcmd = self.visitCall(callCtx)
        if pipeCtx:
            subcmd = self.visitCallPipe(pipeCtx, subcmd)
        if subcmd is not None:
            commandSeq.addCommand(subcmd)
        # continue traversing seq if there are cmds
        if seqCtx:
            self.visitCommandSeq(seqCtx, commandSeq)

    # Visit a parse tree produced by CommandParser#callPipe.
    def visitCallPipe(self, ctx: CommandParser.CallPipeContext, call: Command) -> Pipe:
        pipe = Pipe(call, self.visitCall(ctx.call()))
        if ctx.callPipe():
            return self.visitCallPipe(ctx.callPipe(), pipe)
        else:
            return pipe

    # Visit a parse tree produced by CommandParser#call.
    def visitCall(self, ctx: CommandParser.CallContext) -> Call:
        app_name = ctx.argument().getText()
        redirectionCtx = ctx.redirection()
        atomCtx = ctx.atom()
        # Redirections and arguments
        args, redirectionIn, redirectionOut = [], [], []
        self.visitRedirection(redirectionCtx, redirectionIn, redirectionOut)
        self.visitAtom(atomCtx, args, redirectionIn, redirectionOut)
        return Call(app_name, args, redirectionIn, redirectionOut)

    # Visit a parse tree produced by CommandParser#atom.
    def visitAtom(
        self, ctx: CommandParser.AtomContext, args: List, input: List, output: List
    ):
        for el in ctx:
            if el.redirection():
                inputNew, outputNew = [], []
                self.visitRedirection(el.redirection(), inputNew, outputNew)
                input.extend(inputNew)
                output.extend(outputNew)
            else:
                # amend args list in visitArgument
                self.visitArgument(el.argument(), args)

    # Visit a parse tree produced by CommandParser#argument.
    def visitArgument(self, ctx: CommandParser.ArgumentContext, args: List):
        # to be used ONLY with arguments outside redirections
        arguments = ""
        for el in ctx.getChildren():
            if isinstance(el, CommandParser.QuotedContext):
                arguments += self.visitQuoted(el)
            else:  # unquoted content
                arguments += el.getText()
        arguments = arguments.split()  # split on whitespace
        args.extend(arguments)

    # Visit a parse tree produced by CommandParser#redirection.
    def visitRedirection(
        self, ctx: CommandParser.RedirectionContext, input: List, output: List
    ):
        # TODO: figure out how to implement redirections
        for redirection in ctx:
            sign = redirection.getChild(0).getText()
            # DO NOT CHANGE THE LINE BELOW!
            redText = redirection.argument().getText()
            if sign == "<":
                input.append(redText)
            else:
                output.append(redText)

    # Visit a parse tree produced by CommandParser#quoted.
    def visitQuoted(self, ctx: CommandParser.QuotedContext) -> str:

        # method to be used ONLY with quoted arguments outside redirections
        def evaluateSubCmd(s: str) -> str:
            lexer = CommandLexer(InputStream(s))
            stream = CommonTokenStream(lexer)
            parser = CommandParser(stream)
            tree = parser.command()
            subcmd = tree.accept(Evaluator())  # I will invoke new instance
            out = deque()
            subcmd.eval(output=out)
            return " ".join(out)

        if ctx.SINGLE_QUOTED():  # treat as one argument
            return str(ctx.SINGLE_QUOTED())[1:-1]

        if ctx.BACKQUOTED():
            backquotedCmd = str(ctx.BACKQUOTED())[1:-1]
            new_args = evaluateSubCmd(backquotedCmd)
            return new_args

        if ctx.DOUBLE_QUOTED():
            # do cmd subs. if needed, then treat as single arg
            doublequoted = str(ctx.DOUBLE_QUOTED())[1:-1]
            # search for backquoted parts
            matches = re.findall("`[^`]*`", doublequoted)
            if len(matches) > 0:  # do cmd subs.
                for match in matches:
                    matchCmd = match[1:-1]
                    new_args = evaluateSubCmd(matchCmd)
                    # replace 1st occurence of match with its evaluation
                    doublequoted = doublequoted.replace(match, new_args, 1)
            # after substituting potential subcmds, treat as single arg
            return doublequoted
