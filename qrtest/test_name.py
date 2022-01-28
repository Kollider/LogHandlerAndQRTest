import pytest
from scanner_handler import *

db_test = ['blabl', 'bla', 'asd', 'qwer'] #imitation of the database


@pytest.fixture
def example_qr_codes():
    return ['bla', 'blabl', 'blablab', 'blabla', 'blablablabla', 'qwer', 'blaslab'] #examples of the qr codes
#There was a need to avoid the ConnectionError, as it was not possible to connect to database
def some_test_func(self, second):
    if second in db_test:
        return True
    elif second not in db_test:
        return None

CheckQr.check_in_db = some_test_func
a = CheckQr()


def test_check_len_color_3_letters(example_qr_codes):
    a.check_scanned_device(example_qr_codes[0])
    assert a.color == 'Red'


def test_check_len_color_5_letters(example_qr_codes):
    a.check_scanned_device(example_qr_codes[1])
    assert a.color == 'Green'


def test_check_len_color_7_letters(example_qr_codes):
    a.check_scanned_device(example_qr_codes[2])
    assert a.color == 'Fuzzy Wuzzy'


def test_check_len_color_4_letters(example_qr_codes):
    a.check_scanned_device(example_qr_codes[5])
    assert a.color not in ('Fuzzy Wuzzy', 'Green', 'Red')


def test_check_not_in_db(example_qr_codes):
    assert a.check_in_db(example_qr_codes[6])

def test_can_add_device(example_qr_codes):
    a.check_scanned_device(example_qr_codes[0])
