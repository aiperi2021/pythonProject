car_count = 0
car_name = ''
a_count = 0


car = ["bmwa", "kia", "lexus"]
for c in car:
    if c.__contains__('a'):
        a_count+=1
print(a_count)


print("there are ", car_count, 'cars', "and cars name are ", car_name)



