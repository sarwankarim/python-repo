# Write a Python program to calculate the sum of the digits in an integer
input_value=int(input("Enter a Number: "))
number=input_value
last_number=0
while number > 0:
	last_number += number % 10
	number = number // 10
print("Sum of n Positive integers till {} is {}".format(input_value, last_number))

# Write a python program to sum of the first n positive integers
n=int(input("Enter value of n: "))
sum=(n * (n+1))/2
print("Sum of n Positive integers till {} is {}".format(n, sum))

# Write a Python program to calculate body mass index
meter=int(input("Enter Height in cm: "))
kg=int(input("Enter Weight in Kg: "))
bmi=(kg / (meter*0.01)**2)
print("Your BMI is ", bmi)

# Write a Python program to convert height in feet to centimetres.
feet=int(input("Enter Height in Feet: "))
cm=30.48*feet
print("There are {} Cm in {} ft".format(cm, feet))

# write a Python program to compute the distance between the points (x1, y1) and (x2, y2).
x1=int(input("Enter Co-ordinate for x1: "))
y1=int(input("Enter Co-ordinate for y1: "))
x2=int(input("Enter Co-ordinate for x2: "))
y2=int(input("Enter Co-ordinate for y2: "))
distance = (((x2-x1)**2) + ((y2-y1)**2))**(0.5)
print("Distance between points ({}, {}) and ({}, {}) is {}".format(x1, y1, x2, y2, distance))

# Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years
amount=int(input("Please enter principal amount: "))
interest_rate=float(input("Please Enter Rate of interest in %: "))
years=int(input("Enter number of years for investment: "))
interest=amount*interest_rate*years
print("After {} years your principal amount {} over an interest rate of {}% will be {}".format(years, amount, interest_rate, interest))

# Write a Python program that will accept the base and height of a triangle and compute the area
base=int(input("Enter base: "))
height=int(input("Enter height: "))
area=0.5*base*height
print("The area of the triangle is: ", area)

# Write a Python program to test whether a passed letter is a vowel or not
vowels=["a","e","i","o","u"]
letter=input("Enter a character: ")
if letter.lower() in vowels:
	print("Letter {} is Vowel".format(letter))
else: print("Letter {} is not Vowel".format(letter))


# Check if number is Even or Odd
number=int(input("Enter Number: "))
if number % 2 == 0:
	print(number, "is Even")
else: print(number, "is Odd")

# Write a Python program to get a string which is n (non-negative integer) copies of a given string.
text=input("Enter String: ")
number=int(input("Enter Number: "))
print("{} Copies of {} are ".format(number,text), end="")
for i in range(number):
	print(text, end="")
	
#Divisibility Check of two numbers
numerator=int(input("Enter numerator: "))
denominator=int(input("Enter denominator: "))
if numerator % denominator == 0:
	print('Number {} is Completely divisible by {}'.format(numerator,denominator))
else:
	print('Number {} is not Completely divisible by {}'.format(numerator,denominator))

# 1. Calculate Area of a Circle
radius=int(input("Enter Radius: "))
area = 3.141592 * (radius**2)
print("The Area is: ", area)


# Check Number either positive, negative or zero
number=int(input("Enter Number: "))
if number < 0:
    print("Negative Number Entered")
elif number > 0:
    print("Positive Number Entered")
else: print("Zero Entered")
