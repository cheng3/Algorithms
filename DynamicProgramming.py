
def LCS(a,b):
    '''
    Function to find the Longest Common Subsequence for two strings a, b
    Algorithm used: Dynamic programming with tabulation
    Method: 1. Create and fill LCS table to find length of LCS
            2. Traverse back through the table and get LCS characters
    '''
    #Create and fill LCS table
    length = [[0 for i in range(len(a)+1)] for j in range(len(b)+1)]
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if x == y:
                length[i+1][j+1] = length[i][j] + 1
            else:
                length[i+1][j+1] = max(length[i+1][j],length[i][j+1])
    #Traverse back through table and collect LCS characters
    result = ""
    i, j = len(a), len(b)
    while i != 0 or j != 0:
        if length[i][j] == length[i-1][j]:
            i -= 1
        elif length[i][j] == length[i][j-1]:
            j -= 1
        #We must have an LCS character, so add it to the result. Note the order!
        else:
            result = a[i-1] + result
            i -= 1
            j -= 1
    
    return result


def KadaneAlgo(aList):
    max_so_far = max_ending_here = aList[0]
    #Traverse through array calculating local max and comparing with global max
    for x in aList[1:]:
        max_ending_here = max(max_ending_here+x, x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far


def KadaneAlgoIdx(aList):
    max_so_far = max_ending_here = largest_neg = 0
    #start, end - endpoints of max subarray
    #beg - start of positive sum 
    start = end = beg = 0
    isNeg = True
    for i,x in enumerate(aList):
        max_ending_here += x
        if max_ending_here < 0:
            #keep track of largest negative value in case all elements in list is negative
            if (x > largest_neg) or (largest_neg == 0):
                largest_neg = x
                start = i
                end = i
            max_ending_here = 0
            beg = i+1
        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
            start = beg
            end = i
            isNeg = False
    if isNeg:
        global_max = largest_neg
    else:
        global_max = max_so_far
    print("Max sum = {} found in [{}:{}]".format(global_max, start, end))


def FastFib(n):
    if n <= 1:
        return n
    a = 0
    b = 1
    for i in range(2,n):
        c = a + b
        a = b
        b = c
    return b

def SuperFastFib(n):
    m = [[1,1],[1,0]]
    if n <= 1:
        return n
    if n == 2:
        return 1
    power(m, n)
    return m[0][1]

def MatrixPower(matrix, n):
    M = [[1,1],[1,0]]
    if n == 0 or n == 1:
        return
    MatrixPower(matrix, n // 2)
    if n % 2 == 0:
        multiply(matrix, matrix)
    else:
        multiply(matrix, M)
        
def multiply(X, Y):
    a = X[0][0]*Y[0][0] + X[0][1]*Y[1][0]
    b = X[0][0]*Y[0][1] + X[0][1]*Y[1][1]
    c = X[1][0]*Y[0][0] + X[1][1]*Y[1][0]
    d = X[1][0]*Y[0][1] + X[1][1]*Y[1][1]
    
    X[0][0] = a
    X[0][1] = b
    X[1][0] = c
    X[1][1] = d
    

def Exponent(x, n):
    #base case
    if n == 0:
        return 1
    if n == 1:
        return x
    #recursion and memoization
    temp = Exponent(x, y//2)
    if n % 2 == 0:
        return temp*temp
    return x*temp
        
    
    
    