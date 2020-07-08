# 002 - Even Fibonacci Numbers
#
# Problem: Find the sum of the even-valued terms in the Fibonacci sequence
# whose values are less than four million
#
# For additional info regarding solution, see 002_even_fibonacci_numbers_notes.md



def sum_fib_evens(endpoint):
    sum = 0
    fib1, fib2 = 0, 1
    while fib2 < endpoint:
        if fib2 % 2 == 0:
            sum += fib2
        fib1, fib2 = fib2, fib1 + fib2
    return sum

def main():
    print("The even numbers in the Fibonacci sequence between 0 and your limit will be summed.")
    limit = int(input('Please provide a positive integer as a limit: '))
    evensum = sum_fib_evens(limit)
    print('The sum of even numbers in the Fibonacci sequence between 0 and %s is %s.' % (limit, evensum))

if __name__ == "__main__":
    main()