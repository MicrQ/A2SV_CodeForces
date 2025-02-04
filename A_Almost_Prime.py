""" Almost prime: codeforces """
def is_prime(n: int):
    """ a function that checks if a number is prime """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    i = 3
    while (i ** 2) <= n:
        if n % i == 0:
            return False
        i += 2

    return True

n = int(input())

# all prime numbers form 1 - n
primes = [num for num in range(n + 1) if is_prime(num)]
almost_primes = 0

for num in range(1, n + 1):
    prime_divisors = 0
    for prime in primes:
        if num % prime == 0:
            prime_divisors += 1

    if prime_divisors == 2:
        almost_primes += 1
    
print(almost_primes)
