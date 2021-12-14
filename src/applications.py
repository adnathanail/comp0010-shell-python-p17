from io import DEFAULT_BUFFER_SIZE
import os
from sys import argv
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
        output.append(cwd)


class Cd(Application):
    """Changes current working directory"""

    def exec(self, args, input, output):
        path = args[0]
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
            output.append("\t".join(list_of_files))
        output.append("")  # is this needed?


class Cat(Application):
    """
    Concatenates the content of given files and prints it to stdout.
    """

    def exec(self, args, input, output):
        def read_content(filename):
            s = ""
            try:
                with open(filename, "r") as f:
                    s += f.read()
            except FileNotFoundError:
                raise FileNotFoundError("The file has not been found")
            return s

        if args:
            file_list = args
            content = ""
            for file in file_list:
                content += read_content(file)
            output.append(content)
        else:
            output.append(input)


class Echo(Application):
    """
    Prints its arguments separated by spaces and followed by a newline to stdout.
    """

    def exec(self, args, input, output):
        string = " ".join(args)
        string += "\n"
        output.append(string)


class HeadOrTail:
    DEFAULT_NUM_LINES = 10

    def exec(self, args, input, output, appObject):
        num_lines, file, use_stdin = self.validate_args(args)
        first = isinstance(appObject, Head)  # take first n lines, else take last
        if use_stdin:
            content = input.splitlines(keepends=True)
            content = self.grab_lines(content, num_lines, first)
        else:
            try:
                with open(file, "r") as f:
                    content = f.readlines()
                    content = self.grab_lines(content, num_lines, first)
            except FileNotFoundError:
                raise FileNotFoundError("Could not find the file")
        content = "".join(content)
        output.append(content)

    def validate_args(self, args):
        num_lines, file, use_stdin = None, None, None
        if len(args) == 3:  # OPTIONS & FILE specified
            if args[0] != "-n":
                raise ValueError("wrong flags")
            else:
                num_lines = int(args[1])
                file = args[2]
        elif len(args) == 2:  # OPTIONS specified, use stdin
            if args[0] != "-n":
                raise ValueError("wrong flags")
            else:
                num_lines = int(args[1])
                use_stdin = True
        elif len(args) == 1:  # FILE specified
            num_lines = self.DEFAULT_NUM_LINES
            file = args[0]
        else:
            raise ValueError("wrong number of command line arguments")
        return (num_lines, file, use_stdin)

    @staticmethod
    def grab_lines(content, n, first):
        if n == 0:
            return [""]
        if len(content) < n:
            return content
        elif first:
            return content[:n]
        else:
            return content[-n:]


class Head(Application):
    """
    Prints the first N lines of a given file or stdin.
    If there are less than N lines, prints only the existing lines
    without raising an exception.
    """

    def exec(self, args, input, output):
        HeadOrTail().exec(args, input, output, appObject=self)


class Tail(Application):
    """
    Prints the last N lines of a given file or stdin.
    If there are less than N lines, prints only the existing lines
    without raising an exception.
    """

    def exec(self, args, input, output):
        HeadOrTail().exec(args, input, output, appObject=self)


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
        use_stdin = False
        reverse = False
        if len(args) == 0:
            use_stdin = True
        elif len(args) == 1:
            if args[0] == "-r":
                reverse = True
                use_stdin = True
            else:
                file = args[0]
        elif len(args) == 2:
            option = args[0]
            if option != "-r":
                raise ValueError("wrong flags")
            else:
                reverse = True
            file = args[1]
        try:
            content = []
            if use_stdin:
                if input is not None:
                    content = input.split()
                    content.sort(reverse=reverse)
                    content = "\n".join(content)
                    content += "\n"
                else:
                    raise ValueError("No input to a call")
            else:
                with open(file, "r") as f:
                    content = f.readlines()
                    content.sort(reverse=reverse)
                    content = "".join(content)
            output.append(content)
        except FileNotFoundError:
            raise FileNotFoundError("File was not found")


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
