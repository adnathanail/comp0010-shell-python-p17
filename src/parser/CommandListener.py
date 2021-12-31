# Generated from Command.g4 by ANTLR 4.9.2
from antlr4 import *

if __name__ is not None and "." in __name__:
    from .CommandParser import CommandParser
else:
    from CommandParser import CommandParser


# This class defines a complete listener for a parse tree produced by CommandParser.
class CommandListener(ParseTreeListener):

    # Enter a parse tree produced by CommandParser#command.
    def enterCommand(self, ctx: CommandParser.CommandContext):
        pass

    # Exit a parse tree produced by CommandParser#command.
    def exitCommand(self, ctx: CommandParser.CommandContext):
        pass

    # Enter a parse tree produced by CommandParser#commandSeq.
    def enterCommandSeq(self, ctx: CommandParser.CommandSeqContext):
        pass

    # Exit a parse tree produced by CommandParser#commandSeq.
    def exitCommandSeq(self, ctx: CommandParser.CommandSeqContext):
        pass

    # Enter a parse tree produced by CommandParser#callPipe.
    def enterCallPipe(self, ctx: CommandParser.CallPipeContext):
        pass

    # Exit a parse tree produced by CommandParser#callPipe.
    def exitCallPipe(self, ctx: CommandParser.CallPipeContext):
        pass

    # Enter a parse tree produced by CommandParser#call.
    def enterCall(self, ctx: CommandParser.CallContext):
        pass

    # Exit a parse tree produced by CommandParser#call.
    def exitCall(self, ctx: CommandParser.CallContext):
        pass

    # Enter a parse tree produced by CommandParser#atom.
    def enterAtom(self, ctx: CommandParser.AtomContext):
        pass

    # Exit a parse tree produced by CommandParser#atom.
    def exitAtom(self, ctx: CommandParser.AtomContext):
        pass

    # Enter a parse tree produced by CommandParser#argument.
    def enterArgument(self, ctx: CommandParser.ArgumentContext):
        pass

    # Exit a parse tree produced by CommandParser#argument.
    def exitArgument(self, ctx: CommandParser.ArgumentContext):
        pass

    # Enter a parse tree produced by CommandParser#redirection.
    def enterRedirection(self, ctx: CommandParser.RedirectionContext):
        pass

    # Exit a parse tree produced by CommandParser#redirection.
    def exitRedirection(self, ctx: CommandParser.RedirectionContext):
        pass

    # Enter a parse tree produced by CommandParser#quoted.
    def enterQuoted(self, ctx: CommandParser.QuotedContext):
        pass

    # Exit a parse tree produced by CommandParser#quoted.
    def exitQuoted(self, ctx: CommandParser.QuotedContext):
        pass


del CommandParser
