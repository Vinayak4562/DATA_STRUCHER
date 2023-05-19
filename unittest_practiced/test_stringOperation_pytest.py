import pytest
import stringOperations


@pytest.fixture
def before_method():
        print('------------------setUp is called before calling every testcases---------------')
        yield    
        print('----------------tearDown method will called after every testcases--------------')       
        

def test_firsttestcase(before_method):
    a= stringOperations.stringjoin('vin''ayak')
    assert a == 'vinayak'
    print('First test cases passed')

def test_second_testcase(before_method):
    a = stringOperations.uppercase(a= 'vinayak')
    assert a == 'VINAYAK'
    print('Second test cases passed')


def test_third_testcase(before_method):
    a = stringOperations.lowercase(b='VINAYAK')
    assert a == 'vinayak'
    print('Third test cases passed')

