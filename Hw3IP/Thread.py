# Jason Wein
# Internet Programming
# 20 February 2019

import threading
import time
from os import system,name
import random

# Create an array and set its values to random integers between 1 and 20.
array = []
for j in range(5):
    array.append(random.randint(1, 20))

# Set values for system.
T1 = 45
T2 = 5
Tmin = 12
Tmax = 30
tsec = 0
# Print the starting array.
print(array, "After one second we have: ")


# Define clear class that will clear the screen in the console.
def clear():
    if name == 'nt':
        _= system('cls')
    else:
        _= system('clear')


# Clear the starting array.
clear()


class MyThread1(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self, name="MyThread")

    def run(self):
        global tsec
        # Will run the thread while the time is less than or equal to T1.
        while True and tsec <= T1:
            # If the value of the array at index 0 is greater than 0, it will remove 1 from it and print the array.
            if(array[0] > 0):
                array[0] -= 1
            # If the value of the array at index 0 is 0, it will remove this from the array.
            elif array[0] == 0:
                array.pop(0)
            # Prints the array after every iteration.
            print(array, "After one second we have: ")
            tsec += 1
            time.sleep(1)
            clear()


# Second Thread that will add a value to the array if the length of the array is less than 5.
class MyThread2(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self, name="MyThread")

    def run(self):
        while True:
            # If the sequence is less than 5, it will add a value to the array.
            if(len(array) < 5):
                array.append(random.randint(Tmin,Tmax))
            time.sleep(T2)


# Create both threads and start both.
thread1 = MyThread1()
thread1.start()

thread2 = MyThread2()
thread2.start()




