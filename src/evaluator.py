from typing import List
from parser.python.CommandLexer import CommandLexer
from parser.python.CommandParser import CommandParser
from parser.python.CommandVisitor import CommandVisitor
from antlr4 import *
from commands import Command, Pipe, Seq, Call
import re


class Evaluator(CommandVisitor):
    def __init__(self):  # TODO: Is this method needed?
        super().__init__()

    # Visit a parse tree produced by CommandParser#command.
    def visitCommand(self, ctx) -> Command:
        callCtx = ctx.call()
        pipeCtx = ctx.callPipe()
        seqCtx = ctx.commandSeq()
        # Converting to proper commands
        command = Command()
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
    def visitCommandSeq(self, ctx, commandSeq: Seq) -> None:
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
    def visitCallPipe(self, ctx, call: Command) -> Pipe:
        pipe = Pipe(call, self.visitCall(ctx.call()))
        if ctx.callPipe():
            return self.visitCallPipe(ctx.callPipe(), pipe)
        else:
            return pipe

    # Visit a parse tree produced by CommandParser#call.
    def visitCall(self, ctx) -> Call:
        app_name = ctx.argument().getText()
        redirectionCtx = ctx.redirection()
        atomCtx = ctx.atom()
        # Redirections and arguments
        args, input, output = [], [], []
        self.visitRedirection(redirectionCtx, input, output)
        self.visitAtom(atomCtx, args, input, output)
        return Call(app_name, args, input, output)

    # Visit a parse tree produced by CommandParser#atom.
    def visitAtom(self, ctx, args: List, input: List, output: List):
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
    def visitArgument(self, ctx, args: List) -> None:
        # to be used ONLY with arguments outside redirections
        quotedCtx = ctx.quoted()
        if quotedCtx:
            self.visitQuoted(quotedCtx, args)
        else:  # UNQUOTED_CONTENT()
            args.append(ctx.getText())

    # Visit a parse tree produced by CommandParser#redirection.
    def visitRedirection(self, ctx, input, output) -> None:
        for redirection in ctx:
            sign = redirection.getChild(0).getText()
            # DO NOT CHANGE THE LINE BELOW!
            redText = redirection.argument().getText()
            if sign == "<":
                input.append(redText)
            else:
                output.append(redText)

    # Visit a parse tree produced by CommandParser#quoted.
    def visitQuoted(self, ctx, args) -> None:

        # method to be used ONLY with quoted arguments outside redirections
        def evaluateSubCmd(s: str):
            lexer = CommandLexer(InputStream(s))
            stream = CommonTokenStream(lexer)
            parser = CommandParser(stream)
            tree = parser.command()
            subcmd = tree.accept(Evaluator())  # I will invoke new instance
            return subcmd.eval()

        # add to args, use cmd substitution where needed
        for el in ctx:
            if el.SINGLE_QUOTED():  # treat as one argument
                args.append(str(el.SINGLE_QUOTED())[1:-1])

            if el.BACKQUOTED():
                backquotedCmd = str(el.BACKQUOTED())[1:-1]
                new_args = evaluateSubCmd(backquotedCmd)
                if new_args is not None:
                    new_args = new_args.split()
                    args.extend(new_args)

            if el.DOUBLE_QUOTED():
                # do cmd subs. if needed, then treat as single arg
                doublequoted = str(el.DOUBLE_QUOTED())[1:-1]
                # search for backquoted parts
                matches = re.findall("`[^`]*`", doublequoted)
                if len(matches) > 0:  # do cmd subs.
                    for match in matches:
                        matchCmd = match[1:-1]
                        new_args = evaluateSubCmd(matchCmd).split()
                        new_args = " ".join(new_args)
                        # replace 1st occurence of match with its evaluation
                        doublequoted = doublequoted.replace(match, new_args, 1)
                # after substituting potential subcmds, treat as single arg
                args.append(doublequoted)
