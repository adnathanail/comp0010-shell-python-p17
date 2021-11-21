from parser.python.CommandParser import CommandParser
from parser.python.CommandVisitor import CommandVisitor
from commands import Pipe, Seq, Call


class Evaluator(CommandVisitor):
    def __init__(self):  # TODO: Is this method needed?
        super().__init__()

    # Visit a parse tree produced by CommandParser#command.
    def visitCommand(self, ctx):
        # Don't do anything with Command
        print(f"Command: {ctx.getText()}")

        # get contexts
        callCtx = ctx.call()
        pipeCtx = ctx.callPipe()
        seqCtx = ctx.commandSeq()

        # check for call
        if callCtx:
            call = self.visitCall(callCtx)
            s = call

        # check for pipe
        if pipeCtx:
            pipe = self.visitCallPipe(pipeCtx, call)
            s = pipe

        # check for sequence
        if seqCtx:
            seq = None
            if pipeCtx:
                seq = Seq([pipe])
            else:
                seq = Seq([call])
            s = self.visitCommandSeq(seqCtx, seq)

        print(s)
        return s
        # TODO: change to s.eval() for evaluation

    def visitCommandInSeq(self, ctx):
        print(f"CommandInSeq: {ctx.getText()}")
        # get contexts
        callCtx = ctx.call()
        pipeCtx = ctx.callPipe()
        s = None
        # check for call
        if callCtx:
            call = self.visitCall(callCtx)
            s = call

        # check for pipe
        if pipeCtx:
            pipe = self.visitCallPipe(pipeCtx, call)
            s = pipe

        return s

    # Visit a parse tree produced by CommandParser#commandSeq.
    def visitCommandSeq(self, ctx, seqObject):  # FIXME:
        print(f"CommandSeq: {ctx.getText()}")
        # add command to commandSequence
        temp = self.visitCommandInSeq(ctx)
        print(f"TEMP: {temp}")
        seqObject.addCommand(temp)
        seqCtx = ctx.commandSeq()
        if seqCtx:
            return self.visitCommandSeq(seqCtx, seqObject)
        else:
            return seqObject

    # Visit a parse tree produced by CommandParser#callPipe.
    def visitCallPipe(self, ctx, call):
        print(f"CallPipe: {ctx.getText()}")
        p_temp = Pipe(call, self.visitCall(ctx.call()))
        if ctx.callPipe():
            return self.visitCallPipe(ctx.callPipe(), p_temp)
        else:
            return p_temp

    # Visit a parse tree produced by CommandParser#call.
    def visitCall(self, ctx):  # TODO: handle exceptions
        print(f"Call: {ctx.getText()}")
        redirectionCtx = ctx.redirection()
        argumentCtx = ctx.argument()  # this is application to be called
        atomCtx = ctx.atom()
        if redirectionCtx:
            for el in atomCtx:
                print(f"Redirection: {el.getText()}")
        if argumentCtx:
            print(f"Argument: {argumentCtx.getText()}")
        if atomCtx:
            for el in atomCtx:
                print(f"Atom: {el.getText()}")
        return Call(argumentCtx.getText())

    # Visit a parse tree produced by CommandParser#atom.
    def visitAtom(self, ctx):  # TODO
        try:
            print(f"Atom: {ctx.getText()}")
        except Exception as e:
            print(e)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CommandParser#argument.
    def visitArgument(self, ctx):  # TODO
        # app = self.app_factory.create(ctx.getText())
        # return app
        try:
            print(f"Argument: {ctx.getText()}")
        except Exception as e:
            print(e)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CommandParser#redirection.
    def visitRedirection(self, ctx):  # TODO
        try:
            print(f"Redirection: {ctx.getText()}")
        except Exception as e:
            print(e)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CommandParser#quoted.
    def visitQuoted(self, ctx):  # TODO
        try:
            print(f"Quoted: {ctx.getText()}")
        except Exception as e:
            print(e)
        return self.visitChildren(ctx)
