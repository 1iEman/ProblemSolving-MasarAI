'''
ALgorithm:
1. Promote user to Enter number of rows and columns for the matrix
2. Create matrix[row][column] using nested loop and promote user to enter values
3. Use for loop to sum First diagonal using matrix[i][i]
4. Use for loop to sum Second diagonal using matrix[i][j] and j = -1 then decrement it each loop
3. Subtract First from Second diagonal then use abs function
4. Print the result
'''

rows = int(input("rows: "))
col = int(input("columns: "))

matrix = [] 
print("entries row-wise:")

for i in range(rows):   
    row = []
    for j in range(col):
        row.append(int(input("Enter value: " )))    
    matrix.append(row)  # adding rows to the matrix

print("\n2D matrix is:")

for i in range(rows):
    for j in range(col):
        print(matrix[i][j], end=" ")
    print()


first_diagonal  = 0
second_diagonal = 0

for i in range(len(matrix)):
      print(i , j)
      print(matrix[i][j])
      first_diagonal += matrix[i][i]
   

j = -1
for k in range(len(matrix)):
      second_diagonal += matrix[k][j]
      j-=1

diffe = abs(first_diagonal - second_diagonal)
print("The difference is: " , diffe)
