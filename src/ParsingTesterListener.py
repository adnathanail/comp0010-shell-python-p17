from parser.python.CommandListener import CommandListener
from parser.python.CommandParser import CommandParser

"""
This file is only used for testing lexing and parsing
TODO: discard it before submission
"""


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
        print(" " * self.indent, "enterArgument")
        self.indent += 1
        if ctx.quoted():
            for el in ctx.quoted():
                try:
                    print(f"QUOTED: {el.getText()}")
                    print(f"TOKENS: {el.getChild(0)}")
                    print(f"SINGLE: {el.SINGLE_QUOTED()}")
                    print(f"DOUBLE: {el.DOUBLE_QUOTED()}")
                    print(f"BACK: {el.BACKQUOTED()}")
                except Exception as e:
                    pass

        if len(ctx.UNQUOTED_CONTENT()) > 0:
            print(f"UNQUOTED:{ctx.UNQUOTED_CONTENT()[0].getText()}")

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
