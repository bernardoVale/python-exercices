import os
import subprocess
import unittest

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = "{}/grep.py".format(CURRENT_PATH)
FIXTURE_PATH = "{}/fixtures/01.log".format(CURRENT_PATH)

class TestGrep(unittest.TestCase):


    def test_grep_success_scenario(self):

        expected = "[    3.038498] systemd[1]: Set hostname to <docker-sa.avenuecode.com>.\n"
        got = subprocess.check_output([FILE_PATH, "Set hostname to", FIXTURE_PATH])

        self.assertEqual(got, expected)

    def test_fail_with_single_argument(self):
        rc = subprocess.call([FILE_PATH, "foo"])

        self.assertEqual(1, rc)

        # Test with zero arguments
        rc = subprocess.call([FILE_PATH])

        self.assertEqual(1, rc)

    def test_check_output_when_failed(self):
        should_get = "Two arguments are required, pattern and file path.\n"

        proc = subprocess.Popen([FILE_PATH, "foo"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        stdout = proc.communicate()[0]

        self.assertEqual(should_get, stdout)
        self.assertEqual(1, proc.returncode)

    def test_no_such_file_should_fail_with_message(self):
        should_get = "File foo.txt doesn't exists\n"

        proc = subprocess.Popen([FILE_PATH, "test", "foo.txt"],
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        stdout = proc.communicate()[0]

        self.assertEqual(should_get, stdout)
        self.assertEqual(1, proc.returncode)

    def test_should_return_nothing(self):
        expected = ""
        got = subprocess.check_output([FILE_PATH, ".askjdasbds,./ASDs.d", FIXTURE_PATH])

        self.assertEqual(expected, got)