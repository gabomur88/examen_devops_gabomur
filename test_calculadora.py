import unittest
from calculadora import sumar, restar, multiplicar, dividir


class TestCalculadora(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(sumar(2, 3), 5)

    def test_restar(self):
        self.assertEqual(restar(10, 4), 6)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(3, 4), 12)

    def test_dividir(self):
        self.assertEqual(dividir(10, 2), 5)

    def test_division_por_cero(self):
        with self.assertRaises(ValueError):
            dividir(10, 0)


if __name__ == "__main__":
    unittest.main()