def MergeSort(aList):
    '''
    Merge sort algorithm
    Note we are passing a slice of aList in each recursive call -
    any modification to aList will have its effect propagated through
    the recursion stack and so there's no need for a function "return"
    '''
    #if aList only has single element then it's sorted by definition
    if len(aList) > 1:
        mid = aList // 2
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


def CountSort(lst, k):
    #Initialise temp and sorted list
    temp = [0 for i in range(k+1)]
    Sorted = [0]*len(lst)
    for i in lst:
        if i == 0:
            temp[0] += 1
        else:
            temp[i] += 1
    #THIS STEP IS KEY!!!!!
    #Get running total for temp
    for i in range(1,len(temp)):
        temp[i] += temp[i-1]
    #place each element from lst into correct position in Sorted
    for i in lst:
        Sorted[temp[i]-1] = i
        temp[i] -= 1  #handles duplicate values
    return Sorted
        
        
        