import unittest

class TestCheckNumber(unittest.TestCase):

    def test_is_even(self):
        self.assertEqual(check_number(2), "Es par")
		
def check_number(number):
    if number % 2 == 0:
        return "Es par"        

if __name__ == "__main__":
    unittest.main()
