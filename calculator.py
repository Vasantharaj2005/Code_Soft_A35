print("------MINI CALCULATOR-------")
# To add a number add function
def add(x, y):
    return x + y

#To subtract a number subtract function
def subtract(x, y):
    return x - y

#To multiply a number multiply function
def multiply(x, y):
    return x * y

#To divide a number divide function
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    else:
        return x / y

print("Select operation:")
print("Add means select -> 1")
print("Subtract means select -> 2")
print("Multiply means select -> 3")
print("Divide means select -> 4")

choice = input("Enter choice (1/2/3/4): ")

#To get the input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Invalid input Please enter a number")



