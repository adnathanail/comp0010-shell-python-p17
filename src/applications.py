import os
import re
from typing import List
from abc import ABC, abstractmethod


class Application(ABC):  # pragma: no cover

    @abstractmethod
    def exec(self, args, input, output):
        pass


class UnsafeWrapper(Application):
    def __init__(self, app):
        self._app = app

    def exec(self, args, input, output):
        try:
            self._app.exec(args, input, output)
        except Exception as err:
            output.append(str(err))


class Pwd(Application):
    """Prints current working directory"""

    def exec(self, args, input, output):
        # no args, no input, there may be output
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
        if len(list_of_files) > 0:  # TODO: this line may not be needed
            output.append("\t".join(list_of_files))
        output.append("\n")  # is this needed?


class Cat(Application):
    """
    Concatenates the content of given files and prints it to stdout.
    """

    def exec(self, args, input, output):
        def read_content(filename):
            s = ""
            with open(filename, "r") as f:
                s += f.read()
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
    Prints its arguments separated by spaces and followed by a newline to
    stdout.
    """

    def exec(self, args, input, output):
        string = " ".join(args)
        string += "\n"
        output.append(string)


class HeadOrTail:
    DEFAULT_NUM_LINES = 10

    def exec(self, args, input, output, appObject):
        num_lines, file, use_stdin = self.validate_args(args)
        # take first n lines, else take last
        first = isinstance(appObject, Head)
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
        elif len(args) == 0:
            num_lines = self.DEFAULT_NUM_LINES
            use_stdin = True
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
        named_files_to_search = {}
        if len(args) > 1:
            for fn in args[1:]:
                named_files_to_search[fn] = ""
                with open(fn, "r") as f:
                    named_files_to_search[fn] += f.read()
        else:
            named_files_to_search["stdin"] = input

        for filename, file_contents in named_files_to_search.items():
            for row in file_contents.split("\n"):
                if args[0] in row or re.match(args[0], row):
                    if len(named_files_to_search) > 1:
                        output += filename + ":"
                    output += row + "\n"


class Cut(Application):
    """
    Cuts out sections from each line of a given file or stdin
    and prints the result to stdout.
    """

    def exec(self, args, input, output):
        if args[0] != "-b":
            raise ValueError("Please pass which bytes you would like with -b")
        range_strings = args[1].split(",")
        ranges = []
        for rs in range_strings:
            start_end = rs.split("-")
            rng = []
            if len(start_end) == 1:  # Just 1 index
                rng.append(int(start_end[0]))
            elif len(start_end) == 2:  # A slice, e.g. -3 or 4-6 or 7-
                if start_end[0] == '':
                    rng.append(start_end[0])
                else:
                    rng.append(int(start_end[0]))
                if start_end[1] == '':
                    rng.append(start_end[1])
                else:
                    rng.append(int(start_end[1]))
            ranges.append(rng)

        if len(args) > 2:
            string_to_cut = ""
            with open(args[2], "r") as f:
                string_to_cut += f.read()
        else:
            string_to_cut = input

        for row in string_to_cut.split("\n"):
            row_output = ['' for _ in range(len(row))]
            for rng in ranges:
                if len(rng) == 1:
                    if 1 <= rng[0] <= len(row):
                        row_output[rng[0] - 1] = row[rng[0] - 1]
                elif len(rng) == 2:
                    if rng[0] == '':
                        if 1 <= rng[1] <= len(row):
                            for i in range(rng[1]):
                                row_output[i] = row[i]
                    elif rng[1] == '':
                        if 1 <= rng[0] <= len(row):
                            for i in range(rng[0] - 1, len(row)):
                                row_output[i] = row[i]
                    else:
                        if 1 <= rng[0] <= len(row) \
                           and rng[0] <= rng[1] <= len(row):
                            for i in range(rng[0] - 1, rng[1]):
                                row_output[i] = row[i]
            output += "".join(row_output) + "\n"


class Find(Application):
    """
    Recursively searches for files with matching names.
    Outputs the list of relative paths, each followed by a newline.
    """

    def exec(self, args, input, output):
        if args[0] == "-name":
            directory_to_search = "."
            search_term = args[1]
        else:
            directory_to_search = args[0]
            search_term = args[2]
        for (dirpath, dirnames, filenames) in os.walk(directory_to_search):
            for fn in filenames:
                if fn == search_term or \
                   re.match(search_term.replace("*", ".*"), fn):
                    output += str(dirpath) + "/" + str(fn) + "\n"


class Uniq(Application):
    """
    Detects and deletes adjacent duplicate lines
    from an input file/stdin and prints the result to stdout.
    """

    def exec(self, args, input, output):
        ignore_case = False
        filename = ''
        if len(args) > 0 and args[0] == "-i":
            ignore_case = True
            if len(args) > 1:
                filename = args[1]
        else:
            if len(args) > 0:
                filename = args[0]
        if filename:
            string_to_uniq = ""
            with open(filename, "r") as f:
                string_to_uniq += f.read()
        else:
            string_to_uniq = input

        rows_to_search = string_to_uniq.split("\n")
        current_row = None
        for i in range(len(rows_to_search) - 1):
            if ignore_case:
                if current_row is not None and \
                   rows_to_search[i].lower() == current_row.lower():
                    continue
            else:
                if rows_to_search[i] == current_row:
                    continue
            output += rows_to_search[i] + "\n"
            current_row = rows_to_search[i]


class Sort(Application):
    """
    Sorts the contents of a file/stdin line by line and prints the result to
    stdout.
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


