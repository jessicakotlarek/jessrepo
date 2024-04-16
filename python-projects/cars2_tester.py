from cars2 import Car

cars = []
with open("cars.txt") as file:
    for line in file:
        line = line.strip()
        tokens = line.split()
        car = Car(tokens[0], tokens[1], int(tokens[2]), int(tokens[3]))
        cars.append(car)

print(cars[0])
print(cars[1])

print(cars[0].get_gas_tank())
print(cars[0].get_odometer())
print(cars[1].get_gas_tank())
print(cars[1].get_odometer())

cars[0].drive()
cars[1].drive()
print(cars[0].get_gas_tank())
print(cars[0].get_odometer())
print(cars[1].get_gas_tank())
print(cars[1].get_odometer())



