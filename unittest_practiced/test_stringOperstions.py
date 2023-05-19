import unittest
import stringOperations

class Test_stringOperations(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('********************** SETUP CLASS CALLED HERE********************')

    @classmethod
    def tearDownClass(cls):
        print('********************** TEARDOWN CLASS CALLED HERE********************')
        
    def setUp(self):        
        self.a = 'vin'
        self.b = 'ayak'
        self.c = 'VINAYAK'
        print('------------------setUp is called before calling every testcases---------------')

    def tearDown(self):
        del self.a 
        del self.b
        del self.c 
        print('----------------tearDown method will called after every testcases--------------')

    def test_firsttestcase(self):
        a= stringOperations.stringjoin(self.a, self.b)
        self.assertEqual(a, 'vinayak')
        print('First test cases passed')

    def test_second_testcase(self):
        a = stringOperations.uppercase(self.a)
        self.assertEqual(a, 'VIN')
        print('Second test cases passed')

    def test_third_testcase(self):
        a = stringOperations.lowercase(self.c)
        self.assertEqual(a, 'vinayak')
        print('Third test cases passed')


if __name__ == '__main__':
    unittest.main()