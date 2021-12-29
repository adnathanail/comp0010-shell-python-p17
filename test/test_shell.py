import os
import random
import unittest
from collections import deque
from tempfile import TemporaryDirectory, NamedTemporaryFile

from src.applications import ApplicationFactory
from src.shell import run

app_factory = ApplicationFactory()


def deque_to_str(deque: deque):
    s = ""
    while len(deque) > 0:
        s += deque.popleft()
    return s


class TestPwd(unittest.TestCase):
    def setUp(self):
        self.pwd = app_factory.create("pwd")

    def test_pwd(self):
        args = []
        inp = []
        out = deque()
        self.pwd.exec(inp, out, args)
        out = deque_to_str(out).strip()
        self.assertEqual(out, os.getcwd())


class TestLs(unittest.TestCase):
    def setUp(self):
        self.ls = app_factory.create("ls")
        self.dir = TemporaryDirectory(dir=os.getcwd())
        self.file1 = NamedTemporaryFile(mode="r", dir=self.dir.name)
        self.file2 = NamedTemporaryFile(mode="r", dir=self.dir.name)
        self.empty_dir = TemporaryDirectory(dir=os.getcwd())

    def tearDown(self):
        self.file2.close()
        self.file1.close()
        self.dir.cleanup()
        self.empty_dir.cleanup()

    def test_ls_cwd(self):
        args = []
        inp = []
        out = deque()
        self.ls.exec(inp, out, args)
        out = deque_to_str(out).strip().split()
        correct = list(filter(lambda x: x[0] != ".", list(os.listdir("."))))
        self.assertEqual(out, correct)

    def test_ls_with_arg(self):
        args = [self.dir.name]
        inp = []
        out = deque()
        self.ls.exec(inp, out, args)
        out = sorted(deque_to_str(out).strip().split())
        filename1 = os.path.basename(str(self.file1.name))
        filename2 = os.path.basename(str(self.file2.name))
        correct = sorted([filename1, filename2])
        self.assertEqual(out, correct)

    def test_ls_no_files_found(self):
        args = [self.empty_dir.name]
        inp = []
        out = deque()
        self.ls.exec(inp, out, args)
        out = deque_to_str(out).strip().split()
        correct = []
        self.assertEqual(out, correct)

    def test_ls_with_invalid_arg(self):
        with self.assertRaises(FileNotFoundError):
            args = ["invalid_dir"]
            inp = []
            out = deque()
            self.ls.exec(inp, out, args)

    def test_ls_too_many_args(self):
        with self.assertRaises(ValueError):
            args = ["arg1", "arg2"]
            inp = []
            out = deque()
            self.ls.exec(inp, out, args)


class TestEcho(unittest.TestCase):
    def setUp(self):
        self.echo = app_factory.create("echo")

    def test_echo_no_args(self):
        args = []
        inp = []
        out = deque()
        self.echo.exec(inp, out, args)
        out = deque_to_str(out).strip()
        self.assertEqual(out, "")

    def test_echo_unquoted(self):
        args = ["hello"]
        inp = []
        out = deque()
        self.echo.exec(inp, out, args)
        out = deque_to_str(out).strip()
        self.assertEqual(out, "hello")

    def test_echo_unquoted_many(self):
        args = ["hello", "world, user!"]
        inp = []
        out = deque()
        self.echo.exec(inp, out, args)
        out = deque_to_str(out).strip()
        self.assertEqual(out, "hello world, user!")

    def test_echo_quoted_args(self):
        args = ["'hello'", "w'o'rld, u'se'r!"]
        inp = []
        out = deque()
        self.echo.exec(inp, out, args)
        out = deque_to_str(out).strip()
        self.assertEqual(out, "'hello' w'o'rld, u'se'r!")


