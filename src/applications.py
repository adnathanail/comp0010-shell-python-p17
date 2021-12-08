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


class Cd(Application):
    """changes current working directory"""

    def exec(self, args, input, output):
        path = args[0]
        cwd = os.getcwd()
        os.chdir(path)
        cwd_new = os.getcwd()
        logging.debug(f"Changed: {cwd} to {cwd_new}")


class Cat(Application):
    def exec(self, args, input, output):
        pass


class Pwd(Application):
    def exec(self, args, input, output):
        # no args, or input, there may be output
        cwd = os.getcwd() + "\n"
        if output:
            f = open(output[0], "w+")
            f.write(cwd)
        return cwd


class Ls(Application):
    def exec(self, args: List, input: List, output: List):
        """
        List the content of a directory print a list of files seperated by tabs and followed by \n
        Ignores files and directories whose name start with.

            Parameters:
                args (List): a list of string flags
                input (List): a list of string relative paths
            Returns:
                tab seperated list of string file and dir names
        TODO: Should it work only for zero or one arguments provided?
        """
        if not (input):  # just ls
            list_of_files = self._get_list_of_files()
            output.append("\t".join(list_of_files))
            # print("\t".join(list_of_files))
        else:
            for path in input:
                # print(f"{path}:")
                list_of_files = self._get_list_of_files(path)  # TODO: leave for now
                output.append("\t".join(list_of_files))
                # print("\t".join(list_of_files))

    def _get_list_of_files(self, path=os.getcwd()):
        return [fname for fname in os.listdir(path) if not (fname.startswith("."))]


class Echo(Application):
    def exec(self, args, input, output):
        logging.debug(f"Calling echo: {args} \nIn:{input}\nOut:{output}")
        return " ".join(args)


class Head(Application):
    def exec(self, args, input, output):
        pass


class Tail(Application):
    """Extracts the last n lines of the specified file"""

    DEFAULT_NUM_LINES = 10

    def exec(self, args, input, output: List):
        if len(args) == 3:
            pass

        if len(args) == 1:  # default
            file = args[-1]
            try:
                f = open(file, "r")
                content = f.readlines()[
                    -self.DEFAULT_NUM_LINES :
                ]  # grab last ten lines
                output.append(content)
            except FileNotFoundError:
                raise FileNotFoundError("Could not find the file")
        else:  # error
            raise ValueError(f"Wrong number of arguments: {len(args)}")


class Grep(Application):
    def exec(self, args, input, output):
        pass


class ApplicationFactory:

    applications = {
        "cd": Cd,
        "cat": Cat,
        "pwd": Pwd,
        "ls": Ls,
        "echo": Echo,
        "head": Head,
        "tail": Tail,
        "grep": Grep,
    }

    def create(self, app_name) -> Application:
        unsafe = app_name[0] == "_"  # check for unsafe version
        app_name = app_name[1:] if unsafe else app_name
        app = self.applications[app_name]()
        if unsafe:
            return UnsafeWrapper(app)
        return app
