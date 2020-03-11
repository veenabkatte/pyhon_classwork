#to check whether the given number is prime or not 
val=int(input("enter the num"))

for n in range(2,val):

    if(val%n)==0:

        print(val,"is a not prime number")

    else:

        print(val,"is a prime number")