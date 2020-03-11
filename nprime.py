# prime of first n numb



start=1

end=int(input("enter the number of digits "))

for val in range(start,end):

    if val>1:

        for n in range(2,val):

            if(val%n)==0:

                break

            else:

                print(val)

                break