'''
write a code,
to calc average of num,unlimited,
if user enter a str var,
it ignores and continue,
via func.

'''
def calculate_average():
    numbers = []
    print("Enter numbers to calculate the average. Type 'done' to finish.")
    
    while True:
        user_input = input("Enter a number: ")
        
        if user_input.lower() == 'done':
            break
        
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input. Only numerical values are considered.")
            continue

    if numbers:
        average = sum(numbers) / len(numbers)
        print(f"The average of the numbers is: {average}")
    else:
        print("No valid numbers were entered.")

calculate_average()