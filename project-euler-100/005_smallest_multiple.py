# 005 - Smallest Multiple
#
# Problem: Find the smalest positive number that is evenly divisible
# by all of the numbers from 1 to 20.
#
# Program Variation: The solution was set up to find the smallest number
# evenly divisible by all of the numbers from 1 to n, with n being an int
# greater than 1 provided by the user. For additional info regarding
# solution, see 005_smallest_multiple_notes.md



# Function to find smallest multiple over range from 1 to n
def smallest_multiple(n):
    if (n <= 2):
        return n
    multiple = n * 2
    factors = []
    for number in range(n, 1, -1): 
       if number * 2 > n:
           factors.append(number)

    while True:
        for factor in factors:
            if multiple % factor != 0:
                multiple += n
                break
            if (factor == factors[-1] and multiple % factor == 0):
                return multiple


# Main function prompting user to provide integer input > 1
def main():
    num = 1
    print("")
    print("")
    print("")
    print("---------------------------------------------------------------")
    print("Welcome to the Smallest Multiple Finder!")
    print("")
    print("This program will provide the smallest positive number that can be divided by all of the numbers in a range from 1 to n.")
    print("---------------------------------------------------------------")
    while num < 2:
        print("")
        print("Please provide a positive integer greater than 1:")
        num = int(input(""))
        if num < 2:
            print("")
            print("Sorry, the input of %s will not work for this program." % (num))
        else:
            print("")
    multiple = smallest_multiple(num)
    print("---------------------------------------------------------------")
    print("%s is the smallest multiple evenly divisible by all numbers in the range of 1 to %s." % (multiple, num))
    print("")
    print("Cheers!")


if __name__ == "__main__":
    main()