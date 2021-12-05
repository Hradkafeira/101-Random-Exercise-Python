from quicksort.quicksort import quicksort

class TestQuickSort(object):
    message="must be sequence"

    def test_quicksort_norm1(self):
        actual=quicksort([5,6,10,3,2,5,1])
        expected=[1,2,3,5,5,6,10]
        assert actual==expected, TestQuickSort.message

    def test_quicksort_norm2(self):
        actual=quicksort([-5,-6,-10,-3,-2,-5,-1])
        expected=list(reversed([-1,-2,-3,-5,-5,-6,-10]))
        assert actual==expected, TestQuickSort.message

    def test_quicksort_norm3(self):
        actual=quicksort([5,6,10,3,2,5,1],asc=False)
        expected=list(reversed([1,2,3,5,5,6,10]))
        assert actual==expected, TestQuickSort.message

    def test_quicksort_norm4(self):
        actual=quicksort([-5,-6,-10,-3,-2,-5,-1],asc=False)
        expected=[-1,-2,-3,-5,-5,-6,-10]
        assert actual==expected, TestQuickSort.message


