def prime_numbers(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    if len(factors)>2:
        print("Not a prime number")
    else: print("A True Prime Number")
    return factors
print(prime_numbers(89))