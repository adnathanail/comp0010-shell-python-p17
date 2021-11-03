// Generated from Command.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class CommandParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		ARGUMENT=1, WHITESPACE=2;
	public static final int
		RULE_command = 0, RULE_call = 1, RULE_argument = 2;
	private static String[] makeRuleNames() {
		return new String[] {
			"command", "call", "argument"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "ARGUMENT", "WHITESPACE"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Command.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public CommandParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class CommandContext extends ParserRuleContext {
		public CallContext call() {
			return getRuleContext(CallContext.class,0);
		}
		public TerminalNode EOF() { return getToken(CommandParser.EOF, 0); }
		public CommandContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_command; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CommandListener ) ((CommandListener)listener).enterCommand(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CommandListener ) ((CommandListener)listener).exitCommand(this);
		}
	}

	public final CommandContext command() throws RecognitionException {
		CommandContext _localctx = new CommandContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_command);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(6);
			call();
			setState(7);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CallContext extends ParserRuleContext {
		public List<ArgumentContext> argument() {
			return getRuleContexts(ArgumentContext.class);
		}
		public ArgumentContext argument(int i) {
			return getRuleContext(ArgumentContext.class,i);
		}
		public CallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_call; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CommandListener ) ((CommandListener)listener).enterCall(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CommandListener ) ((CommandListener)listener).exitCall(this);
		}
	}

	public final CallContext call() throws RecognitionException {
		CallContext _localctx = new CallContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_call);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(10); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(9);
				argument();
				}
				}
				setState(12); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==ARGUMENT || _la==WHITESPACE );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ArgumentContext extends ParserRuleContext {
		public TerminalNode ARGUMENT() { return getToken(CommandParser.ARGUMENT, 0); }
		public List<TerminalNode> WHITESPACE() { return getTokens(CommandParser.WHITESPACE); }
		public TerminalNode WHITESPACE(int i) {
			return getToken(CommandParser.WHITESPACE, i);
		}
		public ArgumentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_argument; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CommandListener ) ((CommandListener)listener).enterArgument(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CommandListener ) ((CommandListener)listener).exitArgument(this);
		}
	}

	public final ArgumentContext argument() throws RecognitionException {
		ArgumentContext _localctx = new ArgumentContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_argument);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(17);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==WHITESPACE) {
				{
				{
				setState(14);
				match(WHITESPACE);
				}
				}
				setState(19);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(20);
			match(ARGUMENT);
			setState(24);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(21);
					match(WHITESPACE);
					}
					} 
				}
				setState(26);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\4\36\4\2\t\2\4\3"+
		"\t\3\4\4\t\4\3\2\3\2\3\2\3\3\6\3\r\n\3\r\3\16\3\16\3\4\7\4\22\n\4\f\4"+
		"\16\4\25\13\4\3\4\3\4\7\4\31\n\4\f\4\16\4\34\13\4\3\4\2\2\5\2\4\6\2\2"+
		"\2\35\2\b\3\2\2\2\4\f\3\2\2\2\6\23\3\2\2\2\b\t\5\4\3\2\t\n\7\2\2\3\n\3"+
		"\3\2\2\2\13\r\5\6\4\2\f\13\3\2\2\2\r\16\3\2\2\2\16\f\3\2\2\2\16\17\3\2"+
		"\2\2\17\5\3\2\2\2\20\22\7\4\2\2\21\20\3\2\2\2\22\25\3\2\2\2\23\21\3\2"+
		"\2\2\23\24\3\2\2\2\24\26\3\2\2\2\25\23\3\2\2\2\26\32\7\3\2\2\27\31\7\4"+
		"\2\2\30\27\3\2\2\2\31\34\3\2\2\2\32\30\3\2\2\2\32\33\3\2\2\2\33\7\3\2"+
		"\2\2\34\32\3\2\2\2\5\16\23\32";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}