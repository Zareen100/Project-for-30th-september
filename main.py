def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def two_digit_primes():
    primes = []
    for num in range(10, 100):  # Two-digit numbers range from 10 to 99
        if is_prime(num):
            primes.append(num)
    return primes

# Find and print all two-digit prime numbers
prime_numbers = two_digit_primes()
print("Two-digit prime numbers are:", prime_numbers)
