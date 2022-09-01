# While loop
from time import sleep

new_planet = ''
planets = []

while new_planet.lower() != 'done':
    if new_planet:
        planets.append(new_planet)
    new_planet = input('Enter a new planet, or done if done: ')

print(planets)

# For Loop
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
countdown = [4, 3, 2, 1, 0]

for number in countdown:
    print(number)
    sleep(1)  # Wait 1 second
print("Blast off!! 🚀")