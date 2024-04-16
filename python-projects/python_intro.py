print("hello world!")

# this is a one line comment

'''
this is one line
this is another line
these are comments
'''


# Variables in Python
x = 10
print(x)
x = "hello!"
print(x)
s = 'hello world'

x = 100
y = 10
r = int(x / y)
# ^ casting it to make it 10 rather than 10.0
print(r)

# OR
r = x // y
# ^ floor division (does the same thing as casting)
print(r)


# Math Functions
m = min(100,20)
print(m)
p = pow(2,4)
# ^ 2 raised to the power of 4
print(p)
# OR
p = 2**4 
print(p)


# If Statements
x = -1
y = 1

if x < 0:
    x = 1
    x += 10
    print(x)
    print("x was negative")

print('outside of if statement')


if x < 0 and y == 1:
    print("x negative and y is 1")
# doesnt excecute becuace x was changed above
    
if x < 0 or y == 1:
    print("x is negative or y is 1")
# this excecutes becuase it is an "or" rather than "and"
    

if x < 0:
    print('x is less than 0')
elif x > 0:
    print('x greater than 0')
else:
    print('x is 0')



# Loops
    
# While loop
counter = 0
while counter < 10:
    print(counter)
    counter += 1

# For loops
nums = [10,20,30,40,50]
for i in range(5): # iterates 0-4, starts at 0 and goes until one less than stated
    print(nums[i])

nums = [10,20,30,40,50]
for i in range(2, len(nums)): # starts at 2, iterates through 4 (length)
    print(nums[i])

# For each loops
for num in nums: # can name num anything I want
    num += 5 # not modifying the list, just adding to what is being printed out
    print(num)
print(nums)

# Enumerate loop (gives you access to both for loop and for each loop)
for i, val in enumerate(nums): # can name i anything I want
    print("i is ", i , 'and val is ', val)


# ex
dogs = ["boomer","rocky", "daisy"]

for i in range(len(dogs)):
    print(dogs[i])

for val in dogs:
    print(val)

for puppy, pup in enumerate(dogs):
    print("puppy is number ", puppy, "and name is ", pup)


# ex
numbers = [2,4,6,8,10,12]
sum = 0
for val in numbers:
    sum += val
print("the sum of nums is",sum) 
print(f"the sum of nums is {sum}") # these 2 do the same thing



# Functions 

def hello(name): # hello is the name of the function
    print("hello!", name)
hello("Bob") # calling the funciton using the name parameter


# with a default parameter
def hello(name="friend"): # giving the parameter a default value
    print("hello!", name)
hello() # calling the funciton without the parameter, can put a name even with the default
hello("Bob")


# Strings (you can use either single or double quotes)

fname = 'Jess'
lname = "Kotlarek"
print(fname, lname)

f_initial = fname[0] # geting the first initial of first name
print(f_initial)
f_initial = fname[-4]
print(f_initial)

last_char = fname[-1] # starts counting backwards to get last character in first name
print(last_char)

print('He said "Hi" to his friend.')
print("She's a great dancer.") # won't let you use single quotes here becuase of the apostrophe in "she's"


# String concatenation

full_name = fname + lname
print(full_name)


# More strings

print(full_name * 3)

fname_in_uppercase = fname.upper()
print(fname_in_uppercase)



# Slicing strings 
# string[starting index : ending index]

course = "Platform Computing"

Platform = course[0:8] # goes up to but not including the ending index
print(Platform)
Platform = course[:8] # if you omit the 0, it will start at the beginning and go up to but not including 8
print(Platform)

Computing = course[9:18] 
print(Computing)
Computing = course[9:] # if you omit the 18, it will start at 9 and go to the end of the string
print(Computing)



# Exercise

swap = [0,3,8,5,4]
# change it to look like [0,3,4,5,8]
print(swap)

temp = swap[2]
print(temp)

swap[2] = swap[4]
print(swap)

swap[4] = temp
print(swap)









