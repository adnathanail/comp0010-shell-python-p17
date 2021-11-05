// Generated from Command.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link CommandParser}.
 */
public interface CommandListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link CommandParser#command}.
	 * @param ctx the parse tree
	 */
	void enterCommand(CommandParser.CommandContext ctx);
	/**
	 * Exit a parse tree produced by {@link CommandParser#command}.
	 * @param ctx the parse tree
	 */
	void exitCommand(CommandParser.CommandContext ctx);
	/**
	 * Enter a parse tree produced by {@link CommandParser#commandSeq}.
	 * @param ctx the parse tree
	 */
	void enterCommandSeq(CommandParser.CommandSeqContext ctx);
	/**
	 * Exit a parse tree produced by {@link CommandParser#commandSeq}.
	 * @param ctx the parse tree
	 */
	void exitCommandSeq(CommandParser.CommandSeqContext ctx);
	/**
	 * Enter a parse tree produced by {@link CommandParser#callPipe}.
	 * @param ctx the parse tree
	 */
	void enterCallPipe(CommandParser.CallPipeContext ctx);
	/**
	 * Exit a parse tree produced by {@link CommandParser#callPipe}.
	 * @param ctx the parse tree
	 */
	void exitCallPipe(CommandParser.CallPipeContext ctx);
	/**
	 * Enter a parse tree produced by {@link CommandParser#call}.
	 * @param ctx the parse tree
	 */
	void enterCall(CommandParser.CallContext ctx);
	/**
	 * Exit a parse tree produced by {@link CommandParser#call}.
	 * @param ctx the parse tree
	 */
	void exitCall(CommandParser.CallContext ctx);
	/**
	 * Enter a parse tree produced by {@link CommandParser#atom}.
	 * @param ctx the parse tree
	 */
	void enterAtom(CommandParser.AtomContext ctx);
	/**
	 * Exit a parse tree produced by {@link CommandParser#atom}.
	 * @param ctx the parse tree
	 */
	void exitAtom(CommandParser.AtomContext ctx);
	/**
	 * Enter a parse tree produced by {@link CommandParser#argument}.
	 * @param ctx the parse tree
	 */
	void enterArgument(CommandParser.ArgumentContext ctx);
	/**
	 * Exit a parse tree produced by {@link CommandParser#argument}.
	 * @param ctx the parse tree
	 */
	void exitArgument(CommandParser.ArgumentContext ctx);
	/**
	 * Enter a parse tree produced by {@link CommandParser#redirection}.
	 * @param ctx the parse tree
	 */
	void enterRedirection(CommandParser.RedirectionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CommandParser#redirection}.
	 * @param ctx the parse tree
	 */
	void exitRedirection(CommandParser.RedirectionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CommandParser#quoted}.
	 * @param ctx the parse tree
	 */
	void enterQuoted(CommandParser.QuotedContext ctx);
	/**
	 * Exit a parse tree produced by {@link CommandParser#quoted}.
	 * @param ctx the parse tree
	 */
	void exitQuoted(CommandParser.QuotedContext ctx);
}