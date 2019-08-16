#Write a program that determines the number of trailing zeros at the end of X! (X factorial), where X is 
#an arbitrary number. For instance, 5! is 120, so it has one trailing zero. 
#(How can you handle extremely values, such as 100!?) The input format should be that the 
#program asks the user to enter a number, minus the !. 
import math

UserInput = int(input("Give me a number"))

X = math.factorial(UserInput)

strX = str(X)

stripped_strX = strX.rstrip("0")

print(len(strX) - len(stripped_strX))