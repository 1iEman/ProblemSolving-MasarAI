

"""
ALgorithm Steps:

Input house boundaries:
 - Ask the user to enter two integers s and t — the start and end positions of the house.

Input tree locations:
 - Ask the user to enter two integers locationA and locationB — the positions of the apple tree and orange tree.

Input apple distances:
 - Ask the user to enter a list of integers representing the distances apples fell from the apple tree.

Input orange distances:
 - Ask the user to enter a list of integers representing the distances oranges fell from the orange tree.

Initialize apple counter to 0.

For each apple distance:

    - Calculate its final landing position: apple + locationA.

    - If it lands within the house range [s, t], increment the apple counter.

Initialize orange counter to 0.

For each orange distance:

    - Calculate its final landing position: orange + locationB.

    - If it lands within the house range [s, t], increment the orange counter.

Output:

    - Print the number of apples that fell on the house.

    - Print the number of oranges that fell on the house.
"""


s, t = map(int, input("Enter s and t of home: ").split())
locationA , locationB =map(int, input("Enter location apple tree then orange tree: ").split())
locationAppleFalls = list(map(int, input("Enter apples fall: ").split()))
locationOrangeFalls = list(map(int, input("Enter orange fall: ").split()))
countApple = 0
for apple in locationAppleFalls:
    if s <= (apple + locationA) <= t:
        countApple+=1

countOrange = 0
for orange in locationOrangeFalls:
    if s <= (orange +locationB) <= t:
        countOrange+=1
   
print(countApple , "Apple" )
print(countOrange , "Orange" )

