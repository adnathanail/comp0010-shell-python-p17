import os
import unittest
from collections import deque
from tempfile import NamedTemporaryFile

from src.applications import ApplicationFactory
from src.shell import run

app_factory = ApplicationFactory()


def deque_to_str(dq: deque) -> str:
    s = ""
    while len(dq) > 0:
        s += dq.popleft()
    return s


class TestShellOther(unittest.TestCase):

    def test_no_command(self):
        out = deque()
        run("", out)
        out = deque_to_str(out).strip()
        self.assertEqual("", out)

    def test_invalid_application(self):
        out = deque()
        with self.assertRaises(Exception):
            run("invalid_app arg_1", out)
        out = deque_to_str(out).strip()
        self.assertEqual("", out)


class TestQuoting(unittest.TestCase):

    def test_quoted_single(self):
        text = "\'this is a text in single quotes\'"
        out = deque()
        run(f'echo {text}', out)
        out = deque_to_str(out).strip()
        self.assertEqual(out, text[1:-1])

    def test_double_quoted_single(self):
        text = "\"this is a text in double quotes\""
        exp_text = "this is a text in double quotes"
        out = deque()
        run(f'echo {text}', out)
        out = deque_to_str(out).strip()
        self.assertEqual(out, exp_text)


class TestCmdSubstitution(unittest.TestCase):

    def test_cmd_substitution_in_double(self):
        text = "\"this is a `echo test` in `echo double quotes`\""
        exp_text = "this is a test in double quotes"
        out = deque()
        run(f'echo {text}', out)
        out = deque_to_str(out).strip()
        self.assertEqual(out, exp_text)

    def test_cmd_substitution_in_backquoted(self):
        cmd = "echo `echo test`"
        exp_out = "test"
        out = deque()
        run(cmd, out)
        out = deque_to_str(out).strip()
        self.assertEqual(out, exp_out)


class TestRedirection(unittest.TestCase):

    def test_redirection_output(self):
        text = 'testing redirection output'
        file1 = NamedTemporaryFile(mode="r+", dir=os.getcwd())
        run(f"echo {text} > {file1.name}")
        out = file1.readlines()[0].strip()
        self.assertEqual(out, text)
        file1.close()

    def test_multiple_redirections_output(self):
        with self.assertRaises(ValueError):
            run("echo hello > file1.txt > file2.txt > file3.txt")

    def test_multiple_redirections_input(self):
        with self.assertRaises(ValueError):
            run("cat < file1.txt < file2.txt < file3.txt")

    def test_redirection_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            run("cat < non_existing_file.txt")

    def test_redirection_input(self):
        text = "test"
        file = NamedTemporaryFile("r+", dir=os.getcwd())
        file.write(text)
        file.seek(0)
        out = deque()
        run(f"cat < {file.name}", output=out)
        out = deque_to_str(out).strip()
        self.assertEqual(out, text)
        file.close()

    def test_redirection_input_before_call(self):
        text = "test"
        file = NamedTemporaryFile("r+", dir=os.getcwd())
        file.write(text)
        file.seek(0)
        out = deque()
        run(f"< {file.name} cat", output=out)
        out = deque_to_str(out).strip()
        self.assertEqual(out, text)
        file.close()


class TestCommands(unittest.TestCase):

    def test_cmd_sequence(self):
        out = deque()
        run("echo 'text1'; echo text2", out)
        out = deque_to_str(out).strip().split()
        self.assertEqual(out, ['text1', 'text2'])

    def test_cmd_sequence_more_than_one(self):
        out = deque()
        run("echo 'text1'; echo text2; echo \"text3\"", out)
        out = deque_to_str(out).strip().split()
        self.assertEqual(out, ['text1', 'text2', 'text3'])

    def test_pipe(self):  # TODO: change
        cmdline = "echo abc | cut -b -1,2-"
        out = deque()
        run(cmdline, output=out)
        out = deque_to_str(out).strip()
        self.assertEqual(out, "abc")

    def test_pipe_more_than_one(self):
        cmdline = "echo abc | cut -b -1,2- | cut -b -1"
        out = deque()
        run(cmdline, output=out)
        out = deque_to_str(out).strip()
        self.assertEqual(out, "a")

    def test_cmd_sequence_with_pipe(self):  # TODO: change
        out = deque()
        run("echo 'text1'; echo abc | cut -b -1,2-", out)
        out = deque_to_str(out).strip().split()
        self.assertEqual(out, ['text1', 'abc'])


class TestGlobbing(unittest.TestCase):

    def test_globbing(self):
        file = NamedTemporaryFile('r+', dir=os.getcwd(), suffix='.unique')
        file.write('hello')
        file.seek(0)
        out = deque()
        run("cat *.unique", output=out)
        file.close()
        out = deque_to_str(out)
        self.assertEqual(out, 'hello')


class TestUnsafeAppVersion(unittest.TestCase):

    def test_unsafe_wrapper_single_call(self):
        out = deque()
        cwd = os.getcwd()
        path = "nonexistent_dir"
        run(f"_cd {path}", out)
        out = deque_to_str(out).strip()
        self.assertEqual(out, f"Could not find path '{path}'")
        self.assertEqual(cwd, os.getcwd())

    def test_cmd_sequence_with_unsafe_wrapper(self):
        out = deque()
        filename = "nonexistent_file"
        run(f"_cat {filename}; echo text2", out)
        out = deque_to_str(out).strip().split("\n")
        self.assertEqual(out, [f"Could not find file '{filename}'", "text2"])


if __name__ == "__main__":
    unittest.main()
