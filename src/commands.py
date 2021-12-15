import logging
from collections import deque
from typing import List

from applications import ApplicationFactory


def dequeToStr(deque: deque):
    s = ""
    while len(deque) > 0:
        s += deque.popleft()
    return s


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
        new_input = dequeToStr(content_list)
        self.right.eval(input=new_input, output=output)


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
    def __init__(
        self,
        app_name: str,
        args: List,
        redirectFrom: List,
        redirectTo: List
    ):
        self.app = self.app_factory.create(app_name)
        self.args = args
        if len(redirectFrom) == 0:
            self.redirectFrom = None
        elif len(redirectFrom) == 1:
            self.redirectFrom = redirectFrom[0]
        else:  # > 0
            raise ValueError("Multiple files specified for input redirection")
        if len(redirectTo) == 0:
            self.redirectTo = None
        elif len(redirectTo) == 1:
            self.redirectTo = redirectTo[0]
        else:
            raise ValueError("Multiple files specified for output redirection")

    def __str__(self):
        return (
            f"{str(self.app).capitalize()}"
            f"(args={self.args},"
            f"redirectFrom={self.redirectFrom},"
            f"redirectTo={self.redirectTo})"
        )

    def eval(self, args=None, input=None, output=None):
        logging.debug(f"ARGS IN EVAL: {self.args}")
        # TODO: expanding filenames (globbing)
        if args is None:
            args = self.args
        # Handle input redirections
        if self.redirectFrom is not None:  # read input from file
            input = self.readFromFile(self.redirectFrom)
        # Execute the app
        self.app.exec(args, input, output)
        # Handle output redirection by writing the output of executed app
        if self.redirectTo is not None:
            self.writeToFile(self.redirectTo, output)

    def writeToFile(self, filename, output):
        # overwrites existent or creates a new file
        with open(filename, "w") as f:
            while len(output) > 0:
                f.write(output.popleft())

    def readFromFile(self, filename):
        try:
            with open(filename, "r") as f:
                content = f.read()
                return content
        except FileNotFoundError:
            raise FileNotFoundError(f"Could not find the file: {filename}")
