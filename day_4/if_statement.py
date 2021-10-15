# Using true vs false
is_Tuesday = True
is_Friday = True
is_Monday = False
is_Evening = True
is_Morning = False

if is_Monday:
    print("I have python class")
else:
    print("I dont have python class")

# try multiple condition
if is_Friday or is_Monday:
    print("I have python class")
else:
    print("I dont have python class")


if is_Friday and is_Evening:
    print("I have python class")
else:
    print("I dont have python class")

if is_Friday and is_Morning:
    print("I have python class")
else:
    print("I dont have python class")


if is_Friday and not is_Morning:
    print("I have python class")
else:
    print("I dont have python class")

if is_Friday and is_Morning:
    print("I dont have python class")
elif is_Monday and is_Evening:
    print("I have python class")
else:
    print("I dont have python class in any of this time ")


