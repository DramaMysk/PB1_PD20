import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import pytest
from app import check_age
from app import check_name

def test_valid_age():
    rezultats = check_age("18")
    assert rezultats == 18

def test_strip_age():
    rezultats = check_age(" 19  ")
    assert rezultats == 19

def test_invalid_age():
    with pytest.raises(ValueError):
        check_age("abc")
    

def test_valid_name():
    rezultats = check_name("Bob")
    assert rezultats == "Bob"

def test_strip_name():
    rezultats = check_name("  Bob   ")
    assert rezultats == "Bob"

def test_invalid_name():
    with pytest.raises(ValueError):
        check_name("123")