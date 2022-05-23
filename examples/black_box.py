import unittest
#pruebas de caja negras se envian inputs y se veia el output
def suma(num_1, num_2):
    """Defino 
    num_1 as int
    num_2 as int
    return num_1 + num_"
    """
    return abs(num_1)+ num_2

class Black_box(unittest.TestCase):
    
    def test_two_numbers_positive(self):
        """ Test de prueba positivo
        """
        num_1 = 10
        num_2 = 5

        result = suma(num_1, num_2)
        self.assertEqual(result, 15)
    
    def test_two_numerbs_negative(self):
        """Test de prueba negativo
        """
        num_1 = -10
        num_2 = -15

        result = suma(num_1, num_2)
        self.assertEqual(result, -25)

if __name__ == '__main__':
    unittest.main()