class WCCounter:
    def __init__(self, filenames: List[str]):
        # l-lines, w-words, c-bytes, m-chars, L-length of longest lines
        def calc_file_stats(filename):  # TODO: add Exceptions
            d = {"l": 0, "w": 0, "c": 0, "m": 0, "L": 0}
            with open(filename, 'r') as file:
                d["c"] = os.path.getsize(filename)
                for line in file:
                    d["l"] += 1
                    d["w"] += len(line.split())
                    d["m"] += len(line)
                    if len(line) > d["L"]:
                        d["L"] = len(line)
                return d

        self.filenames = filenames
        self.data = {"l": [], "w": [], "c": [], "m": [], "L": []}
        for filename in filenames:
            res = calc_file_stats(filename)
            for k, v in self.data.items():
                v.append(res[k])

    def _add_total_count(self):
        for v in self.data.values():
            total = str(sum(v))
            v.append(total)
        self.filenames.append("total")

    def _get_alignment(self):
        def calc_align(iterable):
            return max(map(lambda x: len(str(x)), iterable))
        align = dict()
        for k, v in self.data.items():
            align[k] = calc_align(v)
        return align

    def get_string_output(self, flag):
        output = ""
        if len(self.filenames) > 1:
            self._add_total_count()
        align = self._get_alignment()
        # iterate over each file and its stats
        for i in range(len(self.filenames)):
            s = ""
            if flag is None:
                lines = self.data["l"][i]  # num of lines
                w = self.data["w"][i]  # num of words
                c = self.data["m"][i]  # num of chars
                align_l = align["l"]
                align_w = align["w"]
                align_m = align["m"]
                s += f"{lines: >{align_l}} {w: >{align_w}} {c: >{align_m}}"
            elif flag in ["-c", "-l", "-m", "-w", "-L"]:
                key = flag[1:]
                s += f"{self.data[key][i]: >{align[key]}}"
            else:  # wrong flag
                raise ValueError(f"Invalid flag: {flag}")
            s += " " + self.filenames[i] + "\n"
            output += s
        return output


class Wc(Application):
    """
    Word prints specified statistics of a file
    or multiple files or stdin if no file is specified.
    """

    def exec(self, args, input, output):
        use_stdin = False
        flag = None
        if len(args) == 0:  # default counter + use stdin
            use_stdin = True
        elif len(args) == 1:  # flag + stdin OR default + file
            if args[0][0] == "-":
                flag = args[0]
                use_stdin = True
            else:  # default + file
                files = [args[0]]
        else:  # single flag + n files OR n files
            if args[0][0] == "-":
                flag = args[0]
                files = args[1:]
            else:
                files = args
        if use_stdin:  # if no files specified
            files = input.split()
        wccounter = WCCounter(filenames=files)
        res = wccounter.get_string_output(flag)
        output.append(res)


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
        "wc": Wc,
    }

    def create(self, app_name) -> Application:
        unsafe = app_name[0] == "_"  # check for unsafe version
        app_name = app_name[1:] if unsafe else app_name
        app = self.applications[app_name]()
        if unsafe:
            return UnsafeWrapper(app)
        return app
