from parser.python.CommandLexer import CommandLexer
from parser.python.CommandListener import CommandListener
from parser.python.CommandParser import CommandParser
from antlr4 import *
import sys


class CustomCommandListener(CommandListener):
    def enterCommand(self, ctx: CommandParser.CommandContext):
        print("enterCommand")

    def exitCommand(self, ctx: CommandParser.CommandContext):
        print("exitCommand")

    def enterCall(self, ctx: CommandParser.CallContext):
        print("enterCall")

    def exitCall(self, ctx: CommandParser.CallContext):
        print("exitCall")

    def enterAtom(self, ctx: CommandParser.AtomContext):
        print("enterAtom")

    def exitAtom(self, ctx: CommandParser.AtomContext):
        print("exitAtom")

    def enterArgument(self, ctx: CommandParser.ArgumentContext):
        print("enterArgument")

    def exitArgument(self, ctx: CommandParser.ArgumentContext):
        print("exitArgument")

    def enterRedirection(self, ctx: CommandParser.RedirectionContext):
        print("enterRedirection")

    def exitRedirection(self, ctx: CommandParser.RedirectionContext):
        print("exitRedirection")

    def enterQuoted(self, ctx: CommandParser.QuotedContext):
        print("enterQuoted")

    # Exit a parse tree produced by CommandParser#quoted.
    def exitQuoted(self, ctx: CommandParser.QuotedContext):
        print("exitQuoted")


lexer = CommandLexer(InputStream("echo `hello' world` > input.txt"))
stream = CommonTokenStream(lexer)
parser = CommandParser(stream)
tree = parser.command()
printer = CustomCommandListener()
walker = ParseTreeWalker()
walker.walk(printer, tree)
