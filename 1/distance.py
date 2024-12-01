# Read the file and split the two columns into two lists
with open('numbers.txt', 'r') as file:
    column1 = []
    column2 = []
    for line in file:
        num1, num2 = line.split('   ')
        column1.append(int(num1))
        column2.append(int(num2))
# print("Column 1:", column1)
# print("Column 2:", column2)

# Sort each lists by increasing order
column1.sort()
column2.sort()
# print("Sorted Column 1:", column1)
# print("Sorted Column 2:", column2)

# Calculate distance between each pair of numbers
distances = []
for i in range(len(column1)):
    distances.append(abs(column2[i] - column1[i]))
# print("Distances:", distances)
# 
# # Sum all of the distances
sum = 0
for distance in distances:
    sum += distance

print("Sum of distances:", sum)