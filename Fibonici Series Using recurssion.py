def fib(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return fib(n-1)+fib(n-2)
a=fib(25+25+2)
print(a)