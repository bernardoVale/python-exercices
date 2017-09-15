import unittest
from exercise01 import check_linux_version

class TestExercise01(unittest.TestCase):

    def test_check_linux_version(self):

        cases = {
            'el5_case': {
                'kernel_info': "Linux ecmagentqark1v 2.6.18-419.el5 #1 SMP Wed Feb 22 22:40:57 "
                               "EST 2017 x86_64 x86_64 x86_64 GNU/Linux",
                'expected': 'el5'
            },
            'el6_case': {
                'kernel_info': "Linux mg-intdev1-rk1 2.6.32-642.15.1.el6.x86_64 #1 SMP Fri Feb 24 "
                      "14:31:22 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux",
                'expected': 'el6'
            },
            'el7_case': {
                'kernel_info': "Linux localhost.localdomain 4.10.1-1.el7.elrepo.x86_64 #1 SMP Sun "
                    "Feb 26 19:47:48 EST 2017 x86_64 x86_64 x86_64 GNU/Linux",
                'expected': 'el7'
            },
            'unknown_version': {
                'kernel_info': "Linux 4c426268476d 4.9.13-moby #1 SMP "
                               "Sat Mar 25 02:48:44 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux",
                'expected': 'unknown_version'
            }
        }

        for name, case in cases.iteritems():
            got = check_linux_version(case['kernel_info'])
            self.assertEqual(case['expected'], got, msg="Failed case {}".format(name))
