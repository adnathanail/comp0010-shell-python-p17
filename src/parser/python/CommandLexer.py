# Generated from Command.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\6")
        buf.write("\"\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\6\2\r\n\2\r")
        buf.write("\2\16\2\16\3\3\3\3\6\3\23\n\3\r\3\16\3\24\3\3\3\3\3\4")
        buf.write("\3\4\6\4\33\n\4\r\4\16\4\34\3\4\3\4\3\5\3\5\2\2\6\3\3")
        buf.write("\5\4\7\5\t\6\3\2\5\4\2\13\13\"\"\4\2\f\f))\4\2\f\fbb\2")
        buf.write("$\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\3\f")
        buf.write("\3\2\2\2\5\20\3\2\2\2\7\30\3\2\2\2\t \3\2\2\2\13\r\n\2")
        buf.write("\2\2\f\13\3\2\2\2\r\16\3\2\2\2\16\f\3\2\2\2\16\17\3\2")
        buf.write("\2\2\17\4\3\2\2\2\20\22\7)\2\2\21\23\n\3\2\2\22\21\3\2")
        buf.write("\2\2\23\24\3\2\2\2\24\22\3\2\2\2\24\25\3\2\2\2\25\26\3")
        buf.write("\2\2\2\26\27\7)\2\2\27\6\3\2\2\2\30\32\7b\2\2\31\33\n")
        buf.write("\4\2\2\32\31\3\2\2\2\33\34\3\2\2\2\34\32\3\2\2\2\34\35")
        buf.write("\3\2\2\2\35\36\3\2\2\2\36\37\7b\2\2\37\b\3\2\2\2 !\t\2")
        buf.write("\2\2!\n\3\2\2\2\6\2\16\24\34\2")
        return buf.getvalue()


class CommandLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    UNQUOTED_CONTENT = 1
    SINGLE_QUOTED = 2
    BACKQUOTED = 3
    WHITESPACE = 4

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "UNQUOTED_CONTENT", "SINGLE_QUOTED", "BACKQUOTED", "WHITESPACE" ]

    ruleNames = [ "UNQUOTED_CONTENT", "SINGLE_QUOTED", "BACKQUOTED", "WHITESPACE" ]

    grammarFileName = "Command.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


