from parser.python.CommandLexer import CommandLexer
from parser.python.CommandParser import CommandParser
from ParsingTesterListener import CustomCommandListener
from antlr4 import *
import sys
from applications import *
from evaluator import Evaluator
from collections import deque
import logging

logging.DEBUG = False
logging.basicConfig(format="%(message)s", level=logging.DEBUG)


def run(cmdline):
    lexer = CommandLexer(InputStream(cmdline))
    stream = CommonTokenStream(lexer)
    parser = CommandParser(stream)
    tree = parser.command()
    # listener
    # printer = CustomCommandListener()
    # walker = ParseTreeWalker()
    # walker.walk(printer, tree)
    cmd = tree.accept(Evaluator())  # convert
    logging.debug(f"{cmd}")
    out = cmd.eval()  # evaluate
    if out != "":  # temporal
        print(out)


def run_shell():
    while True:
        print(os.getcwd() + "> ", end="")
        cmdline = input()
        run(cmdline)


if __name__ == "__main__":
    run_shell()
