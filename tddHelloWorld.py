import unittest
import mojprogram2

class TestHelloWorld(unittest.TestCase):

    def test_zwroc_parametr(self):
        self.assertEqual(mojprogram2.zwroc_parametr(), "HelloWorld")

if __name__ == '__main__':
    unittest.main()
