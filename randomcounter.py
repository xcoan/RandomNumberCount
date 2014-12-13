#randomcounter.py
#displays 100 random numbers from 0 -> 100 and displays the number of times each number occurs in a dictionary
#programmed by xcoan

import random


def main():
    #variable to count the loop
    countVariable = 0
    # a list for random numbers to be placed into
    valuelist = []
    #
    while countVariable != 100:
        x = random.randint(0, 101)
        print(x)
        valuelist.append(x)
        #adds 1 to the countVariable, allowing the loop to terminate after 100 runs
        countVariable += 1

    #enables space on IDLE window
    for i in range( 0, 51):
        print(" ")

    #displays the number of times each number occures
    for i in range(0, 101):
        print( str(i) + " occurs " + str(valuelist.count(i)) + " times")


    
main()
