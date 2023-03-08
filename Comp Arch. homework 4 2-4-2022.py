# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 17:42:08 2022

@author: jt108
"""

#Jacob Thomas#
#Comp Arch. and operating systems
#2/4/2022


########## Problem 3 ##########

### Binary to decimal ###
#decimal base 1
#each value to exponent

'''
def BinaryDecimal(num):
    
    
    exponent = 1
    decimal = 0
    
    while(num):
        num = int(num%10) #divide by 10 remainder
        
        decimal = num * exponent
        exponent = exponent * 2
    return decimal

num = int(input("Enter binary number: ")) #enter binary number
print(BinaryDecimal(num)) #print decimal number
'''


"""

binary = int(input("Enter binary number: "))
decimal = 0 #the final result
exponent = 1 #value of exponent, each number is multiplied by the exponent

for values in binary:
    decimal = decimal * exponent
    exponent = exponent * 2 

print(decimal)   
    
"""







### Decimal to binary ###

"""
def DecimalBinary(num):
    
    if num > 1: #greater than 1
        DecimalBinary(num // 2) #makes it as integer and not a float value. Rounds it
    print(num % 2) #remainder of num divided by 2

num = int(input("Enter a decimal value: ")) #input decimal value
DecimalBinary(num) #calling function


"""





########## Problem 4 ##########

### Hexadecimal to binary ###
"""
def HexaToBinary(hexa):
    
    for x in hexa:
        
        if x == "0": #If number or letter is input then prints out binary value
            print("0000")
        elif x == "1":
            print("0001")
        elif x == "2":
            print("0010")
        elif x == "3":
            print("0011")
        elif x == "4":
            print("0100")
        elif x == "5":
            print("0101")
        elif x == "6":
            print("0110")
        elif x == "7":
            print("0111")
        elif x == "8":
            print("1000")
        elif x == "9":
            print("1001")
        elif x == 'A':
            print("1010")
        elif x == 'B':
            print("1011")
        elif x == 'C':
            print("1100")
        elif x == 'D':
            print("1101")
        elif x == 'E':
            print("1110")
        elif x == 'F':
            print("1111")
            
hexa = input("Enter a hexadecimal value: ") #input hexa value
HexaToBinary(hexa) #calling the function

"""



### Binary to hexadecimal ###
"""
def BinaryToHexa(binary):
    
    for x in binary:
        
        if x == "0000":
            print("0")
        elif x == "0001":
            print("1")
        elif x == "0010":
            print("2")
        elif x == "0011":
            print("3")
        elif x == "0100":
            print("4")
        elif x == "0101":
            print("5")
        elif x == "0110":
            print("6")
        elif x == "0111":
            print("7")
        elif x == "1000":
            print("8")
        elif x == "1001":
            print("9")
        elif x == '1010':
            print("A")
        elif x == '1011':
            print("B")
        elif x == '1100':
            print("C")
        elif x == '1101':
            print("D")
        elif x == '1110':
            print("E")
        elif x == '1111':
            print("F")

binary = input("Enter a binary value: ") 
BinaryToHexa(binary) 

"""
"""
binary = input("Enter a binary value: ") #input binary value
        
if binary == "0000":
    print("0")
elif binary == "0001":
    print("1")
elif binary == "0010":
    print("2")
elif binary == "0011":
    print("3")
elif binary == "0100":
    print("4")
elif binary == "0101":
    print("5")
elif binary == "0110":
    print("6")
elif binary == "0111":
    print("7")
elif binary == "1000":
    print("8")
elif binary == "1001":
    print("9")
elif binary == '1010':
    print("A")
elif binary == '1011':
    print("B")
elif binary == '1100':
    print("C")
elif binary == '1101':
    print("D")
elif binary == '1110':
    print("E")
elif binary == '1111':
    print("F")
            

"""










