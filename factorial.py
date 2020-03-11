#to find the factorial of given numbers
num=int(input("enter the number"))
fact=1
for i in range(1,num+1):
    fact=fact*i
print("the factorial of number is",fact)