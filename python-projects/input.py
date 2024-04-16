num = int(input("Enter a number: ")) # cast it to an int because otherwise it would give an error when += 10 bc it's a string
print(num)
num += 10
print(num)

try: 
    num = int(input("Enter a number: "))
    num += 10
except: 
    print("You did not enter a number.")

print("continue")


with open("movies.txt") as file:
    for line in file:
        line = line.strip()
        print(line)

with open("heights.txt") as file:
    for line in file:
        line = line.strip()
        tokens = line.split()
        print(tokens)







        