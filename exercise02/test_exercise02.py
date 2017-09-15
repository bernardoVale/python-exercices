import os
import unittest
from exercise02 import grep


class TestExercise02(unittest.TestCase):


    def test_grep(self):

        cases = {
            'hostname_log': {
                'fixture': "01.log",
                'pattern': 'Set hostname to',
                'expected': [
                    "[    3.038498] systemd[1]: Set hostname to <docker-sa.avenuecode.com>."]
            },
            'systemd_logs': {
                'fixture': "01.log",
                'pattern': 'iscsi',
                'expected': ["[    3.490674] iscsi: registered transport (tcp)",
                             "[    3.547531] iscsi: registered transport (iser)"]
            },
            'error_logs': {
                'fixture': "01.log",
                'pattern': 'error',
                'expected': []
            },
        }

        for name, case in cases.iteritems():
            file_path = "{}/fixtures/{}".format(os.path.dirname
                                                (os.path.abspath(__file__)), case['fixture'])
            with open(file_path) as reader:
                content = ''.join(reader.readlines())
                got = grep(case['pattern'], content)
                self.assertEqual(case['expected'], got, msg="Failed case {}".format(name))

