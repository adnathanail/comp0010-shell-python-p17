grammar Command;

/*
 * Lexer Rules
 */

ARGUMENT : (~[ \t])+ ;

WHITESPACE          : (' ' | '\t') ;

/*
 * Parser Rules
 */

command                : call EOF ;

call                : (argument)+ ;

argument : WHITESPACE* ARGUMENT WHITESPACE*;
