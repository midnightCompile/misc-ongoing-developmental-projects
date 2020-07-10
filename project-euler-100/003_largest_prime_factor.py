# 003 - Largest Prime Factor
#
# Problem: What is the largest prime factor of the number 600851475143?
#
# For additional info regarding solution, see 003_largest_prime_factor_notes.md


# Function to find all primes for a positive integer
def prime_factors(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d += 1
        if d*d > n:
            if n > 1: factors.append(n)
            break
    return factors



# Main function prompting user to provide positive integer to receive largest prime
def main():
    num = int(input("Provide a positive integer to determine its largest prime factor: "))
    primes = prime_factors(num)
    largest_prime = max(primes)
    print("The largest prime factor of %s is the number %s" % (num, largest_prime))

if __name__ == "__main__":
    main()

