import unittest
import program

class Test(unittest.TestCase)

    def test_lower(self):
        self.assertEqual(program.doLower("DzienDOBRY"), "dziendobry")

    def test_upper(self):
        self.assertEqual(program.doUpper("hello"), "HELLO")

    def test_replace(self):
        self.assertEqual(program.DoReplace("hello", "DzienDobry") "DzienDobry")

    def test_capitalize(self):
        self.assertEqual(program.DoCapitalize("hello"), "Hello")

    def tes_split(self):
        self.assertEqual(program.DoSplit("Dzien dobry"), "Dzien",g "dobry")


if __name__ == '__main__':
    unittest.main()
