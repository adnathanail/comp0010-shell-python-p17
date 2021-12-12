from parser.python.CommandLexer import CommandLexer
from parser.python.CommandParser import CommandParser
from ParsingTesterListener import CustomCommandListener
from antlr4 import *
import sys
from applications import *
from evaluator import Evaluator
import logging

logging.DEBUG = False
logging.basicConfig(format="%(message)s", level=logging.DEBUG)


def run(cmdline):
    lexer = CommandLexer(InputStream(cmdline))
    stream = CommonTokenStream(lexer)
    parser = CommandParser(stream)
    tree = parser.command()
    # listener (for debugging only)
    # printer = CustomCommandListener()
    # walker = ParseTreeWalker()
    # walker.walk(printer, tree)
    cmd = tree.accept(Evaluator())  # convert
    cmd.eval()  # evaluate
    logging.debug(f"{cmd}")


def run_shell(interactive=True):
    if interactive:
        while True:
            print(os.getcwd() + "> ", end="")
            cmdline = input()
            run(cmdline)
    else:  # non-interactive mode
        run(sys.argv[2])


if __name__ == "__main__":
    args_num = len(sys.argv) - 1
    if args_num > 0:  # non-interactive mode
        if args_num != 2:
            raise ValueError("wrong number of command line arguments")
        if sys.argv[1] != "-c":
            raise ValueError(f"unexpected command line argument {sys.argv[1]}")
        run_shell(interactive=False)
    else:  # interactive mode
        run_shell(interactive=True)
