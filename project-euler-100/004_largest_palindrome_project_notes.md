# Notes: 004 - Largest Palindrome Problem


## Problem
Find the largest palindrome made from the product of two 3-digit numbers.

## General Problem Solving Approach
Just like a word, a palindromic number reads the same the both ways, forwards and backwards. In this exercise, we're asked to find the largest palindromic number based on the products of two 3-digit numbers.

The first step taken was to create a test to determine if a number was indeed palindromic. This was achieved by defining a function that converts an input value to a string, then uses the Python equal operator to compare if the string is equivalent to the same input reversed (string slicing is used to reverse the input after converting it to a string). This function returns a boolean true/false value based on the outcome of comparison.

After creating the above function, an empty list was created to hold the palindromic products to be calculated.

Knowing that the products of interest are from two 3-digit numbers, a nested for loop was set up with the outer loop counting down by 1 from 999 to 99. Each increment of this outer loop multiplied the current incremental number (first) by another incremental number (second) determined by a nested, inner for loop.

The inner for loop would start at the current increment of the outer loop, and decrement by 1 until reaching 99 before exiting and returning to the outer loop.

During each step of the inner loop, the product of the outer loop and inner loop numbers ould be calculated and that product would be tested using the palindrometest() function defined above in the code. Products returning a true value were then appended to the palindromes[] list before the inner loop would decrement.

The inner loop was set up so that each iteration would start at the current value of the outer loop's increment value so as to avoid duplicate calculations and duplicate values being appended to the palindromes[] list.

After all values were calculated, the max() method was utiltized to determine the greatest palindromic number appended to the palindromes[] list, and printed to the console.