def contains_duplicate(numbers = []):
  is_duplicated = False
  start_index = 1

  for number in numbers:
    
    if number in numbers[start_index : ]:
      is_duplicated = True
    
    if is_duplicated:
      break

    start_index += 1
  
  return is_duplicated

print(contains_duplicate([1, 1, 3, 4]))
print(contains_duplicate([1, 2, 3, 4]))
print(contains_duplicate([1, 2, 3, 4 , 5 , 6 ,6]))
print(contains_duplicate([]))

