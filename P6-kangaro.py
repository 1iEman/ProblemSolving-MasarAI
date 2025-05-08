"""
Algorithm Steps:

- Promote user to input the initial positions and jump distances for two kangaroos (k1p, k1v, k2p, k2v).

- Initialize a flag as False to track if the kangaroos meet.

- Repeat up to 500 times:

    Add the jump distance to each kangaroo’s position.

    Check if both kangaroos are at the same position:

        If yes, set the flag to True and exit the loop.

- After the loop, check the flag:

    If it's True, print "Yes, kangaroos meet" and show the position.

    Otherwise, print "No", the kangaroos never meet.
"""

k1p,k1v,k2p, k2v = map(int, input("Enter position and unit jumps for each kangaro sequentially:  ").split())
flag = False
for i in range(0,500):
    k1p+=k1v
    k2p+=k2v
    if k1p == k2p:
        flag = True
        break

if flag:
    print("Yes kangaros meet in position " , k1p)
else:
    print("No")