import pytest
from selection_sort.selection_sort import sorting_selection

class TestSelectionSort(object):
    message="must be same type"
    
    def test_selectsort_norm(self):
        actual = sorting_selection([100,1000,1,10])
        expected = [1,10,100,1000]
        assert actual==expected,TestSelectionSort.message

    def test_selectsort_norm2(self):
        actual = sorting_selection([100,1000,1,10],asc=False)
        expected = [1000,100,10,1]
        assert actual==expected,TestSelectionSort.message

    def test_selectsort_norm3(self):
        actual = sorting_selection([-100,-1,0,-5])
        expected = [-100,-5,-1,0]
        assert actual==expected,TestSelectionSort.message

    def test_selectsort_norm4(self):
        actual = sorting_selection([-100,-1,0,-5],asc=False)
        expected = [0,-1,-5,-100]
        assert actual==expected,TestSelectionSort.message

    def test_selectsort_error(self):
        with pytest.raises(TypeError) as exp_info:
            actual = sorting_selection(["1","1","a","b",1],asc=False)
        assert exp_info
