import array

def test_array_creation():
    # Test creation of an array with integers
    arr = array.array('i', [1, 2, 3, 4, 5])
    assert arr[0] == 1
    assert arr[1] == 2
    assert arr[2] == 3
    assert arr[3] == 4
    assert arr[4] == 5

def test_array_append():
    # Test appending elements to an array
    arr = array.array('i', [1, 2, 3])
    arr.append(4)
    assert arr[-1] == 4
    arr.append(5)
    assert arr[-1] == 5

def test_array_insert():
    # Test inserting elements at specific positions
    arr = array.array('i', [1, 2, 3])
    arr.insert(1, 10)  # Insert 10 at index 1
    assert arr[1] == 10
    assert arr[2] == 2

def test_array_remove():
    # Test removing elements from an array
    arr = array.array('i', [1, 2, 3, 4, 5])
    arr.remove(3)  # Remove the first occurrence of 3
    assert 3 not in arr
    assert len(arr) == 4

def test_array_pop():
    # Test popping elements from an array
    arr = array.array('i', [1, 2, 3, 4, 5])
    popped_value = arr.pop()  # Pop the last element
    assert popped_value == 5
    assert len(arr) == 4
    assert arr[-1] == 4

def test_array_index():
    # Test finding the index of an element
    arr = array.array('i', [1, 2, 3, 4, 5])
    index = arr.index(3)
    assert index == 2
    try:
        arr.index(10)  # This should raise a ValueError
    except ValueError:
        pass
    else:
        assert False, "ValueError not raised for non-existent element"
    arr.append(3)  # Add another 3 to test multiple occurrences
    index = arr.index(3)
    assert index == 2  # Should return the index of the first occurrence
    index = arr.index(3, 3)  # Start searching from index 3
    assert index == 5  # Should return the index of the second occurrence

def test_array_slice():
    # Test slicing an array
    arr = array.array('i', [1, 2, 3, 4, 5])
    sliced_arr = arr[1:4]  # Slice from index 1 to 3
    assert sliced_arr.tolist() == [2, 3, 4]
    sliced_arr = arr[:3]  # Slice from start to index 2
    assert sliced_arr.tolist() == [1, 2, 3]
    sliced_arr = arr[2:]  # Slice from index 2 to end
    assert sliced_arr.tolist() == [3, 4, 5]
    sliced_arr = arr[:]  # Slice the entire array
    assert sliced_arr.tolist() == [1, 2, 3, 4, 5]
    sliced_arr = arr[::2]  # Slice with step of 2
    assert sliced_arr.tolist() == [1, 3, 5]
    sliced_arr = arr[1::2]  # Slice with step of 2 starting
    assert sliced_arr.tolist() == [2, 4]
    sliced_arr = arr[::-1]  # Reverse the array
    assert sliced_arr.tolist() == [5, 4, 3, 2, 1]
    sliced_arr = arr[3:1:-1]  # Reverse slice from index 3 to 2
    assert sliced_arr.tolist() == [4, 3]

def test_array_extend():
    # Test extending an array with another array
    arr1 = array.array('i', [1, 2, 3])
    arr2 = array.array('i', [4, 5, 6])
    arr1.extend(arr2)
    assert arr1.tolist() == [1, 2, 3, 4, 5, 6]
    arr1.extend([7, 8])  # Extend with a list
    assert arr1.tolist() == [1, 2, 3, 4, 5, 6, 7, 8]
    arr1.extend((9, 10))  # Extend with a tuple
    assert arr1.tolist() == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    arr1.extend(array.array('i', [11, 12]))  # Extend with another array
    assert arr1.tolist() == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def test_array_reverse():
    # Test reversing an array
    arr = array.array('i', [1, 2, 3, 4, 5])
    arr.reverse()
    assert arr.tolist() == [5, 4, 3, 2, 1]
    arr.reverse()  # Reverse again to get original order
    assert arr.tolist() == [1, 2, 3, 4, 5]
    arr = array.array('i', [1])  # Test reversing a single-element array
    arr.reverse()
    assert arr.tolist() == [1]
    arr = array.array('i', [])  # Test reversing an empty array
    arr.reverse()
    assert arr.tolist() == []

def test_array_count():
    # Test counting occurrences of an element
    arr = array.array('i', [1, 2, 3, 2, 4, 2, 5])
    count_2 = arr.count(2)
    assert count_2 == 3
    count_3 = arr.count(3)
    assert count_3 == 1
    count_10 = arr.count(10)  # Element not in array
    assert count_10 == 0

if __name__ == "__main__":
    test_array_creation()
    test_array_append()
    test_array_insert()
    test_array_remove()
    test_array_pop()
    test_array_index()
    test_array_slice()
    test_array_extend()
    test_array_reverse()
    test_array_count()
    print("All tests passed.")