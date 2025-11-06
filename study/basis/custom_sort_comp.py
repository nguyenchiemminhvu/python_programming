from functools import cmp_to_key

def custom_compare(x:int, y:int) -> int:
    if str(x) + str(y) > str(y) + str(x):
        return -1 # mean x should come before y
    elif str(x) + str(y) < str(y) + str(x):
        return 1  # mean y should come before x
    else:
        return 0  # mean they are equal in terms of ordering 

arr = [5, 2, 9, 1, 5, 6]
arr.sort(key=cmp_to_key(custom_compare))
print(arr)
print("".join(map(str, arr)))