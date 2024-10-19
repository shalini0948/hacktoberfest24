def generate_fibonacci(n_terms):
    fibonacci_sequence = []
    a, b = 0, 1
    
    for _ in range(n_terms):
        fibonacci_sequence.append(a)
        a, b = b, a + b  # Update values for the next iteration
    
    return fibonacci_sequence

def main():
    print("Fibonacci Sequence Generator")
    
    while True:
        user_input = input("Enter the number of terms to display (or 'exit' to quit): ")
        
        if user_input.lower() == 'exit':
            print("Exiting the program.")
            break
        
        if user_input.isdigit():
            n_terms = int(user_input)
            if n_terms <= 0:
                print("Please enter a positive integer.")
                continue
            
            fibonacci_sequence = generate_fibonacci(n_terms)
            print(f"Fibonacci sequence up to {n_terms} terms: {fibonacci_sequence}")
        else:
            print("Invalid input. Please enter a valid positive integer.")

if __name__ == "__main__":
    main()
