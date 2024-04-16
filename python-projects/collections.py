lst = [10,20,30,40,50]
# to add values to the list:
lst.append(5)
lst.append(6)
lst.append(7)
print(lst)

# to remove a chosen value:
lst.remove(40)
print(lst)
# to remove at a specific index place:
lst.pop(2)
print(lst)

# to reverse list:
lst.reverse()
print(lst)

# to sort list in ascending order:
lst.sort()
print(lst)

# changing values in list:
lst[0] = 500
print(lst)

# list slicing
lst = lst[1:]
print(lst)

# finding index place of certain value
index = lst.index(7)
print(index)

# count the number of times a certain value appears in list
lst.append(20)
lst.append(20)
lst.append(20)
print(lst)
num20 = lst.count(20) # USE FOR HOMEWORK 2
print(num20)

# to make a copy of a list
lst_copy = lst # won't actually make a new copy
print(lst_copy)
lst_copy[1] = 99
print(lst_copy)
print("original list:", lst) # the original list has also been modified, even though we only changed the value in the copy

new_copy = lst.copy() # this is the right way to make a copy
print(new_copy)
new_copy.append(3)
print(new_copy)
print(lst)

# another way to make a copy
new_copy = lst[:] # slicing the whole list


# creating an empty list
empty_lst = []
print(empty_lst)
for val in new_copy:
    empty_lst.append(val)
print(empty_lst)

# initializing list to a certain number of values
empty_lst = [0] * 10 # an empty list of 10 zeroes
print(empty_lst)

# list comprehension in for loop form
squares = []
for val in range(1, 10):
    squares.append(val * val) # or (i**2)
print(squares)

# list comprehension
print(lst)
plus_5 = [val + 5 for val in lst]
print(plus_5)

small_values = [x for x in lst if x < 20]
print(small_values)

# DICTIONARIES
    # keys are unique, values do not have to be

# creating a food dictionary
fav_foods = {"Kathleen" : "pizza", "Mya" : "ice cream", "Tom" : "ice cream",
             "Eric" : "steak"}
print(fav_foods)

# what is mya's favorite food?
mff = fav_foods["Mya"]
print(mff)


# iterating through the dictionary
for key in fav_foods:
    print(f"{key}'s favorite food is {fav_foods[key]}")


for person, food in fav_foods.items():
    print(f"{person}'s favorite food is {food}")

if "Bob " in fav_foods:
    print(fav_foods["Bob"])
else: 
    fav_foods["Bob"] = "wings"
print(fav_foods)





