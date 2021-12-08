from applications import ApplicationFactory
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
        result = self.left.eval()
        return self.right.eval(input=result)


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
        total_output = ""  # only used for cmd subs.
        # TODO: choose when and how to print the results
        for command in iter(self.commands):
            output = command.eval()
            if output:
                total_output += output
        return total_output


class Call(Command):
    def __init__(self, app_name, args, input, output):
        self.app = self.app_factory.create(app_name)
        self.args = args
        self.input = input
        self.output = output

    def __str__(self):
        return (
            f"{str(self.app).capitalize()}"
            f"(args={self.args},"
            f"input={self.input},"
            f"output={self.output})"
        )

    def eval(self, args=None, input=None, output=None):
        # DEBUGGING
        logging.debug(f"ARGS   IN EVAL: {self.args}")
        logging.debug(f"INPUT  IN EVAL: {self.input}")
        logging.debug(f"OUTPUT IN EVAL: {self.output}\n")
        # expanding filenames (globbing)
        # for i in range(len(self.args)):
        #     if self.args[i][-1] == "*":
        #         files = glob.glob(self.args[i])
        #         self.args[i] = " ".join(files)
        # if multiple files specified for I/O
        if len(self.input) > 1 or len(self.output) > 1:
            raise ValueError("Multiple files specified for I/O")
        # open input file
        # if self.input:
        #     if os.path.isfile(self.input):
        #         inFile = open(self.input, "r")
        #         inp = inFile.readlines()
        #         inFile.close()
        #     else:
        #         raise FileNotFoundError()
        # # open output file
        # if output:
        #     outFile = open(self.output, "w+")
        #     outFile.close()
        return self.app.exec(self.args, self.input, self.output)
