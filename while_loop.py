# A program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd.
# The program terminates when zero is entered. 

odd_numbers = 0 
even_numbers = 0

# Read the first number
number = int(input("Enter a number or type 0 to stop: "))

# 0 terminates execution
while number != 0: # alternatively we can use `while number:` it is just equals to 'while number !=0:'
    # check if the number is odd
    if number % 2:
        # increase the odd numbers counter.
        odd_numbers += 1
    else:
        # increase the even numbers counter
        even_numbers += 1
    # Read the next number
    number = int(input("Enter a number or type 0 to stop: "))

# print results
print("Odd numbers count:", odd_numbers)
print("even numbers count:", even_numbers)