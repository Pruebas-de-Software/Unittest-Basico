import unittest

class TestCheckNumber(unittest.TestCase):

    def test_is_even(self):
        self.assertEqual(check_number(2), "Es par")
        self.assertEqual(check_number(3), "No es par")
		
def check_number(number):
    if number % 2 == 0:
        return "Es par"
    return "No es par"

if __name__ == "__main__":
    unittest.main()
