import unittest

from antlr4 import InputStream

from src.parser.CommandLexer import CommandLexer


class TestLexer(unittest.TestCase):

    def do_lex(self, input_string):
        lexer = CommandLexer(InputStream(input_string))
        tokens = []
        while not lexer._hitEOF:
            nt = lexer.nextToken()
            tokens.append(nt.text)
        return tokens

    def test_empty_command(self):
        self.assertEqual(
            self.do_lex(""),
            ["<EOF>"]
        )

    def test_basic_command(self):
        self.assertEqual(
            self.do_lex("echo hello world"),
            ["echo", " ", "hello", " ", "world"]
        )

    def test_command_arg_with_slash(self):
        self.assertEqual(
            self.do_lex("ls dir2/subdir"),
            ["ls", " ", "dir2/subdir"]
        )

    def test_double_quote_string(self):
        self.assertEqual(
            self.do_lex('echo "hello world"'),
            ["echo", " ", '"hello world"']
        )

    def test_single_quote_string(self):
        self.assertEqual(
            self.do_lex("grep 'A..' dir1/file1.txt"),
            ["grep", " ", "'A..'", " ", "dir1/file1.txt"]
        )

    def test_command_sequence(self):
        self.assertEqual(
            self.do_lex("cd dir1; pwd"),
            ["cd", " ", "dir1", ";", " ", "pwd"]
        )

    def test_redirection(self):
        self.assertEqual(
            self.do_lex("cat < dir1/file1.txt"),
            ["cat", " ", "<", " ", "dir1/file1.txt"]
        )

    def test_command_flag(self):
        self.assertEqual(
            self.do_lex("head -n 5 dir1/longfile.txt"),
            ["head", " ", "-n", " ", "5", " ", "dir1/longfile.txt"]
        )

    def test_pipe(self):
        self.assertEqual(
            self.do_lex("sort dir1/file1.txt | uniq"),
            ["sort", " ", "dir1/file1.txt", " ", "|", " ", "uniq"]
        )

    def test_large_compound_command(self):
        self.assertEqual(
            self.do_lex("echo aaa > dir1/file2.txt; cat dir1/file1.txt dir1/file2.txt | uniq -i"),
            ["echo", " ", "aaa", " ", ">", " ", "dir1/file2.txt", ";", " ", "cat", " ", "dir1/file1.txt", " ",
             "dir1/file2.txt", " ", "|", " ", "uniq", " ", "-i"]
        )

    def test_substitution(self):
        self.assertEqual(
            self.do_lex("echo `echo foo`"),
            ["echo", " ", "`echo foo`"]
        )

    def test_substitution_insidearg(self):
        self.assertEqual(
            self.do_lex("echo a`echo a`a"),
            ["echo", " ", "a", "`echo a`", "a"]
        )

    def test_substitution_doublequotes(self):
        self.assertEqual(
            self.do_lex('echo "`echo foo`"'),
            ["echo", " ", '"`echo foo`"']
        )

    def test_nested_doublequotes(self):
        self.assertEqual(
            self.do_lex('echo "a `echo "b"`"'),
            ["echo", " ", '"a `echo "b"`"']
        )

    def test_disabled_doublequotes(self):
        self.assertEqual(
            self.do_lex("echo '\"\"'"),
            ["echo", " ", '\'""\'']
        )

    def test_splitting(self):
        self.assertEqual(
            self.do_lex('echo a"b"c'),
            ["echo", " ", "a", '"b"', "c"]
        )
