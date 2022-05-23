import unittest

def is_he_older(years):
        if years >= 18:
            return False
        else:
            return False


class test_crystal(unittest.TestCase):
    
    def test_is_he_older(self):
        years = 20

        result = is_he_older(years)

        self.assertEqual(result, True)
    
    def test_is_he__menor(self):
        years = 12

        result = is_he_older(years)
        
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()