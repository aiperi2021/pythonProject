#looping (that is either a list, a tuple, a dictionary, a set, or a string)
# list looping
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# string looping
for x in "banana":
  print(x)

# exit looping once the correct is found
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break


# continue with next iteration
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)


# range() function
for x in range(6):
  print(x)

# range(2,6) from 2 to 6
for x in range(2, 6):
  print(x)


print("Range with 3 parameters")
# range increment by 3
for x in range(2, 30, 3):
  print(x)

# if else in loop
for x in range(6):
  print(x)
else:
  print("Finally finished!")

# nested loop
  adj = ["red", "big", "tasty"]
  fruits = ["apple", "banana", "cherry"]

  for x in adj:
    for y in fruits:
      print(x, y)

# using pass
print("using pass")
for x in [0, 1, 2]:
  pass
