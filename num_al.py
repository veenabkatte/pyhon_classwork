#program for check whether the input is number ar alphabet
n=int(input("enter the input"))
n1,n2=0,1
count = 0

if n<=0:
    print("please enter a positive integer")
elif n==1:
    print("fibonacci sequence upto",n)
    print(n1)
else:
    print("fibonacci sequence:")
    while count < n:
        print(n1)
        n=n1+n2
        n1=n2
        n2=n
        count +=1
    
