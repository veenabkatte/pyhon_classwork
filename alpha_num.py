#program for check whether the input is number ar alphabet
n=int(input("enter the input"))
def fibonacci(n):
    fib=fibonacci(n-1)+fibonacci(n-2)
    n.append(fib)
    return fib
print(fibonacci(n))