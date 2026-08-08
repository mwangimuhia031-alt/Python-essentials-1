'''
Variable are kind of containers where data can be  stored.
The nanme of the variable must not be any of pythons reserved words,must begin with  letter
and can even have underscores
eg
'''
#making a variable
var=1
account_balance=1000
client_name= 'trey Chelsea'
print(var, account_balance, client_name)

#lab
john=3
mary=5
adam=6
print( john ,mary, adam, sep="," )
total_apples=john+mary+adam
print(total_apples)

kilometers=12.25
miles=7.38
# 1 mile = 1.61 kilometers
miles_to_kilometers= miles * 1.61
kilometers_to_miles= kilometers / 1.61

print(miles, "miles is ", round(miles_to_kilometers, 2) ,"kilometers")
print(kilometers, "kilometers is ", round(kilometers_to_miles, 2) ,"miles")


a=6
b=3
a /=2*b
print(a)