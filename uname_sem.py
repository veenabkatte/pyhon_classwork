#program for accepting the user_name only if sem is 6
uname=input("enter the user name")
sem=int(input("enter the sem"))
if sem==6:
    print("the username is",uname)
else:
    print("enter the valid sem")