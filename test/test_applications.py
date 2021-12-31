import os
import random
import unittest
from collections import deque
from tempfile import TemporaryDirectory, NamedTemporaryFile

from src.applications import ApplicationFactory

app_factory = ApplicationFactory()


def deque_to_str(dq: deque) -> str:
    s = ""
    while len(dq) > 0:
        s += dq.popleft()
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
        lines = ["line1\n", "line1\n", "LINE1\n", "line2\n", "Line2\n"]
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
        out = set(deque_to_str(out).strip().split())
        self.assertEqual(out, set(['line1', 'LINE1', 'line2', 'Line2']))

    def test_uniq_file_case_insensitive(self):
        args = ['-i', self.file1.name]  # ignores case
        inp = []
        out = deque()
        self.uniq.exec(inp, out, args)
        out = set(deque_to_str(out).strip().split())
        self.assertEqual(out, set(['line1', 'line2']))

    def test_uniq_stdin(self):
        args = []
        inp = "line1\nline1\nline2\nline2\n"
        out = deque()
        self.uniq.exec(inp, out, args)
        out = set(deque_to_str(out).strip().split())
        self.assertEqual(out, set(['line1', 'line2']))

    def test_uniq_stdin_with_flag(self):
        args = ['-i']
        inp = "line1\nLine1\nline2\nLINE2\n"
        out = deque()
        self.uniq.exec(inp, out, args)
        out = set(deque_to_str(out).strip().split())
        self.assertEqual(out, set(['line1', 'line2']))

    def test_uniq_file_invalid_flag(self):
        args = ['-b', self.file1.name]
        inp = []
        out = deque()
        with self.assertRaises(ValueError):
            self.uniq.exec(inp, out, args)

    def test_uniq_too_many_arguments(self):
        args = ['-i', '-i', '-i']
        inp = "line1\nLine1\nline2\nLINE2\n"
        out = deque()
        with self.assertRaises(ValueError):
            self.uniq.exec(inp, out, args)


class TestWc(unittest.TestCase):

    def setUp(self):
        self.wc = app_factory.create('wc')

    def test_wc_file_no_flag(self):
        file = NamedTemporaryFile("r+")
        file.write("Hello, this is COMP0010 Shell\n")
        file.seek(0)
        args = [file.name]
        inp = []
        out = deque()
        self.wc.exec(inp, out, args)
        file.close()
        out = deque_to_str(out).split()
        correct = ["1", "5", "30", file.name]
        self.assertEqual(out, correct)

    def test_wc_stdin_no_flag(self):
        inp = ["Hello, this is COMP0010 Shell\n"]
        args = []
        out = deque()
        self.wc.exec(inp, out, args)
        out = deque_to_str(out).split()
        correct = ["1", "5", "30", "stdin"]
        self.assertEqual(out, correct)

    def test_wc_stdin_with_flag(self):
        inp = ["Quick test\n"]
        args = ["-m"]
        out = deque()
        self.wc.exec(inp, out, args)
        out = deque_to_str(out).split()
        correct = ["11", "stdin"]
        self.assertEqual(out, correct)

    def test_wc_stdin_multiple_lines(self):
        inp = ["Line1\nLine2\nLine3\nLongestLine\n"]
        args = []
        out = deque()
        self.wc.exec(inp, out, args)
        out = deque_to_str(out).split()
        correct = ["4", "4", "30", "stdin"]
        self.assertEqual(out, correct)

    def test_wc_file_single_flag(self):
        file = NamedTemporaryFile("r+")
        file.write("LongestLine\nHello!\n")
        file.seek(0)
        args = ["-L", file.name]
        inp = []
        out = deque()
        self.wc.exec(inp, out, args)
        file.close()
        out = deque_to_str(out).split()
        correct = ["12", file.name]
        self.assertEqual(out, correct)

    def test_wc_file_invalid_flag(self):
        args = ["-r"]
        inp = ["Hello!\nLongestLine\n"]
        out = deque()
        with self.assertRaises(ValueError):
            self.wc.exec(inp, out, args)

    def test_wc_multiple_files(self):
        file1 = NamedTemporaryFile("r+")
        file1.write("This is file1.txt\n")
        file1.seek(0)
        file2 = NamedTemporaryFile("r+")
        file2.write("This is file2.txt\n")
        file2.seek(0)
        args = [file1.name, file2.name]
        inp = []
        out = deque()
        self.wc.exec(inp, out, args)
        print(out)
        out = deque_to_str(out).split("\n")
        res = []
        for el in out:
            res.extend(el.split())
        out = res
        correct = ['1', '3', '18', file1.name,
                   '1', '3', '18', file2.name,
                   '2', '6', '36', 'total']
        self.assertEqual(out, correct)


class TestCd(unittest.TestCase):
    def setUp(self):
        self.cd = app_factory.create("cd")
        self.dir = TemporaryDirectory(dir=os.getcwd())
        self.file1 = NamedTemporaryFile(mode="r", dir=self.dir.name)
        self.file2 = NamedTemporaryFile(mode="r", dir=self.dir.name)
        self.empty_dir = TemporaryDirectory(dir=os.getcwd())

    def tearDown(self):
        self.file2.close()
        self.file1.close()
        self.dir.cleanup()
        self.empty_dir.cleanup()

    def test_cd_no_args(self):
        with self.assertRaises(ValueError):
            args = []
            inp = []
            out = deque()
            self.cd.exec(inp, out, args)

    def test_cd_too_many_args(self):
        with self.assertRaises(ValueError):
            args = ["arg1", "arg2"]
            inp = []
            out = deque()
            self.cd.exec(inp, out, args)

    def test_cd_invalid_path(self):
        with self.assertRaises(FileNotFoundError):
            args = ["invalid_dir"]
            inp = []
            out = deque()
            self.cd.exec(inp, out, args)


class TestCat(unittest.TestCase):
    def setUp(self):
        self.cat = app_factory.create("cat")
        self.file1 = NamedTemporaryFile("r+", delete=False)
        self.file1.writelines([str(i) + "\n" for i in range(0, 100)])
        self.file1.close()
        self.file2 = NamedTemporaryFile("r+", delete=False)
        self.file2.writelines([str(i) + "\n" for i in range(100, 200)])
        self.file2.close()

    def tearDown(self):
        os.unlink(self.file1.name)
        os.unlink(self.file2.name)
        assert (not (os.path.exists(self.file1.name)) and
                not (os.path.exists(self.file2.name)))

    def test_cat_invalid_filename(self):
        output = deque()
        with self.assertRaises(FileNotFoundError):
            self.cat.exec(args=["invalid_filename"], inp=[], output=output)

    def test_cat_no_args(self):
        output = deque()
        self.cat.exec(args=[], inp=["input"], output=output)
        self.assertEqual(output, "input")

    def test_cat_single_arg(self):
        output = deque()
        fname = self.file1.name
        self.cat.exec(args=[fname], inp=[], output=output)
        self.assertEqual(output, [str(i) for i in range(0, 100)])

    def test_cat_multiple_args(self):
        output = deque()
        fname1 = self.file1.name
        fname2 = self.file2.name
        self.cat.exec(args=[fname1, fname2], inp=[], output=output)
        self.assertEqual(output, [str(i) for i in range(0, 200)])


if __name__ == "__main__":
    unittest.main()
