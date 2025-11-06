arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filtered_even = list(filter(lambda x: not (x & 1), arr))
print(filtered_even)  # Output: [2, 4, 6, 8, 10]

filtered_odd = list(filter(lambda x: x & 1, arr))
print(filtered_odd)   # Output: [1, 3, 5, 7, 9]

filtered_gt5 = list(filter(lambda x: x > 5, arr))
print(filtered_gt5)  # Output: [6, 7, 8, 9, 10]