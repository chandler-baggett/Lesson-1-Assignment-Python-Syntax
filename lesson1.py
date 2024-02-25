#1. Python Indentation Practice with if Statements:
#Task 1: Code Correction
weather = "sunny"

if weather == "sunny":
    print("Wear sunglasses!")
else:
    print("Take an umbrella!")

#Task 2: Your Mood Today
mood = input("How do you feel today?")
if mood == "happy":
    print("That's great to hear!")
elif mood == "sad":
    print("I hope your day gets better!")

#Task 3: Spotting Indentation Errors
mood = "excited"

if mood == "excited":
    print("Yay! Let's have fun.")
else:
    print("Let's find something fun to do!")

#2. Python Comments & Multi-line Practice
#Task 1: Create a Poem using Comments
# Python, oh Python, so clear and so neat
# With every new challenge, you're hard to beat.
# From what I understand, you make it easy to greet
# You make hello world such an easy feat
# Alas, your codewars 6kyu make me want to retreat
    
#Task 2: Multi-line Poem
'''
Python, in the realm of code you shine,
With simplicity and grace, you're truly divine.
I stare at my laptop, considered my shrine
I study and study, typing to pass time
After several hours of coding, I start to feel like slime
'''

# Task 3: Combining Single and Multi-line Comments
'''
After several hours of coding, I start to feel like slime
'''
#it's best to stretch after some period of time

# Alas, your codewars below 6kyu make me want to retreat
# codewars is not easy to master

#3. Python Naming Convention Practice
#Task 1: Code Correction
PI_VALUE = 3.14
user_age = 25
user_location = "New York"
MAX_LIMIT = 1000

#4. Python Data Types and type() Function
#Task 1: Code Correction
variable_a = "Hello, World!"
#str
print(type(variable_a))
variable_b = 23
#int
print(type(variable_b))
variable_c = 3.14
#float
print(type(variable_c))
variable_d = True
#bool
print(type(variable_d))

#5. Python Dynamic Typing Practice
# Task 1: Code Correction
dynamic_variable = "This is a string"
print(type(dynamic_variable))

dynamic_variable = 100
print(type(dynamic_variable))

dynamic_variable = 25.5
print(type(dynamic_variable))

#6. Arithmetic Operations in Daily Life
#Task 1: Grocery Store Math
def groceryStoreMath(a, b, c):
    return a + b + c

print(groceryStoreMath(1, 5, 1))

#Task 2: Bank Interest
def bankInterest(a, b):
    return a * b

print(bankInterest(1000, .5))

#Task 3: Area and Perimeter
def areaAndPerimeter(length, width):
    return [length * width, 2 * length + 2 * width]

print(areaAndPerimeter(3, 5))

#7. Understanding Assignments and Comparisons
# Task 1: Value Swapping
def swapValues(x, y):
    x,y = y,x
    return x,y

print(swapValues(1, 3))

# Task 2: Perfect Square Checker
import math
def is_square(num):
    return num == math.isqrt(num) ** 2

print(is_square(9))
print(is_square(8))

#8. Exploring Logical Operations and Precedence

#Task 1: Simple Logic Puzzles
print(True or False and True)
print(True or True and True)
print(False or True and True)
print(False or True and False)

#Task 2: Validating Calculations
print(1 + 2 * 3)
print((1 + 2) * 3)

#Task 3: Mix and Match
if (2 + 3) * 5 < (3 - 1) * 2:
    print("What a mix and match!")
else:
    print("What so not!")