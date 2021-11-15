// Generated from Command.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link CommandParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface CommandVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link CommandParser#command}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCommand(CommandParser.CommandContext ctx);
	/**
	 * Visit a parse tree produced by {@link CommandParser#commandSeq}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCommandSeq(CommandParser.CommandSeqContext ctx);
	/**
	 * Visit a parse tree produced by {@link CommandParser#callPipe}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCallPipe(CommandParser.CallPipeContext ctx);
	/**
	 * Visit a parse tree produced by {@link CommandParser#call}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCall(CommandParser.CallContext ctx);
	/**
	 * Visit a parse tree produced by {@link CommandParser#atom}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAtom(CommandParser.AtomContext ctx);
	/**
	 * Visit a parse tree produced by {@link CommandParser#argument}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitArgument(CommandParser.ArgumentContext ctx);
	/**
	 * Visit a parse tree produced by {@link CommandParser#redirection}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRedirection(CommandParser.RedirectionContext ctx);
	/**
	 * Visit a parse tree produced by {@link CommandParser#quoted}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitQuoted(CommandParser.QuotedContext ctx);
}