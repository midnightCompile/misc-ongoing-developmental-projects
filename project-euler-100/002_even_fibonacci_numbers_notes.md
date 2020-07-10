# Notes: 002 - Even Fibonacci Numbers


## Problem
Find the sum of the even-valued terms in the Fibonacci sequence whose values are less than four million


## General Problem Solving Approach
Similar to the solution for problem 001, I wanted to create a solution that would allow the user define an endpoint so this calculation could be done for all even-valued terms in the Fibonacci sequence greater than zero but less than the endpoint provided by the user.

To achieve this, a function was created that accepted an endpoint value for an argument. An internal sum variable was initiated with the value of 0, and two other internal variables (fib1, fib2) were set with initial values of 0 and 1 (respectively) for the first two values in the calculation.

A while loop was used to check if the value of fib2 was less than the value of the endpoint argument, and as long as that condition remained true, an if statement would evaluate whether the current value was an even number. Even numbers were added to the value of the sum variable.

After each if conditional was checked, the fib1 and fib2 values were adjusted to allow the while loop to progress toward the endpoint. The value of fib1 was set to the value of fib2, and fib2's value was set to fib1 + fib2, allowing for the computer to progress along the Fibonacci series.

There are likely more efficient ways to solve this problem by using some more advanced mathmatical strategies, but I've not had the opportunity to research them yet.


## Notes About Solution Code
Although it's best to avoid nested loops when possible for the purposes of performance, I was unable to determine a more efficient way to solve the problem.

One thing I did differently in this excercise compared with the 001 problem solution was adding a main() function to the code. I wanted to expand my skills and Python knowledge, and wanted to be able to run the script from command line.

With regards to running the script from commandline, there are definitely other features that should have been implemented to validate and sanitize user input. For the time being, I have not added those features and intend to gradually add them to future solution code as I continue developing skills.