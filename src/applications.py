from io import DEFAULT_BUFFER_SIZE
import os
from typing import List
import logging


class Application:
    """Informal application interface"""

    def exec(self, args, input, output):
        pass

    def __str__(self):
        return str(type(self).__name__)


class UnsafeWrapper(Application):
    def __init__(self, app):
        self._app = app

    def exec(self, args, input, output):
        try:
            self._app.exec(args, input, output)
        except Exception as err:
            logging.debug(err)
            return str(err)  # TODO: temporary, waits for I/O


class Pwd(Application):
    """Prints current working directory"""

    def exec(self, args, input, output):
        # no args, or input, there may be output
        cwd = os.getcwd() + "\n"
        return cwd


class Cd(Application):
    """Changes current working directory"""

    def exec(self, args, input, output):
        path = args[0]
        cwd = os.getcwd()
        os.chdir(path)


class Ls(Application):
    """
    List the content of a directory print a list of files seperated by tabs
    and followed by newline character. Ignores files and directories
    whose name start with '.'
    """

    def exec(self, args: List, input: List, output: List):
        if len(args) == 0:
            path = os.getcwd()
        elif len(args) == 1:
            path = args[0]  # PATH
        else:  # > 1
            raise ValueError("Wrong number of command line arguments")
        list_of_files = [
            fname for fname in os.listdir(path) if not (fname.startswith("."))
        ]
        if len(list_of_files) > 0:
            return "\t".join(list_of_files)
        return ""


class Cat(Application):
    """
    Concatenates the content of given files and prints it to stdout.
    """

    def exec(self, args, input, output):
        content = ""
        for file in args:
            f = open(file, "r")
            content += f.read()
            f.close()
        return content


class Echo(Application):
    """
    Prints its arguments separated by spaces and followed by a newline to stdout.
    """

    def exec(self, args, input, output):
        return " ".join(args)


class Head(Application):
    """
    Prints the first N lines of a given file or stdin.
    If there are less than N lines, prints only the existing lines
    without raising an exception.
    """

    DEFAULT_NUM_LINES = 10

    def exec(self, args, input, output):
        if len(args) == 3:
            if args[0] != "-n":
                raise ValueError("wrong flags")
            else:
                num_lines = int(args[1])
                file = args[2]
        elif len(args) == 1:
            file = args[0]
            num_lines = self.DEFAULT_NUM_LINES
        else:
            raise ValueError("wrong number of command line arguments")
        try:
            content = ""
            with open(file, "r") as f:
                content = f.readlines()
                if len(content) > num_lines:
                    content = content[:num_lines]  # grab first n lines
                content = "".join(content)
            return content
        except FileNotFoundError:
            raise FileNotFoundError("Could not find the file")


class Tail(Application):
    """
    Prints the last N lines of a given file or stdin.
    If there are less than N lines, prints only the existing lines
    without raising an exception.
    """

    DEFAULT_NUM_LINES = 10

    def exec(self, args, input, output):
        if len(args) == 3:
            if args[0] != "-n":
                raise ValueError("wrong flags")
            else:
                num_lines = int(args[1])
                file = args[2]
        elif len(args) == 1:
            file = args[0]
            num_lines = self.DEFAULT_NUM_LINES
        else:
            raise ValueError("wrong number of command line arguments")
        try:
            content = ""
            with open(file, "r") as f:
                content = f.readlines()
                if len(content) > num_lines:
                    content = content[-num_lines:]  # grab n last lines
                content = "".join(content)
            return content
        except FileNotFoundError:
            raise FileNotFoundError("Could not find the file")


class Grep(Application):
    """
    Searches for lines containing a match to the specified pattern.
    The output of the command is the list of lines.
    Each line is printed followed by a newline.
    """

    def exec(self, args, input, output):
        pass


class Cut(Application):
    """
    Cuts out sections from each line of a given file or stdin
    and prints the result to stdout.
    """

    def exec(self, args, input, output):
        pass


class Find(Application):
    """
    Recursively searches for files with matching names.
    Outputs the list of relative paths, each followed by a newline.
    """

    def exec(self, args, input, output):
        pass


class Uniq(Application):
    """
    Detects and deletes adjacent duplicate lines
    from an input file/stdin and prints the result to stdout.
    """

    def exec(self, args, input, output):
        pass


class Sort(Application):
    """
    Sorts the contents of a file/stdin line by line and prints the result to stdout.
    """

    def exec(self, args, input, output):
        pass


class ApplicationFactory:

    applications = {
        "pwd": Pwd,
        "cd": Cd,
        "ls": Ls,
        "cat": Cat,
        "echo": Echo,
        "head": Head,
        "tail": Tail,
        "grep": Grep,
        "cut": Cut,
        "find": Find,
        "uniq": Uniq,
        "sort": Sort,
    }

    def create(self, app_name) -> Application:
        unsafe = app_name[0] == "_"  # check for unsafe version
        app_name = app_name[1:] if unsafe else app_name
        app = self.applications[app_name]()
        if unsafe:
            return UnsafeWrapper(app)
        return app
