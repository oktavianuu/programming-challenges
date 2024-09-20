# Using counter variable to exit loops
import time

counter = int(input("Enter how many numbers u want me to do the loop: "))
while counter != 0:
    time.sleep(0.5) # delay looping for 0.5 seconds
    print("inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)