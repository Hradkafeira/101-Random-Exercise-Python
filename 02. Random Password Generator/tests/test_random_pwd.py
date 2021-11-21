import pytest
import re
from password_generator.random_pwd import pwd_generator

class TestPwdGenerator(object):

    actual = pwd_generator()
    expected=True
    message="should contain alphabet, number and character"

    def test_random_pwd(self):        
        is_valid=False
        pattern=r'[^a-zA-Z0-9\d]'
        if re.search(pattern, TestPwdGenerator.actual):
            is_valid=TestPwdGenerator.expected
        assert is_valid, TestPwdGenerator.message

    def test_random_pwd2(self):
        is_valid=False
        pattern=r'[^a-zA-Z0-9\d]'
        if re.search(pattern, TestPwdGenerator.actual):
            is_valid=TestPwdGenerator.expected
        assert is_valid, TestPwdGenerator.message
