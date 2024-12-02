'''
amir5
ali7
reza15
mohsen8
mohammad10
write a code,that read the students name and mark *,based on the written num in front their name
'''
students = [
    ("amir", 5),
    ("ali", 7),
    ('reza',15),
    ("mohsen", 8),
    ("mohameed", 10)
]

# Loop over each person in the list
for name, number in students:
    print(name, end=" ")  # Print the name without a newline
    for star in range(number):  # Nested loop to print '*' based on the number
        print("*", end="")  # Print '*' on the same line
    print()  # Newline after each name and its stars
#mind-of-king-,-hear-of-warrior
