from parser.python.CommandLexer import CommandLexer
from parser.python.CommandParser import CommandParser
from ParsingTesterListener import CustomCommandListener
from antlr4 import *
import sys
from applications import *
from evaluator import Evaluator


DEBUG = True


def run(s):
    lexer = CommandLexer(InputStream(s))
    stream = CommonTokenStream(lexer)
    parser = CommandParser(stream)
    tree = parser.command()
    if DEBUG:  # listener runs in DEBUG mode
        printer = CustomCommandListener()
        walker = ParseTreeWalker()
        walker.walk(printer, tree)
        # print("*" * 50)
    # visitor = Evaluator()
    # tree.accept(visitor)


if __name__ == "__main__":
    s = "echo `ls`"
    run(s)
