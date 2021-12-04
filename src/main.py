from parser.python.CommandLexer import CommandLexer
from parser.python.CommandParser import CommandParser
from ParsingTesterListener import CustomCommandListener
from antlr4 import *
import sys
from applications import *
from evaluator import Evaluator
from collections import deque
import logging

logging.DEBUG = True
logging.basicConfig(format="%(message)s", level=logging.DEBUG)
logging.debug("This message should appear on the console")

DEBUG = True


def run(s):
    lexer = CommandLexer(InputStream(s))
    stream = CommonTokenStream(lexer)
    parser = CommandParser(stream)
    tree = parser.command()
    # if DEBUG:  # listener runs in DEBUG mode
    #     printer = CustomCommandListener()
    #     walker = ParseTreeWalker()
    #     walker.walk(printer, tree)
    # print("*" * 50)
    cmd = tree.accept(Evaluator())
    print(f"{cmd}")


def run_shell():
    while True:
        print(os.getcwd() + "> ", end="")
        cmdline = input()
        run(cmdline)
        # while len(out) > 0:
        #     print(out.popleft(), end="")


if __name__ == "__main__":
    run_shell()
    # s = "echo `ls`"
    # run(s)
