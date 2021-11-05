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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\n")
        buf.write("\62\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write("\7\4\b\t\b\4\t\t\t\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6")
        buf.write("\6\6\35\n\6\r\6\16\6\36\3\7\3\7\6\7#\n\7\r\7\16\7$\3\7")
        buf.write("\3\7\3\b\3\b\6\b+\n\b\r\b\16\b,\3\b\3\b\3\t\3\t\2\2\n")
        buf.write("\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\3\2\6\7\2\13\f\"\"")
        buf.write("=>@@~~\4\2\f\f))\4\2\f\fbb\4\2\13\13\"\"\2\64\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\3\23\3\2\2\2\5")
        buf.write("\25\3\2\2\2\7\27\3\2\2\2\t\31\3\2\2\2\13\34\3\2\2\2\r")
        buf.write(" \3\2\2\2\17(\3\2\2\2\21\60\3\2\2\2\23\24\7=\2\2\24\4")
        buf.write("\3\2\2\2\25\26\7~\2\2\26\6\3\2\2\2\27\30\7>\2\2\30\b\3")
        buf.write("\2\2\2\31\32\7@\2\2\32\n\3\2\2\2\33\35\n\2\2\2\34\33\3")
        buf.write("\2\2\2\35\36\3\2\2\2\36\34\3\2\2\2\36\37\3\2\2\2\37\f")
        buf.write("\3\2\2\2 \"\7)\2\2!#\n\3\2\2\"!\3\2\2\2#$\3\2\2\2$\"\3")
        buf.write("\2\2\2$%\3\2\2\2%&\3\2\2\2&\'\7)\2\2\'\16\3\2\2\2(*\7")
        buf.write("b\2\2)+\n\4\2\2*)\3\2\2\2+,\3\2\2\2,*\3\2\2\2,-\3\2\2")
        buf.write("\2-.\3\2\2\2./\7b\2\2/\20\3\2\2\2\60\61\t\5\2\2\61\22")
        buf.write("\3\2\2\2\6\2\36$,\2")
        return buf.getvalue()


class CommandLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    UNQUOTED_CONTENT = 5
    SINGLE_QUOTED = 6
    BACKQUOTED = 7
    WHITESPACE = 8

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "'|'", "'<'", "'>'" ]

    symbolicNames = [ "<INVALID>",
            "UNQUOTED_CONTENT", "SINGLE_QUOTED", "BACKQUOTED", "WHITESPACE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "UNQUOTED_CONTENT", "SINGLE_QUOTED", 
                  "BACKQUOTED", "WHITESPACE" ]

    grammarFileName = "Command.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


