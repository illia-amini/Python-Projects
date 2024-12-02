'''
amir5
ali7
reza15
mohsen8
mohammad10
write a code,that read the students name and mark *,based on the written num in front their name
'''
#code-01
students = [
    ("amir", 5),
    ("ali", 7),
    ('reza',15),
    ("mohsen", 8),
    ("mohameed", 10)
]

# Loop over each person in the list
for name, number in students:
    print(name, end=" ")  # Print the name without a newline #The end="" in the print() function ensures that the * symbols are printed on the same line.
    for star in range(number):  # Nested loop to print '*' based on the number
        print("*", end="")  # Print '*' on the same line
    print()  # Newline after each name and its stars
#code-02
names=['amir','ali','reza','mohsen','mohammad']
scores=[5,7,15,8,10]
for i,name in enumerate(names):#what enumarate does acctually it comes and find index or give a number to our each index of each list and match toghter
    print(name, "*"*scores[i])
#mind-of-king-,-hear-of-warrior