class TestHeadAndTail(unittest.TestCase):
    def setUp(self):
        self.head = app_factory.create("head")
        self.tail = app_factory.create("tail")
        self.file1 = NamedTemporaryFile("r+", delete=False)
        self.file1.writelines([str(i) + "\n" for i in range(0, 100)])
        self.file1.close()

    def tearDown(self):
        os.unlink(self.file1.name)
        assert not (os.path.exists(self.file1.name))

    def test_head_tail_file(self):
        head_out = deque()
        tail_out = deque()
        fname = self.file1.name
        self.head.exec(args=[fname], inp=[], output=head_out)
        self.tail.exec(args=[fname], inp=[], output=tail_out)
        head_out = deque_to_str(head_out).split()
        tail_out = deque_to_str(tail_out).split()
        self.assertEqual(head_out, [str(i) for i in range(0, 10)])
        self.assertEqual(tail_out, [str(i) for i in range(90, 100)])

    def test_head_tail_file_flag_zero(self):
        head_out = deque()
        tail_out = deque()
        num = 0
        fname = self.file1.name
        self.head.exec(args=["-n", str(num), fname], inp=[], output=head_out)
        self.tail.exec(args=["-n", str(num), fname], inp=[], output=tail_out)
        head_out = deque_to_str(head_out).split()
        tail_out = deque_to_str(tail_out).split()
        self.assertEqual(head_out, [])
        self.assertEqual(tail_out, [])

    def test_head_tail_file_flag_nonzero(self):
        head_out = deque()
        tail_out = deque()
        num = random.randint(1, 99)
        fname = self.file1.name
        self.head.exec(args=["-n", str(num), fname], inp=[], output=head_out)
        self.tail.exec(args=["-n", str(num), fname], inp=[], output=tail_out)
        head_out = deque_to_str(head_out).split()
        tail_out = deque_to_str(tail_out).split()
        correct_1 = [str(i) for i in range(0, num)]
        correct_2 = [str(i) for i in range(100 - num, 100)]
        self.assertEqual(head_out, correct_1)
        self.assertEqual(tail_out, correct_2)

    def test_head_tail_file_not_found(self):
        non_existent_file = "hello"
        with self.assertRaises(FileNotFoundError):
            self.head.exec(args=[non_existent_file], inp=[], output=deque())
        with self.assertRaises(FileNotFoundError):
            self.tail.exec(args=[non_existent_file], inp=[], output=deque())

    def test_head_tail_take_more_than_exist(self):
        num = 101  # where len(file) = 100
        head_out = deque()
        tail_out = deque()
        args = ["-n", str(num), self.file1.name]
        self.head.exec(args=args, inp=[], output=head_out)
        self.tail.exec(args=args, inp=[], output=tail_out)
        head_out = deque_to_str(head_out).split()
        tail_out = deque_to_str(tail_out).split()
        self.assertEqual(head_out, [str(i) for i in range(0, 100)])
        self.assertEqual(tail_out, [str(i) for i in range(0, 100)])

    def test_head_tail_only_flag_stdin(self):
        stdin = "\n".join([str(i) for i in range(0, 100)])
        num = random.randint(1, 99)
        head_out = deque()
        tail_out = deque()
        args = ["-n", str(num)]
        self.head.exec(args=args, inp=stdin, output=head_out)
        self.tail.exec(args=args, inp=stdin, output=tail_out)
        head_out = deque_to_str(head_out).strip().split()
        tail_out = deque_to_str(tail_out).strip().split()
        correct_1 = [str(i) for i in range(0, num)]
        correct_2 = [str(i) for i in range(100 - num, 100)]
        self.assertEqual(head_out, correct_1)
        self.assertEqual(tail_out, correct_2)

    def test_head_tail_wrong_args(self):
        with self.assertRaises(ValueError):  # wrong flag
            args = ["-c", "10", self.file1.name]
            self.tail.exec(args=args, inp=[], output=deque())
        with self.assertRaises(ValueError):  # wrong flag
            args = ["-c", "10"]
            self.tail.exec(args=args, inp=[], output=deque())
        with self.assertRaises(ValueError):  # more than 3 args
            args = ["-n", "10", self.file1.name, "arg4"]
            self.tail.exec(args=args, inp=[], output=deque())

    def test_head_tail_no_args(self):
        stdin = "\n".join([str(i) for i in range(0, 100)])
        head_output = deque()
        tail_output = deque()
        self.head.exec(args=[], inp=stdin, output=head_output)
        self.tail.exec(args=[], inp=stdin, output=tail_output)
        head_output = deque_to_str(head_output).strip().split()
        tail_output = deque_to_str(tail_output).strip().split()
        self.assertEqual(head_output, [str(i) for i in range(0, 10)])
        self.assertEqual(tail_output, [str(i) for i in range(90, 100)])


