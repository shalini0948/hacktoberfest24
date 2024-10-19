def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."

# Input: Ask the user for a number
num = int(input("Enter a number: "))

# Output: Check if the number is even or odd
result = check_even_odd(num)
print(result)
