import unittest
import tests_12_3

rtt = unittest.TestSuite()
rtt.addTest((unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest)))
rtt.addTest((unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest)))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(rtt)
