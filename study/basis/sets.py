s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
print(s1 | s2)  # Union of s1 and s2
print(s1 & s2)  # Intersection of s1 and s2
print(s1 - s2)  # Difference of s1 and s2
print(s1 ^ s2)  # Symmetric difference of s1 and s2
print((s1 | s2) - (s1 & s2))  # Union minus intersection

s = {x for x in range(10) if x in {1, 2, 3, 4, 5}}
print(s)

s.remove(1)  # Remove element 1 from the set
print(s)

print(s1 > s2)  # Check if s1 is a superset of s2
print(s1 < s2)  # Check if s1 is a subset of s2
print(s1 == s2)  # Check if s1 and s2 are equal
print(s1 != s2)  # Check if s1 and s2 are not equal
print(s1.issubset(s2))  # Check if s1 is a subset of s2
print(s1.issuperset(s2))  # Check if s1 is a superset of s2
print(s1.isdisjoint(s2))  # Check if s1 and s2 are disjoint sets
