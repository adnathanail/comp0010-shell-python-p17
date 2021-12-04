from typing import List
from parser.python.CommandParser import CommandParser
from parser.python.CommandVisitor import CommandVisitor
from commands import Command, Pipe, Seq, Call
import logging
from collections import deque


class Evaluator(CommandVisitor):
    def __init__(self):  # TODO: Is this method needed?
        super().__init__()

    # Visit a parse tree produced by CommandParser#command.
    def visitCommand(self, ctx) -> Command:
        logging.debug(f"Command: {ctx.getText()}")
        callCtx = ctx.call()
        pipeCtx = ctx.callPipe()
        seqCtx = ctx.commandSeq()
        # Converting to proper commands
        command = Command()
        if callCtx:
            command = self.visitCall(callCtx)
        if pipeCtx:
            command = self.visitCallPipe(pipeCtx, command)
        if seqCtx:
            command = Seq(command)
            self.visitCommandSeq(seqCtx, command)
        return command

    # Visit a parse tree produced by CommandParser#commandSeq.
    def visitCommandSeq(self, ctx, commandSeq: Seq) -> None:
        logging.debug(f"CommandSeq: {ctx.getText()}")
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
        logging.debug(f"CallPipe: {ctx.getText()}")
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
                args.append(self.visitArgument(el.argument()))

    # Visit a parse tree produced by CommandParser#argument.
    def visitArgument(self, ctx):
        return ctx.getText()

    # Visit a parse tree produced by CommandParser#redirection.
    def visitRedirection(self, ctx, input, output):
        for redirection in ctx:
            redText = self.visitArgument(redirection.argument())
            if redText.startswith("<"):
                input.append(redText)
            else:
                output.append(redText)

    # Visit a parse tree produced by CommandParser#quoted.
    def visitQuoted(self, ctx):  # TODO
        # TODO: check if backquoted and perform cmd substitution
        print(f"Quoted: {ctx.getText()}")
        return self.visitChildren(ctx)
