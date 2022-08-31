import sys # To Capture inputs
from datetime import date

sum = 1 + 2
print('Value of sum is: ', sum)

product = 1 * 2
print('And product is: ', product)

# Types

planets_in_solar_system = 8 # int, pluto used to be the 9th planet, but is too small
distance_to_alpha_centauri = 4.367 # float, lightyears
can_liftoff = True
shuttle_landed_on_the_moon = "Apollo 11" #string

type(distance_to_alpha_centauri) ## <class 'float'>
print(type(can_liftoff))

# Operators

left_side = 10
right_side = 5
result = left_side / right_side
print(result)

# Date
print('Today is:', date.today())
print('Today is: ' + str(date.today()) + ' with as string')

# Collect input
# Command-Line
print(sys.argv)
print(sys.argv[0]) # program name
print(sys.argv[1]) # first arg

# User input
print("Welcome to the greeter program")
name = input("Enter your name ")
print("Greetings: " + name)