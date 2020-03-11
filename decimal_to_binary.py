#program to convert from decimal to binary

decimal=input("Enter the decimal number\n")
def DecimalToBinary(decimal):
    if decimal>1:
        DecimalToBinary(decimal//2)
    print(decimal%2,end="")
DecimalToBinary(int(decimal))