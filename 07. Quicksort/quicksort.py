def quicksort(arr):
    if len(arr)<2:
        return arr
    else:
        pivot=arr[0]
        smaller=[el for el in arr[1:] if el <= pivot]
        bigger = [el for el in arr[1:] if el > pivot]
        return quicksort(smaller) + [pivot] + quicksort(bigger)

print(quicksort([3,4,1,2,10,5,6]))