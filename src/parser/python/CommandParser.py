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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\4")
        buf.write("\36\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\3\2\3\3\6\3\r\n\3")
        buf.write("\r\3\16\3\16\3\4\7\4\22\n\4\f\4\16\4\25\13\4\3\4\3\4\7")
        buf.write("\4\31\n\4\f\4\16\4\34\13\4\3\4\2\2\5\2\4\6\2\2\2\35\2")
        buf.write("\b\3\2\2\2\4\f\3\2\2\2\6\23\3\2\2\2\b\t\5\4\3\2\t\n\7")
        buf.write("\2\2\3\n\3\3\2\2\2\13\r\5\6\4\2\f\13\3\2\2\2\r\16\3\2")
        buf.write("\2\2\16\f\3\2\2\2\16\17\3\2\2\2\17\5\3\2\2\2\20\22\7\4")
        buf.write("\2\2\21\20\3\2\2\2\22\25\3\2\2\2\23\21\3\2\2\2\23\24\3")
        buf.write("\2\2\2\24\26\3\2\2\2\25\23\3\2\2\2\26\32\7\3\2\2\27\31")
        buf.write("\7\4\2\2\30\27\3\2\2\2\31\34\3\2\2\2\32\30\3\2\2\2\32")
        buf.write("\33\3\2\2\2\33\7\3\2\2\2\34\32\3\2\2\2\5\16\23\32")
        return buf.getvalue()


class CommandParser ( Parser ):

    grammarFileName = "Command.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "ARGUMENT", "WHITESPACE" ]

    RULE_command = 0
    RULE_call = 1
    RULE_argument = 2

    ruleNames =  [ "command", "call", "argument" ]

    EOF = Token.EOF
    ARGUMENT=1
    WHITESPACE=2

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
            self.state = 6
            self.call()
            self.state = 7
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
            self.state = 10 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 9
                self.argument()
                self.state = 12 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CommandParser.ARGUMENT or _la==CommandParser.WHITESPACE):
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

        def ARGUMENT(self):
            return self.getToken(CommandParser.ARGUMENT, 0)

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
            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CommandParser.WHITESPACE:
                self.state = 14
                self.match(CommandParser.WHITESPACE)
                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 20
            self.match(CommandParser.ARGUMENT)
            self.state = 24
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 21
                    self.match(CommandParser.WHITESPACE) 
                self.state = 26
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





