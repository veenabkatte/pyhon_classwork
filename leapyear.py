#leap_year program
yr=int(input("enter the year"))

print(yr)

if(yr%4==0 and yr%100!=0 or yr%400==5):

    print("Leap Year")

else:

    print("not leap year")