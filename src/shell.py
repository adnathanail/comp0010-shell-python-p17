import logging
import os
import sys

from antlr4 import InputStream, CommonTokenStream

from converter import Converter
from parser.python.CommandLexer import CommandLexer
from parser.python.CommandParser import CommandParser

logging.DEBUG = False
logging.basicConfig(format="%(message)s", level=logging.DEBUG)


def run(cmdline):
    lexer = CommandLexer(InputStream(cmdline))
    stream = CommonTokenStream(lexer)
    parser = CommandParser(stream)
    tree = parser.command()
    cmd = tree.accept(Converter())  # convert
    cmd.eval()  # evaluate
    logging.debug(f"{cmd}")


if __name__ == "__main__":
    args_num = len(sys.argv) - 1
    if args_num > 0:  # non-interactive mode
        if args_num != 2:
            raise ValueError("wrong number of command line arguments")
        if sys.argv[1] != "-c":
            raise ValueError(f"unexpected command line argument {sys.argv[1]}")
        run(sys.argv[2])
    else:
        while True:
            print(os.getcwd() + "> ", end="")
            cmdline = input()
            run(cmdline)
