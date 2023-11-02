# Problem2:
# Create a function that takes a list of numbers and returns a new list containing 
# only the prime numbers from the original list.

def prime_numbers(list):
    prime = []
    for i in list:
        if i < 2:
            continue
        count = 0
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                count += 1
        if count == 0:  
            prime.append(i)
    return prime

x = [5,8,11,18,23,28,31,36,37]
print(prime_numbers(x))

# Method2:
def prime_numbers(lst):
    primes = []
    for i in lst:
        if i < 2:
            continue
        is_prime = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes

x = [5, 8, 11, 18, 23, 28, 31, 36, 37]
print(prime_numbers(x))
