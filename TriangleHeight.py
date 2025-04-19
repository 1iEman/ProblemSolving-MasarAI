'''
ALgorithm : 
1. Promote user to Input the height n.

2. Loop from i = 1 to n (each row):

    Initialize an empty list line.

    Loop j = 0 to i-1:

        Append 2^j (power of 2) as a string to line.

    Loop j = i-2 down to 0:

        Append 2^j as a string to line.

    Join the list line into a single string and print it.
'''

'''
Pseudocode: 
START
  INPUT height
  FOR i FROM 1 TO height DO
    SET line TO empty list

    FOR j FROM 0 TO i-1 DO
      ADD 2^j AS STRING TO line

    FOR j FROM i-2 DOWNTO 0 DO
      ADD 2^j AS STRING TO line

    JOIN elements of line into a single string
    PRINT the string
  END FOR
END
'''
height = int(input("Enter the height: "))

for i in range(1, height + 1):
    line = []

    for j in range(i):
        line.append(str(2 ** j))

    for j in range(i - 2, -1, -1):
        line.append(str(2 ** j))

    print("".join(line))
