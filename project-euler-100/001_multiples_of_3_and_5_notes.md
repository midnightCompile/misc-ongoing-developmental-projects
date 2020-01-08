# Notes: 001 - Multiples of 3 and 5


## Problem
Find the sum of all the multiples of 3 or 5 below 1000.


## General Problem Solving Approach
Rather than trying to solve for the values required to complete the challenge, I was looking to take a programmatic approach so any two inputs could be used to test their multiples over a range starting at 0 and ending at a value specified with a third input. 

At a glance, this problem is immediately recognizable as something that could be solved with some kind of loop logic. Pursuing that route could be cumbersome, also the best time complexity we could achieve would be something in the neighborhood of O(n) since the function would be looping over an interval of n length.

Instead, the mathematical formula for the summation of n natural numbers over an inteval could be utilized to improve efficiency. Basically, this allows for the summation of a series of natural numbers (positive integers) using the formula:
   Sum = 1 + 2 + .. + n = n*(n+1)/2

For multiples of a natural number, the same formula can be applied. However, the total number of multiples over the series must be acounted for. This leads to the formula:
   SumA = A + 2A + .. + nA = A * (m*(m+1)/2) ; m = n/A 

Furthermore, when we have two multiples over an interval, A and B, the same formula can be used to remove the overlapping multiples from the final sum. This can be done by plugging in A*B for the value of the multiple being tested over the variable. 

All in, by using the formula, the time complexity can be reduced to O(1) regardless of the interval size or the number of multiples that occur for each argument being tested over the interval.


## Notes About Solution Code
The above outlined formula was applied using one function to find the sum of multiples for a given input over a given range. This was called by a second function to get the sum of two different variables over a given range, and then subtract the value for their intersecting multiples.

With regards to the first function- floor division was used to ensure whole numbers were used throughout the calculations.

Although the code will return the sum of multiples for two different arguments, there are some limitations. For example, there isn't anything included to determine if the inputs are valid. Also, the this will test on an interval from 0 up to the endpoint that is provided to the function. There are was to make sure the endpoint isn't inclusive, but they weren't implemented.