''''
for is a keyword
any variable after for is the control variable
'''
for i in range(2,10,) :
    print("The current value of i is currently", i )
'''
break is used to exit a loop
continue- here the next turn is started and the condition expressiom is tested immediately
below is a good example of break ad continue in a loop
'''
print("The break instruction: ")
for i in range(1, 5):
    if i == 3:
        break
    print("Inside the loop", i )
print("outside the loop")

print("\nThe continue instruction: ")
for i in range(1, 5 ):
    if i == 3:
        continue
    print("Inside the loop.", i )
print("Outside the loop.")