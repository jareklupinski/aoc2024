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

# Get the "similarity score" between the two columns
similarity_score = 0
for num in column1:
    similarity_score += num * column2.count(num)
print(similarity_score)