def quicksort(arr,asc=True):
    if len(arr)<2:
        return arr
    else:
        pivot=arr[0]
        smaller=[el for el in arr[1:] if el <= pivot]
        bigger = [el for el in arr[1:] if el > pivot]
        if asc == True:
            return quicksort(smaller) + [pivot] + quicksort(bigger)
        else:
            return list(reversed(quicksort(smaller) + [pivot] + quicksort(bigger)))
