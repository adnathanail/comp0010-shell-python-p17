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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\b")
        buf.write("*\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\3\2\3\2\3\3\3\3\3\4\6\4\25\n\4\r\4\16\4\26\3\5\3\5\6")
        buf.write("\5\33\n\5\r\5\16\5\34\3\5\3\5\3\6\3\6\6\6#\n\6\r\6\16")
        buf.write("\6$\3\6\3\6\3\7\3\7\2\2\b\3\3\5\4\7\5\t\6\13\7\r\b\3\2")
        buf.write("\6\7\2\13\f\"\"=>@@~~\4\2\f\f))\4\2\f\fbb\4\2\13\13\"")
        buf.write("\"\2,\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
        buf.write("\2\13\3\2\2\2\2\r\3\2\2\2\3\17\3\2\2\2\5\21\3\2\2\2\7")
        buf.write("\24\3\2\2\2\t\30\3\2\2\2\13 \3\2\2\2\r(\3\2\2\2\17\20")
        buf.write("\7>\2\2\20\4\3\2\2\2\21\22\7@\2\2\22\6\3\2\2\2\23\25\n")
        buf.write("\2\2\2\24\23\3\2\2\2\25\26\3\2\2\2\26\24\3\2\2\2\26\27")
        buf.write("\3\2\2\2\27\b\3\2\2\2\30\32\7)\2\2\31\33\n\3\2\2\32\31")
        buf.write("\3\2\2\2\33\34\3\2\2\2\34\32\3\2\2\2\34\35\3\2\2\2\35")
        buf.write("\36\3\2\2\2\36\37\7)\2\2\37\n\3\2\2\2 \"\7b\2\2!#\n\4")
        buf.write("\2\2\"!\3\2\2\2#$\3\2\2\2$\"\3\2\2\2$%\3\2\2\2%&\3\2\2")
        buf.write("\2&\'\7b\2\2\'\f\3\2\2\2()\t\5\2\2)\16\3\2\2\2\6\2\26")
        buf.write("\34$\2")
        return buf.getvalue()


class CommandLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    UNQUOTED_CONTENT = 3
    SINGLE_QUOTED = 4
    BACKQUOTED = 5
    WHITESPACE = 6

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'<'", "'>'" ]

    symbolicNames = [ "<INVALID>",
            "UNQUOTED_CONTENT", "SINGLE_QUOTED", "BACKQUOTED", "WHITESPACE" ]

    ruleNames = [ "T__0", "T__1", "UNQUOTED_CONTENT", "SINGLE_QUOTED", "BACKQUOTED", 
                  "WHITESPACE" ]

    grammarFileName = "Command.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


