import unittest

class TestCheckNumber(unittest.TestCase):

    def test_is_even(self):
        self.assertEqual(check_number(2), "Es par")
        self.assertNotEqual(check_number(3), "Es par")
        
    def test_is_divisible_by_3(self):
        self.assertEqual(check_number(3), "Es divisible por 3")
        self.assertNotEqual(check_number(2), "Es divisible por 3")
    
    def test_is_even_and_divisible_by_3(self):
        self.assertEqual(check_number(6), "Es par y divisible por 3")
        self.assertNotEqual(check_number(2), "Es par y divisible por 3")
        self.assertNotEqual(check_number(3), "Es par y divisible por 3")
		
def check_number(number):
    if number % 2 == 0 and number % 3 == 0:
        return "Es par y divisible por 3"
    elif number % 2 == 0:
        return "Es par"
    elif number % 3 == 0:
        return "Es divisible por 3"
    return "No es par ni divisible por 3"

if __name__ == "__main__":
    unittest.main(exit=False)
    
    # Solicitar entrada del usuario por consola
    number = int(input("Ingrese un número: "))
    result = check_number(number)
    print(result)
