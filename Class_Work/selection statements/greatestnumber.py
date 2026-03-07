# Program to find the greatest number among five numbers
# using if, elif and else statements

# Taking input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
num4 = float(input("Enter fourth number: "))
num5 = float(input("Enter fifth number: "))

# Checking which number is the greatest
if num1 >= num2 and num1 >= num3 and num1 >= num4 and num1 >= num5:
    greatest = num1

elif num2 >= num1 and num2 >= num3 and num2 >= num4 and num2 >= num5:
    greatest = num2

elif num3 >= num1 and num3 >= num2 and num3 >= num4 and num3 >= num5:
    greatest = num3

elif num4 >= num1 and num4 >= num2 and num4 >= num3 and num4 >= num5:
    greatest = num4

else:
    greatest = num5

# Display the greatest number
print("The greatest number among the five numbers is:", greatest)