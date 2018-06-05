##########################################
#
# MERGE SORT
#
##########################################
def MergeSort(aList):
    '''
    Merge sort algorithm
    Note we are passing a slice of aList in each recursive call -
    any modification to aList will have its effect propagated through
    the recursion stack and so there's no need for a function "return"
    '''
    #if aList only has single element then it's sorted by definition
    if len(aList) > 1:
        mid = len(aList) // 2
        leftHalf = aList[:mid]
        rightHalf = aList[mid:]
        
        #recursion
        MergeSort(leftHalf)
        MergeSort(rightHalf)
        
        #define indices for leftHalf, rightHalf and aList
        i = j = k = 0
        
        #compare and merge the sublists back into the main list aList
        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] < rightHalf[j]:
                aList[k] = leftHalf[i]
                i += 1
            else:
                aList[k] = rightHalf[j]
                j += 1
            k += 1
        
        #take care of any leftover elements from leftHalf and rightHalf
        while i < len(leftHalf):
            aList[k] = leftHalf[i]
            i += 1
            k += 1
            
        while j < len(rightHalf):
            aList[k] = rightHalf[j]
            j += 1
            k += 1

##########################################
#
# COUNTING SORT
#
##########################################
def CountSort(lst, asc=True):
    #Find maximum value from list
    maxVal = max(lst)
    #temp will contain lists of numbers whose values all equal its index
    temp = [[] for i in range(maxVal+1)]
    Sorted = []
    #Populate temp
    for val in lst:
        temp[val].append(val)
    #Now temp will contain values sorted in ascending order
    if asc:
        for sublist in temp:
            Sorted += sublist
    else:
        for i in range(maxVal,-1,-1):
            Sorted += temp[i]
    return Sorted

##########################################
#
# RADIX SORT
#
##########################################
def RadixSort(lst, base=10):
    def SortByDigit(lst, base, it):
        temp = [[] for i in range(base)]
        Sorted = []
        #Sort lst in ascending order based on the ith positional digit
        #Use counting sort for this
        for num in lst:
            #Get the ith positional digit from the number
            digit = (num // (base**it)) % base
            temp[digit].append(num)
        for sublist in temp:
            Sorted += sublist
        return Sorted
    
    maxVal = max(lst)
    it = 0
    #Sort lst by each positional digit in turn
    while base**it <= maxVal:
        lst = SortByDigit(lst, base, it)
        it += 1
    return lst

    
##########################################
#
# HEAP SORT
#
##########################################
def MaxHeapify(lst, i):
    size = len(lst) - 1
    leftChild, rightChild = 2*i+1, 2*i+2
    j = i
    #if we reach a leaf
    if leftChild > size or rightChild > size:
        return lst
    if lst[i] < lst[leftChild]:
        j = leftChild
    elif lst[i] < lst[rightChild]:
        j = rightChild
    else:
        return lst
    #swap parent and child values
    lst[i], lst[j] = lst[j], lst[i]
    return MaxHeapify(lst, j)