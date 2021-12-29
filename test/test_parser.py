import unittest

from antlr4 import InputStream, CommonTokenStream

from src.converter import Converter
from src.parser.CommandLexer import CommandLexer
from src.parser.CommandParser import CommandParser


class TestParser(unittest.TestCase):

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
        self.assertEqual(type(parse_tree).__name__, "Call")
        self.assertEqual(type(parse_tree.app).__name__, "Echo")
        self.assertEqual(parse_tree.args, ["hello", "world"])

    def test_command_arg_with_slash(self):
        parse_tree = self.do_parse("ls dir2/subdir")
        self.assertEqual(type(parse_tree).__name__, "Call")
        self.assertEqual(type(parse_tree.app).__name__, "Ls")
        self.assertEqual(parse_tree.args, ["dir2/subdir"])

    def test_single_quote_string(self):
        parse_tree = self.do_parse("grep 'A..' dir1/file1.txt")
        self.assertEqual(type(parse_tree).__name__, "Call")
        self.assertEqual(type(parse_tree.app).__name__, "Grep")
        self.assertEqual(parse_tree.args, ["'A..'", "dir1/file1.txt"])
