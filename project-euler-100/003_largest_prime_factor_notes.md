# Notes: 003 - Largest Prime Factor


## Problem
Find the largest prime factor of the number 600851475143


## General Problem Solving Approach
Sticking to the theme of earlier problems, I wanted to develop a solution that would allow me to find the largest prime factor of any positive integer provided by the user.

To achieve this, a function was created that would take an argument and return a list of the argument's prime factors. After returning the list, when the script was run, main() would utilize python's built in max() function to find the largest value from the list of primes.

After further research, it appears there are a number of other algorithms that could be utilized to enhance performance when searching for the greatest prime factor of much larger numbers than the one used in this challenge. However, those methods would be more complex to implement (and beyond my current, limited understanding of them)


## Notes About Solution Code
The function prime_factors() takes a positive integer argument and works to create a list of its prime factors. An empty list (factors) is created before the while loop begins. As long as the argument provided is >1, the while loop will cycle through potential factors.

Prior to the loop beginning, the variable d is initialized with a value of 2, and gets used as a divisor by a nested while loop after the initial loop begins. The nested while loop checks to see if the argument passed to prime_factors is divisable by d. If it is, then d is added to the factors list and the argument n's value is set to n /= d.

Before the initial while loop restarts, the value of d is incremented by 1 and nested conditional statements are used to check the value of d*d against n, and to confirm n > 1. This check is done to determine if any larger factors might be found with subsequent while loop executions. If both conditions are met, the loop will break.

The nested conditional statements added prior to the function returning the list factors was added as a means to improve performance of the function. This check should help the algorithmic efficiency approach O(sqrt(n)).

After defining the function prime_factors(), the built in Python function max() is utilized when running main() to return the largest prime factor in the list returned by prime_factors().