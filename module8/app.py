planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

print("The first planet is", planets[0])
print("The second planet is", planets[1])
print("The third planet is", planets[2])

planets[3] = "Red Planet"
print("Mars is also known as", planets[3])

planets.append("Pluto")
number_of_planets = len(planets)
print("There are actually", number_of_planets, "planets in the solar system.")

planets.pop()  # Goodbye, Pluto
number_of_planets = len(planets)
print("No, there are definitely", number_of_planets, "planets in the solar system.")
print("The last planet is", planets[-1])
print("The penultimate planet is", planets[-2])

# Find an item by value
jupiter_index = planets.index("Jupiter") # Returns the index of jupiter element
print("Jupiter is the", jupiter_index + 1, "planet from the sun")
