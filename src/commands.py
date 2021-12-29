import sys
from collections import deque
from typing import List
from abc import ABC, abstractmethod

from applications import ApplicationFactory


def deque_to_str(deque: deque) -> str:
    s = ""
    while len(deque) > 0:
        s += deque.popleft()
    return s


def read_from_file(filename):
    try:
        with open(filename, "r") as f:
            content = f.read()
            return content
    except FileNotFoundError:
        raise FileNotFoundError(f"Could not find the file: {filename}")


class Command:  # pragma: no cover

    def eval(self, input=None, output=None):
        return


class Pipe(Command):
    # reference to commands and calls

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self, input=None, output=None):
        content_list = deque()
        self.left.eval(input=input, output=content_list)
        new_input = deque_to_str(content_list)
        self.right.eval(input=new_input, output=output)


class Seq(Command):
    def __init__(self, initial_command: Command):
        self.commands = [initial_command]

    def add_command(self, command: Command):
        self.commands.append(command)

    def eval(self, input=None, output=None):
        for command in self.commands:
            command.eval(output=output)


class Call(Command):

    app_factory = ApplicationFactory()

    def __init__(
        self,
        app_name: str,
        args: List,
        redirect_from: List,
        redirect_to: List
    ):
        self.app = self.app_factory.create(app_name)
        self.args = args
        if len(redirect_from) == 0:
            self.redirect_from = None
        elif len(redirect_from) == 1:
            self.redirect_from = redirect_from[0]
        else:  # > 0
            raise ValueError("Multiple files specified for input redirection")
        if len(redirect_to) == 0:
            self.redirect_to = None
        elif len(redirect_to) == 1:
            self.redirect_to = redirect_to[0]
        else:
            raise ValueError("Multiple files specified for output redirection")

    def eval(self, args=None, input=None, output=None):
        # set print_output to True if not to be outputed to external Command
        print_output = output is None
        if print_output:
            output = deque()
        # If args not specified, get attr. after parsing/converting
        if args is None:
            args = self.args
        # Handle input redirections
        if self.redirect_from is not None:  # read input from file
            input = read_from_file(self.redirect_from)
        # Execute the app
        self.app.exec(args, input, output)
        # Handle output redirection by writing the output of executed app
        original_stdout = sys.stdout
        if self.redirect_to is not None:
            with open(self.redirect_to, "w") as f:
                sys.stdout = f
                print(deque_to_str(output))
            sys.stdout = original_stdout
        else:
            if print_output:
                print(deque_to_str(output))
