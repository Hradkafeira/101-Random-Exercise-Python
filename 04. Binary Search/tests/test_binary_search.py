import pytest
from binary_search.binary_search import binary_search

class TestBinarySeach(object):
    message="sequence must be sorted"
    def test_binary_search_norm(self):
        actual = binary_search([0,2,4,6,8,10],6)
        expected = 3
        assert actual == expected,TestBinarySeach.message

    def test_binary_search_norm2(self):
        actual = binary_search([1.5,2.5,3.5,4.5,6.0,7],6.0)
        expected = 4
        assert actual == expected,TestBinarySeach.message

    def test_binary_search_error(self):
        seq=[10,0,4,8,6,2]
        with pytest.raises(ValueError) as exc_info:
            actual = binary_search(seq,2)
            expected = 5            
        assert exc_info.match("sequence must be sorted")
        