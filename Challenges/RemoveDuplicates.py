numbers = [1, 1, 1, 4, 4, 7, 7, 8, 9, 9, 10 , 11, 32, 32, 32, 45, 555, 567, 777, 777]
numbers_to_remove = [1, 1, 1, 4, 4, 7, 7, 8, 9, 9, 10 , 11, 32, 32, 32, 45, 555, 567, 777, 777]

def reorder_duplicated_numbers(numbersArray = []):
  "Reorder Duplicated numbers from a sorted numbers array"

  endIndex = 0
  startIndex = 1

  for number in numbersArray:
    if number in numbersArray[startIndex : len(numbersArray) - endIndex]:
      endIndex += 1
      numbersArray.append(number)
      numbersArray.remove(number)
    else:
      startIndex += 1

  return numbersArray;

t = reorder_duplicated_numbers(numbers)
print('Final Reorder: ', t)

def remove_duplicated_numbers(numbersArray = []):
  "Remove Duplicated numbers from a sorted numbers array"

  startIndex = 1
  clean_array = []
  
  for number in numbersArray:
    if number not in numbersArray[startIndex : ]:
      clean_array.append(number)

    startIndex += 1
    
  return clean_array


k = remove_duplicated_numbers(numbers_to_remove)
print('Final Removed: ', k)