import unittest
import math as math

class testes(unittest.TestCase):
    def testar_soma(self):
            self.assertEqual(3, math.S(1, 2))
            self.assertEqual(8, math.S(6, 2))
            self.assertEqual(7, math.S(5, 2))
    def testar_subtrair(self):
            self.assertEqual(3, math.Sub(5, 2))
            self.assertEqual(6, math.Sub(8, 2))
            self.assertEqual(7, math.Sub(9, 2))
    def testar_multiplicar(self):
            self.assertEqual(6, math.M(2, 3))
            self.assertEqual(0, math.M(2, 0))
            self.assertEqual(8, math.M(2, 4))
    def testar_dividir(self):
            self.assertEqual(2, math.D(2, 1))
            self.assertEqual(6, math.D(12, 2))
            self.assertEqual(12, math.D(144, 12))
unittest.main(argv=[""], exit= False)
