# Generated from Command.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CommandParser import CommandParser
else:
    from CommandParser import CommandParser

# This class defines a complete listener for a parse tree produced by CommandParser.
class CommandListener(ParseTreeListener):

    # Enter a parse tree produced by CommandParser#command.
    def enterCommand(self, ctx:CommandParser.CommandContext):
        pass

    # Exit a parse tree produced by CommandParser#command.
    def exitCommand(self, ctx:CommandParser.CommandContext):
        pass


    # Enter a parse tree produced by CommandParser#call.
    def enterCall(self, ctx:CommandParser.CallContext):
        pass

    # Exit a parse tree produced by CommandParser#call.
    def exitCall(self, ctx:CommandParser.CallContext):
        pass


    # Enter a parse tree produced by CommandParser#argument.
    def enterArgument(self, ctx:CommandParser.ArgumentContext):
        pass

    # Exit a parse tree produced by CommandParser#argument.
    def exitArgument(self, ctx:CommandParser.ArgumentContext):
        pass



del CommandParser