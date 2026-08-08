#read 3 numbers
'''number1=int(input("Enter the first number: "))
number2=int(input("Enter the second number: "))
number3=int(input("Enter the third number: "))
#assume that the first number is the larest one
largest_number=number1
if number2>number1:
    largest_number=number2
if number3>largest_number:
    largest_number=number3

print("The largest number is: ", largest_number)'''
#the above condition can be simplified using max

''''number1=int(input("Enter the first number: "))
number2=int(input("Enter the second number: "))
number3=int(input("Enter the third number: "))

largest_number=max(number3,number1,number2)

print("The largest number is: ", largest_number)'''

#lab- comparison operators and conditionals
answer = input("write your favourite plant: ")
if answer == "Spathiphyllum":
    print("Yes-Spathiphyllum is the best.")
elif answer == "spathiphyllum":
    print("N0, I want a big spathiphyllum!")
else:
    print("Spathiphyllum! Not [input]")