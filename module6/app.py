# Strings

# Search for string inside another string

"Moon" in "This text will describe facts and challenges with space travel"

"Moon" in "This text will describe facts about the Moon"

temperatures = """Saturn has a daytime temperature of -170 degrees Celsius,
while Mars has -28 Celsius."""
print(temperatures.find("Moon")) # when is not found
print(temperatures.find("Mars")) # when is found return the index

# Another way to search for content is to use the .count() method, which returns the total number of occurrences of a certain word in a string:

mars_temperature = "The highest temperature on Mars is about 30 C"
for item in mars_temperature.split():
    if item.isnumeric():
        print('Mars temp:', item)

# Formatting strings

# Using multiple values changes the syntax, because it requires parentheses to surround the variables that are passed in:
print("""Both sides of the %s get the same amount of sunlight, 
but only one side is seen from %s because
the %s rotates around its own axis when it orbits %s.""" % ("Moon", "Earth", "Moon", "Earth"))

mass_percentage = "1/6"
title = 'hello python'

print("On the Moon, you would weigh about {} of your weight on Earth".format(mass_percentage))
print("""You are lighter on the {0}, because on the {0} 
you would weigh about {1} of your weight on Earth""".format("Moon", mass_percentage))

# To improve readability use keywords arguments in format and then reference the same arguments within braces
print("""You are lighter on the {moon}, because on the {moon} 
you would weigh about {mass} of your weight on Earth""".format(moon="Moon", mass=mass_percentage))

# f-strings, you can use expressions inside the braces
print(f'Mas percentage is {mass_percentage}')
print(f'Mas percentage is {round(100/6, 1)}')
print(f'The title using f-string is {title.title()}')

name = 'Ganymede'
planet = 'Mars'
gravity = '1.43'

template =  f"""Gravity Facts about {name}
----------------------------------------
Planet Name: {planet}
Gravity on {name}: {gravity} m/s2"""