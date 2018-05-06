def Fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-2) + fib(n-1)


def ReverseString(s):
    #base case
    if s == "":
        return
    return s[-1] + Reverse(s[:-1])

