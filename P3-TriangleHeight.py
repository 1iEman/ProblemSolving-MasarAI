'''
Problem: 
Example:
- input --> 4 , Output : 1 2 4 8 4 2 1
- input -- > 5 , Output : 1 2 4 8 16 8 4 2 1
--------------------------------------
ALgorithm : 
1. Promote user to Input the height n.
2. Loop from level = 1 to h:

    Initialize list1 as an empty list (this will hold the left side + center value).

    Initialize list2 as an empty list (this will hold the right side: mirror of the left).

    Loop from i = 0 to level - 2:

        Append 2^i to list1.

    Append 2^(level - 1) to list1 (this is the center value).

    Loop from j = 2 to level:

        Append list1[-j] to list2 (mirror the left).

    Concatenate list1 and list2 into list3.

    Print the elements of list3.

---------------------------------------
Pseudocode: 
START
INPUT h

FOR level FROM 1 TO h DO
    INITIALIZE list1 as empty list
    INITIALIZE list2 as empty list

    FOR i FROM 0 TO level - 2 DO
        APPEND 2^i TO list1
    END FOR

    APPEND 2^(level - 1) TO list1

    FOR j FROM 2 TO level DO
        APPEND list1[-j] TO list2
    END FOR

    SET list3 = list1 CONCATENATED WITH list2

    PRINT elements of list3 space-separated
END FOR
END
'''

h = int(input("Enter Height: "))

for level in range(1, h + 1):
    list1 = [] # Left Side + centerd value
    list2 = [] # Right Side 

    for i in range(level - 1):
        list1.append(2 ** i)

    list1.append(2 ** (level - 1))  # Center value

    for j in range(2, level + 1):
        list2.append(list1[-j])

    list3 = list1 + list2 # Megre them
    print(*list3)


