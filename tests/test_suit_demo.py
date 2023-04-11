import unittest
from tests.home.login_tests import LoginTests
from tests.courses.register_courses_tests import InvalidCardNumberTests

# Get all tests from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(InvalidCardNumberTests)

# Create a test suite combining all test classes
smoke_tests = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(smoke_tests)