# 004 - Largest Palindrome Project
#
# Problem: Find the largest palindrome made from the product of two 3-digit numbers.
#
# For additional info regarding solution, see 004_largest_palindrome_project_notes.md

# Test for whether a number is palindromic
def palindrometest(n):
    return str(n) == str(n)[::-1]

# Empty list to contain palindromic products
palindromes = []

# Nested loops to calculate products of 3-digit numbers & add palindromic products to list
for first in range(999, 99, -1):
    for second in range(first, 99, -1):
        prod = (first*second)
        if palindrometest(prod):
            palindromes.append(prod)

# Using max() to find the largest palindromic product in the list
print(max(palindromes))