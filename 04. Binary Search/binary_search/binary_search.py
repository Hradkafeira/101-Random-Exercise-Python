
def binary_search(seq, number):
    """algorithm for searching number that started from middle seq
    and return the index of number. this sequence must be sorted first

    Parameters
    ----------
    seq : `list`
        sequence of number in list
    number : `int` or `float`
        number will be searched

    Returns
    -------

    index of  number:`int` or `None`
        return the index of number that searched
    """

    low=0
    high=len(seq)-1

    if seq != sorted(seq):
        raise ValueError("sequence must be sorted")
    else:
        while low <= high:
            mid=int((high+low)/2)
            guess=seq[mid]
            if guess < number:
                low = mid+1
            elif guess > number:
                high= mid-1
            elif guess == number:
                return mid
        return None
