from applications import ApplicationFactory


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
        if self.left and self.right:
            return f"Pipe({self.left}, {self.right})"
        else:
            return "Pipe"

    def eval(self, input, output):
        pass


class Seq(Command):
    # reference to commands

    def __init__(self, seq=[]):
        self.commands = seq

    def __str__(self):
        if self.commands:
            return f"Seq({str(self.commands)}"
        else:
            return "Seq"

    def addCommand(self, command):
        self.commands.append(command)

    def eval(self, input, output):
        # use iterator for command execution
        pass


class Call(Command):
    def __init__(self, app_name):
        self.app = self.app_factory.create(app_name)

    def __str__(self):
        if self.app:
            return f"Call({self.app})"
        else:
            return "Call"

    def eval(self, input, output):
        pass
