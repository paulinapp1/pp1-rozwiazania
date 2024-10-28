def f(n):
    primes = []
    num = 2
    while len(primes) < n:
        isPrime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:  # Changed from "&" to "%"
                isPrime = False
                break
        if isPrime:
            primes.append(num)
        num += 1
    return primes[-1]
print(f(5))