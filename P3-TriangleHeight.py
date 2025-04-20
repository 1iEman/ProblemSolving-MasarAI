'''
Problem: 
Example:
- input --> 4 , Output : 1 2 4 8 4 2 1
- input -- > 5 , Output : 1 2 4 8 16 8 4 2 1
--------------------------------------
ALgorithm : 
1. Promote user to Input the height n.

2. Initialize an empty list list1 to hold the left side and center value.

3. Initialize an empty list list2 to hold the right side (a mirror of the left side).

4. Loop from i = 0 to height - 2:

        Append 2^i to list1.

5. Append 2 * last element of list1 to list1 (this is the center value).

6. Loop from j = 2 to height:

        Append the -jth element of list1 to list2.

7. Merge list1 and list2 to create final list3.

8. Print list3.
---------------------------------------
Pseudocode: 

START
INPUT h
INITIALIZE list1 as empty list
INITIALIZE list2 as empty list

FOR i FROM 0 TO h - 2 DO
    list1.APPEND(2 TO THE POWER OF i)
END FOR

list1.APPEND(last element of list1 TIMES 2)

FOR j FROM 2 TO h DO
    list2.APPEND(list1[-j])
END FOR

list3 = CONCATENATE list1 AND list2

PRINT list3

END
'''

h = int(input(" Enter Height: "))

list1 = [] # Left Side + Centerd value
list2 = [] # Right Side (Mirror of Left Side)

for i in range(h - 1):
    list1.append(2**i)
    
list1.append(list1[-1] * 2)  # Centerd Value


for j in range(2, h + 1):
    list2.append(list1[-j])
    
list3 = list1 + list2   # Merge them
print(list3)

