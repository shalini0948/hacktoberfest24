# What is Perfect number :- 
# A perfect number is a positive integer that is equal to the sum of its proper divisors (excluding itself).


# this function is for checking if a num is perfect num or not...
def check_prime(n):
    add = 0
    for i in range(1,(n//2)+1):
        if n%i == 0:
            add += i
    if add == n:
        return True
    else:
        return False

# this function prints the perfect num...
def print_perfect_numbers(a, b):
    for i in range(a,b+1):
        if check_prime(i)==True:
            print(i,end=" ")

print_perfect_numbers(1,100)