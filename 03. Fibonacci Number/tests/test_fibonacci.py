import pytest
from fibonacci_number import FibonnaciCollection

fc=FibonnaciCollection()

class TestFibonnaciCollection(object):

    message = "Must be positive number"

    def test_fibonnaci_normal(self):
        actual = fc.fibonnaci(10)
        expected = 55
        assert actual == expected, TestFibonnaciCollection.message 

    def test_fibonnaci_normal2(self):
        actual = fc.fibonnaci(100)
        expected = 354224848179261915075
        assert actual == expected, TestFibonnaciCollection.message 

    def test_fibonnaci_error(self):
        with pytest.raises(AssertionError) as exc_info:
            actual = fc.fibonnaci(-100)
        assert exc_info

    def test_seq_fib_norm(self):
        actual = fc.seq_fibonnaci(10)[-1]
        expected = 55
        assert actual == expected, TestFibonnaciCollection.message

    def test_seq_fib_norm2(self):
        actual = fc.seq_fibonnaci(100)[-1]
        expected = 354224848179261915075
        assert actual == expected, TestFibonnaciCollection.message

    def test_seq_fib_error(self):
        with pytest.raises(AssertionError) as exc_info:
            actual = fc.seq_fibonnaci(-10)
        assert exc_info