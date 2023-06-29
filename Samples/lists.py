# 1D list
names = ["John", "Bob", "Sarah", "Will"]

# First item
print(names[0])

# Final item
print(names[-1])

# Starting from Index 2 to the end
print(names[2:])

# Add to the end
names.append("Tom")

# Remove the final item
names.pop()

# Check the index
index = "Will" in names

# Insert
names.insert(2, "Charles")

# Remove
names.remove("Charles")

# Count the number of the specified item
names.count("Will")

# Sort the list
names.sort()
print(names)

# Copy the list
names2 = names.copy()

# Clear the list
names.clear()

print("\n--------------\n")

# 2D list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0])

row = 0
col = 1
print(matrix[row][col])
