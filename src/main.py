from parser.python.CommandLexer import CommandLexer
from parser.python.CommandListener import CommandListener
from parser.python.CommandParser import CommandParser
from antlr4 import *
import sys


class CustomCommandListener(CommandListener):
    indent = 0

    def enterCommand(self, ctx: CommandParser.CommandContext):
        self.indent += 1
        print(" " * self.indent, "enterCommand")

    def exitCommand(self, ctx: CommandParser.CommandContext):
        self.indent -= 1
        print(" " * self.indent, "exitCommand")

    def enterCommandSeq(self, ctx: CommandParser.CommandSeqContext):
        self.indent += 1
        print(" " * self.indent, "enterCommandSeq")

    def exitCommandSeq(self, ctx: CommandParser.CommandSeqContext):
        self.indent -= 1
        print(" " * self.indent, "exitCommandSeq")

    def enterCallPipe(self, ctx: CommandParser.CallPipeContext):
        self.indent += 1
        print(" " * self.indent, "enterCallPipe")

    def exitCallPipe(self, ctx: CommandParser.CallPipeContext):
        self.indent -= 1
        print(" " * self.indent, "exitCallPipe")

    def enterCall(self, ctx: CommandParser.CallContext):
        self.indent += 1
        print(" " * self.indent, "enterCall")

    def exitCall(self, ctx: CommandParser.CallContext):
        self.indent -= 1
        print(" " * self.indent, "exitCall")

    def enterAtom(self, ctx: CommandParser.AtomContext):
        self.indent += 1
        print(" " * self.indent, "enterAtom")

    def exitAtom(self, ctx: CommandParser.AtomContext):
        self.indent -= 1
        print(" " * self.indent, "exitAtom")

    def enterArgument(self, ctx: CommandParser.ArgumentContext):
        self.indent += 1
        print(" " * self.indent, "enterArgument")

    def exitArgument(self, ctx: CommandParser.ArgumentContext):
        self.indent -= 1
        print(" " * self.indent, "exitArgument")

    def enterRedirection(self, ctx: CommandParser.RedirectionContext):
        self.indent += 1
        print(" " * self.indent, "enterRedirection")

    def exitRedirection(self, ctx: CommandParser.RedirectionContext):
        self.indent -= 1
        print(" " * self.indent, "exitRedirection")

    def enterQuoted(self, ctx: CommandParser.QuotedContext):
        self.indent += 1
        print(" " * self.indent, "enterQuoted")

    def exitQuoted(self, ctx: CommandParser.QuotedContext):
        self.indent -= 1
        print(" " * self.indent, "exitQuoted")


lexer = CommandLexer(InputStream("echo `hello' world` | grep; tes.txt < hi"))
print("Lexed")
stream = CommonTokenStream(lexer)
parser = CommandParser(stream)
print("Parsed")
tree = parser.command()
printer = CustomCommandListener()
walker = ParseTreeWalker()
walker.walk(printer, tree)
