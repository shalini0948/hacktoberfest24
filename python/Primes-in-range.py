# This is a function to check if a number is prime or not...
def is_prime(n):
    if n <=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

#  this function prints the prime numbers in given range...
def print_primes_in_range(A, B):
    for i in range(A,B+1):
        if is_prime(i)==True:
            print(i,end=",")

print_primes_in_range(5,13)
# output = 5,7,11,13