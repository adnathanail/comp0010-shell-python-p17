# Generated from Command.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\6")
        buf.write("%\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\3\3\6\3")
        buf.write("\17\n\3\r\3\16\3\20\3\4\7\4\24\n\4\f\4\16\4\27\13\4\3")
        buf.write("\4\3\4\5\4\33\n\4\3\4\7\4\36\n\4\f\4\16\4!\13\4\3\5\3")
        buf.write("\5\3\5\2\2\6\2\4\6\b\2\3\3\2\4\5\2$\2\n\3\2\2\2\4\16\3")
        buf.write("\2\2\2\6\25\3\2\2\2\b\"\3\2\2\2\n\13\5\4\3\2\13\f\7\2")
        buf.write("\2\3\f\3\3\2\2\2\r\17\5\6\4\2\16\r\3\2\2\2\17\20\3\2\2")
        buf.write("\2\20\16\3\2\2\2\20\21\3\2\2\2\21\5\3\2\2\2\22\24\7\6")
        buf.write("\2\2\23\22\3\2\2\2\24\27\3\2\2\2\25\23\3\2\2\2\25\26\3")
        buf.write("\2\2\2\26\32\3\2\2\2\27\25\3\2\2\2\30\33\7\3\2\2\31\33")
        buf.write("\5\b\5\2\32\30\3\2\2\2\32\31\3\2\2\2\33\37\3\2\2\2\34")
        buf.write("\36\7\6\2\2\35\34\3\2\2\2\36!\3\2\2\2\37\35\3\2\2\2\37")
        buf.write(" \3\2\2\2 \7\3\2\2\2!\37\3\2\2\2\"#\t\2\2\2#\t\3\2\2\2")
        buf.write("\6\20\25\32\37")
        return buf.getvalue()


class CommandParser ( Parser ):

    grammarFileName = "Command.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "UNQUOTED_CONTENT", "SINGLE_QUOTED", 
                      "BACKQUOTED", "WHITESPACE" ]

    RULE_command = 0
    RULE_call = 1
    RULE_argument = 2
    RULE_quoted = 3

    ruleNames =  [ "command", "call", "argument", "quoted" ]

    EOF = Token.EOF
    UNQUOTED_CONTENT=1
    SINGLE_QUOTED=2
    BACKQUOTED=3
    WHITESPACE=4

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def call(self):
            return self.getTypedRuleContext(CommandParser.CallContext,0)


        def EOF(self):
            return self.getToken(CommandParser.EOF, 0)

        def getRuleIndex(self):
            return CommandParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)




    def command(self):

        localctx = CommandParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_command)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.call()
            self.state = 9
            self.match(CommandParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CommandParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(CommandParser.ArgumentContext,i)


        def getRuleIndex(self):
            return CommandParser.RULE_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCall" ):
                listener.enterCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCall" ):
                listener.exitCall(self)




    def call(self):

        localctx = CommandParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 11
                self.argument()
                self.state = 14 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CommandParser.UNQUOTED_CONTENT) | (1 << CommandParser.SINGLE_QUOTED) | (1 << CommandParser.BACKQUOTED) | (1 << CommandParser.WHITESPACE))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UNQUOTED_CONTENT(self):
            return self.getToken(CommandParser.UNQUOTED_CONTENT, 0)

        def quoted(self):
            return self.getTypedRuleContext(CommandParser.QuotedContext,0)


        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(CommandParser.WHITESPACE)
            else:
                return self.getToken(CommandParser.WHITESPACE, i)

        def getRuleIndex(self):
            return CommandParser.RULE_argument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgument" ):
                listener.enterArgument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgument" ):
                listener.exitArgument(self)




    def argument(self):

        localctx = CommandParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_argument)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CommandParser.WHITESPACE:
                self.state = 16
                self.match(CommandParser.WHITESPACE)
                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 24
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CommandParser.UNQUOTED_CONTENT]:
                self.state = 22
                self.match(CommandParser.UNQUOTED_CONTENT)
                pass
            elif token in [CommandParser.SINGLE_QUOTED, CommandParser.BACKQUOTED]:
                self.state = 23
                self.quoted()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 29
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 26
                    self.match(CommandParser.WHITESPACE) 
                self.state = 31
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QuotedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SINGLE_QUOTED(self):
            return self.getToken(CommandParser.SINGLE_QUOTED, 0)

        def BACKQUOTED(self):
            return self.getToken(CommandParser.BACKQUOTED, 0)

        def getRuleIndex(self):
            return CommandParser.RULE_quoted

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuoted" ):
                listener.enterQuoted(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuoted" ):
                listener.exitQuoted(self)




    def quoted(self):

        localctx = CommandParser.QuotedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_quoted)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            _la = self._input.LA(1)
            if not(_la==CommandParser.SINGLE_QUOTED or _la==CommandParser.BACKQUOTED):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





