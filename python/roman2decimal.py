def roman_to_decimal(roman):
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    for char in reversed(roman):  # Process from right to left
        value = roman_numerals.get(char, 0)
        
        if value < prev_value:
            total -= value  # Subtract if the current value is less than the previous value
        else:
            total += value  # Add otherwise
        
        prev_value = value  # Update the previous value
    
    return total

def main():
    print("Roman to Decimal Converter")
    
    while True:
        user_input = input("Enter a Roman numeral (or 'exit' to quit): ").upper()
        
        if user_input.lower() == 'exit':
            print("Exiting the program.")
            break
        
        # Validate Roman numeral
        if all(char in "IVXLCDM" for char in user_input):
            decimal_value = roman_to_decimal(user_input)
            print(f"The decimal value for {user_input} is: {decimal_value}")
        else:
            print("Invalid input. Please enter a valid Roman numeral.")

if __name__ == "__main__":
    main()
