"""
Scenario

There once was a hat. The hat contained no rabbit, but a list of five numbers: 1, 2, 3, 4, and 5.

Your task is to:
    - write a line of code that prompts the user to replace the middle number in the list with an integer number 
      entered by the user (Step 1)
    - write a line of code that removes the last element from the list (Step 2)
    - write a line of code that prints the length of the existing list (Step 3).
"""
hat_list = [1, 2, 3, 4, 5]
middle_number = int(input("Enter a number to replace the middle number of the list: "))
hat_list[2] = middle_number
del hat_list[-1]
print(len(hat_list))
print(hat_list)