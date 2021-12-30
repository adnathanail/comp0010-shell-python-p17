import unittest

from antlr4 import InputStream, CommonTokenStream

from src.converter import Converter
from src.parser.CommandLexer import CommandLexer
from src.parser.CommandParser import CommandParser


class TestParser(unittest.TestCase):

    def assertCallType(self, potential_call, app_name, args=None, redirect_from=None, redirect_to=None):
        if args is None:
            args = []
        self.assertEqual(type(potential_call).__name__, "Call")
        self.assertEqual(type(potential_call.app).__name__, app_name)
        self.assertEqual(potential_call.args, args)
        self.assertEqual(potential_call.redirect_from, redirect_from)
        self.assertEqual(potential_call.redirect_to, redirect_to)

    def do_parse(self, input_string):
        lexer = CommandLexer(InputStream(input_string))
        stream = CommonTokenStream(lexer)
        parser = CommandParser(stream)
        tree = parser.command()
        return tree.accept(Converter())

    def test_empty_command(self):
        parse_tree = self.do_parse("")
        self.assertEqual(type(parse_tree).__name__, "Command")

    def test_basic_command(self):
        parse_tree = self.do_parse("echo hello world")
        self.assertCallType(parse_tree, "Echo", ["hello", "world"])

    def test_command_arg_with_slash(self):
        parse_tree = self.do_parse("ls dir2/subdir")
        self.assertCallType(parse_tree, "Ls", ["dir2/subdir"])

    def test_double_quote_string(self):
        parse_tree = self.do_parse('echo "hello world"')
        self.assertCallType(parse_tree, "Echo", ["hello world"])

    def test_single_quote_string(self):
        parse_tree = self.do_parse("grep 'A..' dir1/file1.txt")
        self.assertCallType(parse_tree, "Grep", ["A..", "dir1/file1.txt"])

    def test_command_sequence(self):
        parse_tree = self.do_parse("cd dir1; pwd")
        self.assertEqual(type(parse_tree).__name__, "Seq")
        self.assertEqual(len(parse_tree.commands), 2)
        self.assertCallType(parse_tree.commands[0], "Cd", ["dir1"])
        self.assertCallType(parse_tree.commands[1], "Pwd")

    def test_redirection(self):
        parse_tree = self.do_parse("cat < dir1/file1.txt")
        self.assertCallType(parse_tree, "Cat", redirect_from="dir1/file1.txt")

    def test_command_flag(self):
        parse_tree = self.do_parse("head -n 5 dir1/longfile.txt")
        self.assertCallType(parse_tree, "Head", ["-n", "5", "dir1/longfile.txt"])

    def test_pipe(self):
        parse_tree = self.do_parse("sort dir1/file1.txt | uniq")
        self.assertEqual(type(parse_tree).__name__, "Pipe")
        self.assertCallType(parse_tree.left, "Sort", ["dir1/file1.txt"])
        self.assertCallType(parse_tree.right, "Uniq", [])

    def test_large_compound_command(self):
        parse_tree = self.do_parse("echo aaa > dir1/file2.txt; cat dir1/file1.txt dir1/file2.txt | uniq -i")
        self.assertEqual(len(parse_tree.commands), 2)
        self.assertCallType(parse_tree.commands[0], "Echo", ["aaa"], redirect_to="dir1/file2.txt")
        self.assertEqual(type(parse_tree.commands[1]).__name__, "Pipe")
        self.assertCallType(parse_tree.commands[1].left, "Cat", ["dir1/file1.txt", "dir1/file2.txt"])
        self.assertCallType(parse_tree.commands[1].right, "Uniq", ["-i"])

    def test_substitution(self):
        parse_tree = self.do_parse("echo `echo foo`")
        self.assertCallType(parse_tree, "Echo", ["foo"])

    def test_substitution_insidearg(self):
        parse_tree = self.do_parse("echo a`echo a`a")
        self.assertCallType(parse_tree, "Echo", ["aaa"])

    def test_substitution_doublequotes(self):
        parse_tree = self.do_parse('echo "`echo foo`"')
        self.assertCallType(parse_tree, "Echo", ["foo"])

    def test_nested_doublequotes(self):
        parse_tree = self.do_parse('echo "a `echo "b"`"')
        self.assertCallType(parse_tree, "Echo", ["a b"])

    def test_disabled_doublequotes(self):
        parse_tree = self.do_parse("echo '\"\"'")
        self.assertCallType(parse_tree, "Echo", ['\"\"'])

    def test_splitting(self):
        parse_tree = self.do_parse('echo a"b"c')
        self.assertCallType(parse_tree, "Echo", ["abc"])
