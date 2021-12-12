from applications import ApplicationFactory
from collections import deque
import glob
import logging
import os


class Command:

    app_factory = ApplicationFactory()

    def __repr__(self) -> str:
        return self.__str__()

    def eval(self, input, output):
        pass


class Pipe(Command):
    # reference to commands and calls

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return f"Pipe({self.left} | {self.right})"

    def eval(self, input=None, output=None):
        content_list = deque()
        self.left.eval(input=input, output=content_list)
        self.right.eval(input=content_list, output=output)


class Seq(Command):
    def __init__(self, command=None):
        if command is not None:
            self.commands = [command]
        else:
            self.command = []

    def __str__(self):
        return f"Seq({str(self.commands)}"

    def addCommand(self, command):
        self.commands.append(command)

    def eval(self, input=None, output=None):
        print_output = False
        if output is None:
            output = deque()
            print_output = True
        for command in self.commands:
            command.eval(output=output)
            if print_output:
                while len(output) > 0:
                    print(output.popleft(), end="")


class Call(Command):
    def __init__(self, app_name, args, redirectionIn, redirectionOut):
        self.app = self.app_factory.create(app_name)
        self.args = args
        self.redirectionIn = redirectionIn
        self.redirectionOut = redirectionOut

    def __str__(self):
        return (
            f"{str(self.app).capitalize()}"
            f"(args={self.args},"
            f"redirectionIn={self.redirectionIn},"
            f"redirectionOut={self.redirectionOut})"
        )

    def eval(self, args=None, input=None, output=None):
        logging.debug(f"ARGS IN EVAL: {self.args}")
        # TODO: expanding filenames (globbing)
        # TODO: handle redirections
        # if multiple files specified for I/O
        if len(self.redirectionIn) > 1 or len(self.redirectionOut) > 1:
            raise ValueError("Multiple files specified for I/O")
        if args is None:
            args = self.args
        self.app.exec(args, input, output)
