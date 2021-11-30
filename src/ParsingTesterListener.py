from parser.python.CommandListener import CommandListener
from parser.python.CommandParser import CommandParser

"""
This file is only used for testing lexing and parsing
TODO: discard it before submission
"""


class CustomCommandListener(CommandListener):
    indent = 0

    def enterCommand(self, ctx: CommandParser.CommandContext):
        print(" " * self.indent, "enterCommand")
        self.indent += 1

    def exitCommand(self, ctx: CommandParser.CommandContext):
        self.indent -= 1
        print(" " * self.indent, "exitCommand")

    def enterCommandSeq(self, ctx: CommandParser.CommandSeqContext):
        print(" " * self.indent, "enterCommandSeq")
        self.indent += 1

    def exitCommandSeq(self, ctx: CommandParser.CommandSeqContext):
        self.indent -= 1
        print(" " * self.indent, "exitCommandSeq")

    def enterCallPipe(self, ctx: CommandParser.CallPipeContext):
        print(" " * self.indent, "enterCallPipe")
        self.indent += 1

    def exitCallPipe(self, ctx: CommandParser.CallPipeContext):
        self.indent -= 1
        print(" " * self.indent, "exitCallPipe")

    def enterCall(self, ctx: CommandParser.CallContext):
        print(" " * self.indent, "enterCall")
        self.indent += 1

    def exitCall(self, ctx: CommandParser.CallContext):
        self.indent -= 1
        print(" " * self.indent, "exitCall")

    def enterAtom(self, ctx: CommandParser.AtomContext):
        print(" " * self.indent, "enterAtom")
        self.indent += 1

    def exitAtom(self, ctx: CommandParser.AtomContext):
        self.indent -= 1
        print(" " * self.indent, "exitAtom")

    def enterArgument(self, ctx: CommandParser.ArgumentContext):
        print(" " * self.indent, "enterArgument")
        if ctx.quoted():
            for el in ctx.quoted():
                try:
                    print(" " * (self.indent + 1), f"QUOTED: {el.getText()}")
                    print(" " * (self.indent + 1), f"TOKENS: {el.getChild(0)}")
                    print(" " * (self.indent + 1), f"SINGLE: {el.SINGLE_QUOTED()}")
                    print(" " * (self.indent + 1), f"DOUBLE: {el.DOUBLE_QUOTED()}")
                    print(" " * (self.indent + 1), f"BACK: {el.BACKQUOTED()}")
                except Exception as e:
                    pass

        if len(ctx.UNQUOTED_CONTENT()) > 0:
            print(
                " " * (self.indent + 1),
                f"UNQUOTED:{ctx.UNQUOTED_CONTENT()[0].getText()}",
            )
        self.indent += 1

    def exitArgument(self, ctx: CommandParser.ArgumentContext):
        self.indent -= 1
        print(" " * self.indent, "exitArgument")

    def enterRedirection(self, ctx: CommandParser.RedirectionContext):
        print(" " * self.indent, "enterRedirection")
        self.indent += 1

    def exitRedirection(self, ctx: CommandParser.RedirectionContext):
        self.indent -= 1
        print(" " * self.indent, "exitRedirection")

    def enterQuoted(self, ctx: CommandParser.QuotedContext):
        print(" " * self.indent, "enterQuoted")
        self.indent += 1

    def exitQuoted(self, ctx: CommandParser.QuotedContext):
        self.indent -= 1
        print(" " * self.indent, "exitQuoted")
