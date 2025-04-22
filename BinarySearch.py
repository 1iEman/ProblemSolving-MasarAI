

# Binary Search
values = [3,4,5,7,100,900]
low = 0
high = len(values) - 1
mid = 0
x = 100
while low <= high:

    mid = (high + low) // 2

    # If x is greater, ignore left half
    if values[mid] < x:
        low = mid + 1

    # If x is smaller, ignore right half
    elif values[mid] > x:
        high = mid - 1

    # means x is present at mid
    else:
        print("Element is found at position: ", mid)
        break

# -------------------------------------------------------------------------------------------------

