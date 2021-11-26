def sorting_selection(arr,asc=True):
    """selection sort algorithm, return the sorted value in ascending or descending

    Parameters
    ----------
    arr : `list` or `array`
        sequence of value that not in ordered        
    asc : `bool`
         (Default value = True)
        if true, return value in ascending list and vice versa
    Returns
    -------
    sorted value : `list`
        returning the sorted value in ascending (small to large) or descending (large to small) order
    """

    sorted_arr=[]
    if asc == True:
        for i in range(len(arr)): # do it again

            smallest=arr[0] 
            smallest_index=0
            for i in range(len(arr)):#access all element
                if arr[i] < smallest: # found the smallest number
                    smallest=arr[i] # store in smallest variabel
                    smallest_index=i #get the index of smallest variabel
            sorted_arr+=[smallest] #append the smallest number to list
            arr.pop(smallest_index) # remove the smallest number from arr
    else:
        for i in range(len(arr)):
            print(arr)
            largest=arr[0]
            largest_index=0
            for i in range(len(arr)):
                if arr[i] > largest:
                    largest=arr[i]
                    largest_index=i
            sorted_arr+=[largest]
            arr.pop(largest_index)

    return sorted_arr