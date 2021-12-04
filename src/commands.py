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

    def eval(self, input, output):
        pass
        # result = self.left.eval()
        # return self.right.eval(result)


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
        for command in iter(self.commands):
            command.eval()


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

    def eval(self, args, input, output):
        # DEBUGGING
        logging.debug(f"ARGS   IN EVAL: {args}")
        logging.debug(f"INPUT  IN EVAL: {input}")
        logging.debug(f"OUTPUT IN EVAL: {output}\n")
        # expanding filenames (globbing)
        for i in range(len(args)):
            if args[i][-1] == "*":
                files = glob.glob(args[i])
                args[i] = " ".join(files)
        # if multiple files specified for I/O
        if len(input) > 1 or len(output) > 1:
            raise ValueError("Multiple files specified for I/O")
        # open input file
        if input:
            if os.path.isfile(input):
                inFile = open(input, "r")
                inp = inFile.readlines()
                inFile.close()
            else:
                raise FileNotFoundError()
        # open output file
        if output:
            outFile = open(output, "w+")
            outFile.close()
        return self.app.exec(args, input, output)