class TestCut(unittest.TestCase):

    def setUp(self):
        self.cut = app_factory.create('cut')
        self.file1 = NamedTemporaryFile(mode="r+")  # deleted dir
        self.file1.write("123456789\n123456789\n123456789")
        self.file1.seek(0)

    def tearDown(self):
        self.file1.close()

    def test_cut_no_flag(self):
        with self.assertRaises(ValueError):
            args = [self.file1.name]
            inp = []
            out = deque()
            self.cut.exec(inp, out, args)

    def test_cut_single_byte_with_stdin(self):
        args = ['-b', '1']
        inp = "Hello!"
        out = deque()
        self.cut.exec(inp, out, args)
        out = deque_to_str(out).strip()
        self.assertEqual(out, 'H')

    def test_cut_single_byte(self):
        fname = self.file1.name
        args = ['-b', '1', fname]
        inp = []
        out = deque()
        self.cut.exec(inp, out, args)
        out = deque_to_str(out).split()
        self.assertEqual(out, ["1", "1", "1"])

    def test_cut_single_range(self):
        fname = self.file1.name
        args = ['-b', '4-7', fname]
        inp = []
        out = deque()
        self.cut.exec(inp, out, args)
        out = deque_to_str(out).split()
        self.assertEqual(out, ["4567", "4567", "4567"])

    def test_cut_one_endpoint_range(self):
        fname = self.file1.name
        args = ['-b', '-6', fname]
        inp = []
        out = deque()
        self.cut.exec(inp, out, args)
        out = deque_to_str(out).split()
        self.assertEqual(out, ["123456", "123456", "123456"])

    def test_cut_one_startpoint_range(self):
        fname = self.file1.name
        args = ['-b', '8-', fname]
        inp = []
        out = deque()
        self.cut.exec(inp, out, args)
        out = deque_to_str(out).split()
        self.assertEqual(out, ["89", "89", "89"])

    def test_cut_multiple_range(self):
        fname = self.file1.name
        args = ['-b', '-3,5-6,9-', fname]
        inp = []
        out = deque()
        self.cut.exec(inp, out, args)
        out = deque_to_str(out).split()
        exp_res = ["123569", "123569", "123569"]
        self.assertEqual(out, exp_res)


class TestUniq(unittest.TestCase):

    def setUp(self):
        self.uniq = app_factory.create('uniq')
        self.file1 = NamedTemporaryFile(mode='r+', dir=os.getcwd())
        lines = ["line1\n", "line1\n", "line2\n", "line2\n", "Line1\n"]
        self.file1.writelines(lines)
        self.file1.seek(0)

    # def test_uniq_invalid_option(self):
    #     args = ["-b", self.file1.name]
    #     inp = ["line1", "line1", "line2", "line2"]
    #     out = deque()
    #     # Raises FileNotFoundError
    #     with self.assertRaises(ValueError, msg="Should raise ValueError"):
    #         self.uniq.exec(inp, out, args)

    def test_uniq_invalid_file(self):
        args = ["nofile.txt"]
        inp = []
        out = deque()
        with self.assertRaises(FileNotFoundError):
            self.uniq.exec(inp, out, args)

    def test_uniq_file_case_sensitive(self):
        args = [self.file1.name]
        inp = []
        out = deque()
        self.uniq.exec(inp, out, args)
        out = deque_to_str(out).strip().split()
        self.assertEqual(out, ['line1', 'line2', 'Line1'])

    # def test_uniq_file_case_insensitive(self):
    #     args = ['-i', self.file1.name]  # ignores case
    #     inp = []
    #     out = deque()
    #     self.uniq.exec(inp, out, args)
    #     out = deque_to_str(out).strip().split()
    #     self.assertEqual(out, ['line1', 'line2'])


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


# class TestGlobbing(unittest.TestCase):
#
#     def test_globbing(self):
#         file = NamedTemporaryFile('r+')
#         file.write('hello')
#         file.seek(0)
#         out = deque()
#         run(f"cat *{file.name[-3:]}", output=out)
#         file.close()
#         out = deque_to_str(out)
#         self.assertEqual(out, 'hello')
#
#
# class TestUnsafeAppVersion(unittest.TestCase):
#
#     def test_unsafe_wrapper_single_call(self):
#         out = deque()
#         cwd = os.getcwd()
#         run("_cd nonexistent_dir", out)
#         self.assertEqual(cwd, os.getcwd())
#         self.assertEqual(out, "TBD")  # TODO: add error raise in app
#
#     def test_cmd_sequence_with_unsafe_wrapper(self):
#         out = deque()
#         run("_cat nonexistent_file; echo text2", out)
#         out = deque_to_str(out).strip().split()
#         out = deque_to_str(out)
#         self.assertEqual(out, "TBD")  # TODO: add error raise in app


if __name__ == "__main__":
    unittest.main()
