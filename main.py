#!/usr/bin/env python3

# Created by: Daniel Pawelko
# Created on: Nov 2021
# Adding Loop


def main():
    # main function for adding while loop

    # variables
    counter = 0
    sum_num = 0

    # asking for input
    number = input("Enter a positive integer: ")
    number = int(number)

    # process
    while counter < number:
        counter += 1
        sum_num += counter

    # output
    print(f"The sum of all positive numbers from 1 to {number} is {sum_num}.")

    # done
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
