# Task 01
# Find most frequent element in the list

lst = [4, 2, 3, 4, 4, 4, 5, 5, 5, 5]

print(max(set(lst),key=lst.count))
print(min(set(lst),key=lst.count))

