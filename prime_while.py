#to check whether the given number is prime or not 
val=int(input("enter the num"))
f=0
i=2
while i<=val/2:
    if val % i == 0:
        f=1
        break
    i=i+1
if f==0:
        print(val,"is a prime number")

else:

        print(val,"is  not  a prime number")