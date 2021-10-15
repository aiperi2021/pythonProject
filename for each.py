cars = ["Ford", "Volvo", "BMW"]

# def length_car():

count = 0
count2 = 0

for i in cars:
    for b in i:
        count += 1
        if count2 < count:
            count2 = count

print(count2)








