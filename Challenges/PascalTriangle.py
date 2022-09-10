
number_of_rows = input("Enter a number to calculate Pascal's Triange: ")

def pascal_triangle(rows = 1):
  "Generate Pascal's Triange"
  pascal_array = []

  for line in range(0, rows):
    pascal_partial_array = []

    for row_index in range(0, line + 1):
      res = 1

      if (row_index > line - row_index) :
        row_index = line - row_index
        
      for column_index in range(0 , row_index) :
        res = res * (line - column_index)
        res = res // (column_index + 1)
    
      pascal_partial_array.append(res)
    pascal_array.append(pascal_partial_array)
  
  return(pascal_array)

p = pascal_triangle(int(number_of_rows))
print(p)