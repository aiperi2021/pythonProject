
num2 = ""
op = ""
num1 = input("Enter number 1:")
if bool(num1):
    num2 = input("Enter number 2:")
    if bool(num2):
        op = input("Enter operation")
        if op =="+":
            print("Addition operation is complete: ", int(num1)+int(num2))
        elif op =="-":
            print("Deduction operation is complete: ", int(num1)-int(num2))
        elif op =="/":
            print("Division operation is complete: ", int(num1)/int(num2))
        elif op =="*":
            print("Multiplication operation is complete: ", int(num1)*int(num2))
    else:
        print("second value should not be empty")
        print(">>>>>>>>>>>> Program terminated")

else:
    print("first value should not be empty")
    print(">>>>>>>>>>>>>> Program terminated")

