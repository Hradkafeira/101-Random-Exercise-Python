import pytest
import re
from password_generator.random_pwd import pwd_generator

class TestPwdGenerator(object):
    def test_random_pwd(self):
        pattern=r'[^a-zA-Z0-9\d]'
        is_valid=False
        if re.search(pattern, pwd_generator()):
            is_valid=True
        assert is_valid

    def test_random_pwd2(self):
        pattern=r'[^0-9a-zA-Z\d]'
        is_valid=False
        if re.search(pattern, pwd_generator()):
            is_valid=True
        assert is_valid
