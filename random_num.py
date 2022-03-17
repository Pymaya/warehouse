# a random integer generator
# author: KiteAB
# this program can help you fast generate the one & more random numbers

import random # the random module can create a or more random numbers
import sys # can exit the program and return the error code


# get the random numbers range
def num_range():
    # if user can't enter the correct number, then not jump out the loop
    while True:
        try:
            min = int(
                input("Please enter this random number(s) minimum value: ")
            ) # try get the minimum value and change it to an integer
        except ValueError:
            # if the enter value is not an integer, then continue the loop
            print("You can't enter float number or letters!\n")
            continue
        else:
            # if user enter the correct value then continue get the max value
            while True:
                try:
                    max = int(
                        input("Please enter this random number(s) max value: ")
                    ) # try get the max value and change it to an integer
                except ValueError:
                    print("You can't enter float number or letters!\n")
                    continue
                else:
                    break

        # if min >= max, then re-loop it
        if min >= max:
            print("The minimum number could not be greater than the maximum number.")
            continue

        break
    return min, max # return min & max values to num_quantity function


# get the numbers quantity
def num_quantity():
    # if user can't enter the correct number, then not jump out the loop
    while True:
        try:
            qty = input("Please enter this random numbers quantity (default 1): ")

            # if user direct press the "enter" key and doesn't type anythings, then set the default value is 1
            if qty == "":
                qty = "1"
            # change the "qty" variable's type to integer
            qty = int(qty)

            # if the quantity < 1, then re-loop it
            if qty < 1:
                print("You can't enter a number less than 1!\n")
                continue
        except ValueError:
            print("You can't enter float number or letters!\n")
            continue
        else:
            break
    return qty


# generate the random number
def num_generate():
    # copy the variable to this function
    min, max = num_range()
    qty = num_quantity()

    # generate random number
    print("\nThe random number(s) is:")
    # if qty is 1, then print 1 number
    if qty == 1:
        for i in range(0, qty):
            # use the get range to generate the random numbers
            num = random.randint(min, max)
            print(num, end="")
    # if qty > or < 1, then print "qty" numbers
    else:
        for i in range(0, qty):
            num = random.randint(min, max)
            # use "end" variable to make the num won't be lined up line by line
            print(num, end=" ")


# the main function
def main():
    print("Welcome to the random integer generator!\n")
    while True:
        num_generate()

        while True:
            # if user want regenerate the next set of numbers, then rerun the num_generate function
            next = input(
                "\n\nDo you want to regenerate the next set of numbers? (Y/n): "
            )
            # case and normal status support
            if next == "y" or next == "Y" or next == "":
                yes = True
                break
            elif next == "n" or next == "N":
                yes = False
                break
            else:
                print("Please enter y/n.")
                continue
        if yes == True:
            yes = False
            continue
        else:
            sys.exit(0)


# run the main function part
if __name__ == "__main__":
    main()