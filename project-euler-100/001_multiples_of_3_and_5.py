# 001 - Multiples of 3 and 5
#
# Problem: Find the sum of all the multiples of 3 or 5 below 1000.
#
# For additional info regarding solution, see 001notes.txt


# Calculates sum of multiples for input variable from 0 to endpoint.
def sum_multiples(n, end):

    # Number of multiples in interval
    m = end // n

    # Sum of first m natural numbers
    sum = m * (m + 1) / 2

    # Returning total sum for all natural numbers
    return n * sum


# Calculates sum of multiples for two different variables on an interval.
def sum_of_two_multiples(a, b, N):

    return sum_multiples(a, N) + sum_multiples(b, N) - sum_multiples(a*b, N)


# Driver
a = 3
b = 5
N = 999
print(sum_of_two_multiples(a, b, N))