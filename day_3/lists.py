#collection
# list can store Str, int, bool
cars = ["bmw", "mercedes", "lexus", "toyota", "porche"]
print(cars)
# reach element in list
print(cars[0])
# negative starts from backward
print(cars[-1])
# read start from
print(cars[1:])
# print range
print(cars[1:3])

# list exersice
car = ["bmw", "mercedes", "lexus","bmw", "toyota", "porche"]
print(car)

# adding the list
car.append("volvo")
print(car)

# insert elements for location
car.insert(0,"kia")
print(car)

# remove element from list
car.remove("toyota")
print(car)

#remove last from list
car.pop()
print(car)

#look for items in list
print(car.index("bmw"))

# count dublicates
print(car.count("bmw"))

# sort list
car.sort()
print("Sorted car: ",car)


# empty the list
car.clear()
print(car)

# work with list of numbers
numb=[1,44,23,35,7,9,10]
print(numb)

# reverse numb
numb.reverse()
print(numb)

# copy list
numb2 = numb.copy()
print(numb2)

