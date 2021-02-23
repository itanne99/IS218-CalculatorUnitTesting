
# Move Imports to fileReader.py ^^
import unittest

# the .py file name is Calculator and the class name is also Calculator

# Move Section to fileReader.py
from src.calculator import Calculator

from tests.src.fileReader import FileReader

'''
This is the TestCase class that test Calculator class functions.
'''

class TestCalculator(unittest.TestCase):
    # this is the Calculator class instance.
    calculator = None

    # class level setup function, execute once only before any test function.
    @classmethod
    def setUpClass(cls):
        print('')
        print('setUpClass')

    # class level setup function, execute once only after all test function's execution.
    @classmethod
    def tearDownClass(cls):
        print('')
        print('tearDownClass')

    # execute before every test case function run.
    def setUp(self):
        self.calculator = Calculator()
        self.fileReader = FileReader()
        print('')
        print('setUp')

    # execute after every test case function run.
    def tearDown(self):
        # release the Calculator object.
        if self.calculator is not None:
            self.calculator = None
        self.fileReader.closeFile()
        print('')
        print('tearDown')

    # below are function that test Calculator class's plus, minus, multiple and divide functions.
    def test_addition(self):
        print('')
        print('******test_addition******')
        # get each row text from the csv file.
        for row in self.fileReader.openFile("testCases/Unit_Test_Addition.csv"):
            # the first column in the text line is x value.
            x = row[0]
            # the second column in the text line is y value.
            y = row[1]
            # the third column in the text line is (x + y) value.
            expect_result = row[2]
            result = self.calculator.sum(x, y)

            print(str(x) + ' + ' + str(y) + ' = ' + str(result) + ', expect ' + str(expect_result))
            self.assertEqual(float(result), float(expect_result))

    def test_subtraction(self):
        print('')
        print('******test_subtraction******')
        for row in self.fileReader.openFile("testCases/Unit_Test_Subtraction.csv"):
            x = row[0]
            y = row[1]
            expect_result = row[2]
            result = self.calculator.subtract(x, y)

            print(str(x) + ' - ' + str(y) + ' = ' + str(result) + ', expect ' + str(expect_result))
            self.assertAlmostEqual(float(result), float(expect_result))

    def test_multiplication(self):
        print('')
        print('******test_multiplication******')
        for row in self.fileReader.openFile("testCases/Unit_Test_Multiplication.csv"):
            x = row[0]
            y = row[1]
            # the fifth column in the text line is (x * y) value.
            expect_result = row[2]
            result = self.calculator.multiply(x, y)

            print(str(x) + ' * ' + str(y) + ' = ' + str(result) + ', expect ' + str(expect_result))
            self.assertEqual(float(result), float(expect_result))

    def test_division(self):
        print('')
        print('******test_division******')
        for row in self.fileReader.openFile("testCases/Unit_Test_Division.csv"):
            x = row[0]
            y = row[1]
            # the sixth column in the text line is (x / y) value.
            expect_result = row[2]
            result = self.calculator.divide(x, y)

            print(str(x) + ' / ' + str(y) + ' = ' + str(result) + ', expect ' + str(expect_result))
            if isinstance(result, float):
                self.assertAlmostEqual(result, float(expect_result))
            else:
                self.assertEqual(result, expect_result)


    def test_squareRoot(self):
        print('')
        print('******test_squareRoot******')
        for row in self.fileReader.openFile("testCases/Unit_Test_Square_Root.csv"):
            x = row[0]
            expect_result = row[1]
            result = self.calculator.root(x, 2)

            print(' √ ' + str(x) + ' = ' + str(result) + ', expect ' + str(expect_result))
            self.assertEqual(float(result), float(expect_result))

    def test_squared(self):
        print('')
        print('******test_squared******')
        for row in self.fileReader.openFile("testCases/Unit_Test_Square.csv"):
            x = row[0]
            # the sixth column in the text line is (x / y) value.
            expect_result = row[1]
            result = self.calculator.power(x, 2)

            print(str(x) + '² ' + ' = ' + str(result) + ', expect ' + str(expect_result))
            self.assertEqual(float(result), float(expect_result))


if __name__ == '__main__':
    unittest.main()


def build_test_suite():
    # create unittest.TestSuite object.
    test_suite = unittest.TestSuite()
    # add each test function to the test suite object.
    test_suite.addTest(TestCalculator('test_addition'))
    test_suite.addTest(TestCalculator('test_subtraction'))
    test_suite.addTest(TestCalculator('test_multiplication'))
    test_suite.addTest(TestCalculator('test_division'))
    test_suite.addTest(TestCalculator('test_squareRoot'))
    test_suite.addTest(TestCalculator('test_squared'))
    return test_suite
