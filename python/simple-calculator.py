def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def main():
    print("Welcome to the Basic Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("Type 'exit' to quit the program.")

    while True:
        operation = input("\nEnter operation (1/2/3/4) (type q to exit): ")
        
        if operation.lower() == 'q':
            print("Exiting the program.")
            break
        
        if operation in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                if operation == '1':
                    result = add(num1, num2)
                    print(f"{num1} + {num2} = {result}")
                elif operation == '2':
                    result = subtract(num1, num2)
                    print(f"{num1} - {num2} = {result}")
                elif operation == '3':
                    result = multiply(num1, num2)
                    print(f"{num1} * {num2} = {result}")
                elif operation == '4':
                    result = divide(num1, num2)
                    print(f"{num1} / {num2} = {result}")

            except ValueError as e:
                print(f"Error: {e}. Please enter valid numbers.")
        else:
            print("Invalid operation. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
