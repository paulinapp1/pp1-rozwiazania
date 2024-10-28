def f(n):
    num_of_primes = []
    num = 2
    
    while len(num_of_primes) < n:
        isPrime = True  # Assume num is prime until proven otherwise
        
        # Check if num is divisible by any number from 2 to square root of num
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                isPrime = False
                break
        
        # If num is prime, add it to the list
        if isPrime:
            num_of_primes.append(num)
        
        num += 1  # Move to the next number
        
    return num_of_primes

print(f(5))
