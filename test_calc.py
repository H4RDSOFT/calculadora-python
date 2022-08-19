import unittest
import calc

class TestCalc(unittest.TestCase):
    def teste_sum(self):
        #Areapare, Act
        
        result = calc.sum(num_1=5, num_2 = 10)
        #Assert
        self.assertEqual(result, 15)

    def teste_substraction(self):


        result = calc.substraction(num_1=30, num_2 = 10)

        self.assertEqual(result, 20)

    def teste_multiply(self):


        result = calc.multiply(num_1=2, num_2 = 4)

        self.assertEqual(result, 8)

    def teste_divide(self):


        result = calc.divide(num_1=6, num_2 = 2)

        self.assertEqual(result, 3)




    
