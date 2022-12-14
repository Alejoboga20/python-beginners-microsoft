# Dictionaries

planet = {
    'name': 'Earth',
    'moons': 1
}

print(planet.get('name')) # Get method is used to access a value using its key
print(planet['name']) # Also valid

### Although the behavior of get and the square brackets ([ ]) is generally the same for retrieving items, there is one key difference. If a key isn't available, 
# get returns None, and [ ] raises a KeyError ###

# Modify Dictionaries
planet.update({'name': 'Mars', 'moons': 10})
print(planet)
planet.update({'name': 'Mars', 'moons': 10, 'extra': 'asd'}) # Can add key value pairs
print(planet)

planet['name'] = 'EarthAgain'
print(planet)

# Add and remove keys
original_planet = { 'name': 'Earth',  'moons': 1}
original_planet['orbital_period'] = 4333
print('Original Planet: ', original_planet)

original_planet.pop('orbital_period')
print('Original Planet: ', original_planet)

original_planet['diameter [km]'] = {
  'polar': 1234,
  'equatorial': 4321
}

print('Planet with dictionary inside: ', original_planet)
print(f"Diameter in KM: {original_planet['diameter [km]']['polar']}")

# Keys and values
rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}

for key in rainfall.keys():
  print(f'{key}: {rainfall[key]}cm3')

if 'december' in rainfall: # Check if key exists before update value
  rainfall['december'] = rainfall['december'] + 1
else:
  rainfall['december'] = 1

total_rainfall_amount = 0

for value in rainfall.values():
  total_rainfall_amount += value

print(total_rainfall_amount)