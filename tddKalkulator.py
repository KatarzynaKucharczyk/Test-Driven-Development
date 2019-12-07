import unittest
import kalkulator

class TestKalkulator(unittest.TestCase):

    def test_kalkulator_dodaj(self):
        self.assertEqual(kalkulator.dodaj(),6)

    def test_kalkulator_odemij(self):
        self.assertEqual(kalkulator.odejmij(),0)

    def test_kalkulator_pomnoz(self):
        self.assertEqual(kalkulator.pomnoz(),9)

    def test_kalkulator_podziel(self):
        self.assertEqual(kalkulator.podziel(),1)


if __name__ == '__main__':
    unittest.main()
