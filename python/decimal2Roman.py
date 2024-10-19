def decimal_to_roman(num):
    if num <= 0 or num >= 4000:
        return "Number out of range (1-3999)"
    
    # Roman numeral mappings
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    
    roman_numeral = ""
    for i in range(len(val)):
        while num >= val[i]:
            roman_numeral += syms[i]
            num -= val[i]
    
    return roman_numeral

def main():
    print("Decimal to Roman Numeral Converter")
    
    while True:
        user_input = input("Enter a decimal number (1-3999) or 'exit' to quit: ")
        
        if user_input.lower() == 'exit':
            print("Exiting the program.")
            break
        
        if user_input.isdigit():
            num = int(user_input)
            if 1 <= num < 4000:
                roman_numeral = decimal_to_roman(num)
                print(f"The Roman numeral for {num} is: {roman_numeral}")
            else:
                print("Please enter a number between 1 and 3999.")
        else:
            print("Invalid input. Please enter a valid positive integer.")

if __name__ == "__main__":
    main()
