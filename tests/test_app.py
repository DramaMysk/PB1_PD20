import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import pytest
from app import check_age

def test_valid_age():
    rezultats = check_age("18")
    assert rezultats == 18

def test_strip_age():
    rezultats = check_age(" 19  ")
    assert rezultats == 19

def test_invalid_age():
    with pytest.raises(ValueError):
        check_age("abc")
    