# Create a variable named hometown with the value of the town where you graduated highschool.
hometown = "Khammam"

# Create a variable named x with a value of 298784. 
x = 298784

# Create two variables, j and l, with values, 5 and 10, respectively. Sum them together and print out the result. Use only 3 lines of code.
j=5
l=10
print(j+l)

# Create a variable named z. Assign it a value equal to the sum of j and l. Print out the result.
z = j+l
print(z)

# Using a single line of code, assign the variables t, q, r, and s the value of education.
t=q=r=s= "education"

# Given the following in Python, identify the data types for each variable. 
x = ["apple", "banana", "cherry"]
y = ("apple", "banana", "cherry")
f = False
g = 'covid-19'

print(type(x))
print(type(y))
print(type(f))
print(type(g))

# If-Else and Scope\

x = 0
j = 3

def funky(arg1, arg2):
	x = 1
	j = 5
	if arg1 > arg2:
		print('arg1 is greater than arg2')
	else:
		print('arg1 is not greater than arg2')
	print(j)

funky(x, j)

print(x)
print(j)

# Change the code such that the global and local variables reference each other, rather than as separate. That is, if I change the variable at the local level within the function, the same value will be available at the global level.
x = 0
j = 3

def funky():
    global x
    global j
    x = 1
    j = 5
    
    if x > j:
        print('x is greater than j')
    else:
        print('x is not greater than j')
    print(j)

funky()

print(x)
print(j)

# Write a for loop to print each item. Use two lines of code.
lunches = ['burger','apple','soba','chahan']
for x in lunches:
    print(x)

# If the food is apple exit the loop immediately.  
for x in lunches:
    print(x)
    if x == 'apple':
        break