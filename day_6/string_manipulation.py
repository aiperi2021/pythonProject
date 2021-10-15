# concatenate string
a = "Hello"
b = "World"
c = a + b
print(c)

# add spacing
a = "Hello"
b = "World"
c = a + " " + b
print(c)

# using format() method  to insert numbers into strings:
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#ex
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# using index to locate number in string
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# remove empty spaces in string
p = " Python "
print(p.strip())


