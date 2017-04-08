#10273765
#B8IT105 Assignment 1
#testsuite for 10 Function Calculators

from calculator import *
    
import unittest

class MyTest(unittest.TestCase):
    
#test to see 2+2=4,5+3=8,4+0=4    
    def testadd1(self):
        self.assertEqual(add(2,2), 4)
    def testadd2(self):    
        self.assertEqual(add(5,3), 8)
    def testadd3(self):
        self.assertEqual(add(4,0), 4)

#test for other calculators 
    def testSubtract(self):
        self.assertEqual(subtract(2,2), 0)   
        self.assertEqual(subtract(5,3), 2)
        self.assertEqual(subtract(4,0), 4)
        
    def testMultiply(self):
        self.assertEqual(multiply(2,2), 4)   
        self.assertEqual(multiply(5,3), 15)
        self.assertEqual(multiply(4,0), 0)

    def testDivide(self):
        self.assertEqual(divide(2,2), 1)   
        self.assertEqual(divide(6,6), 1)
        self.assertEqual(divide(4,1), 4)
        self.assertEqual(divide(4,0), 'Invalid')
        
    def testExponent(self):
        self.assertEqual(exponent(2,2), 4)   
        self.assertEqual(exponent(5,3), 125)
        self.assertEqual(exponent(4,0), 1)
        
    def testSquare(self):
        self.assertEqual(square(2), 4)   
        self.assertEqual(square(3), 9)
        self.assertEqual(square(4), 16)

    def testCube(self):
        self.assertEqual(cube(2), 8)   
        self.assertEqual(cube(3), 27)
        self.assertEqual(cube(4), 64)
    
    def testSqrt(self):
        self.assertEqual(sqrt(4), 2)   
        self.assertEqual(sqrt(9), 3)
        self.assertEqual(sqrt(16), 4)
        self.assertEqual(sqrt(0), 'Invalid')
        
    def testSinh(self):
        self.assertEqual(sinh(1), 1.18)   
        self.assertEqual(sinh(9), 4051.54)
        self.assertEqual(sinh(10), 11013.23)
     
    def testLog10(self):
        self.assertEqual(log10(100), 2)   
        self.assertEqual(log10(1000), 3)
        self.assertEqual(log10(1), 0)
        
if __name__ == '__main__':
    unittest.main()
    
