#!/usr/bin/env python3

# Created By: Jessah
# Date: December 10, 2022
# This program ask the for four points and calculates
# the midpoint and distance using a create function


# function for midpoint
def midpoint(x_one, y_one, x_two, y_two):
    # calculate for x and y points
    x_point = (x_one + x_two) / 2
    y_point = (y_one + y_two) / 2
    # return midpoint
    return x_point, y_point


# function for midpoint
def distance(x_one, y_one, x_two, y_two):
    x_bracket = (x_two - x_one) ** 2
    y_bracket = (y_two - y_one) ** 2
    add = x_bracket + y_bracket
    square_root = add ** (1 / 2)
    # return distance
    return square_root


# main function
def main():
    # loop the program
    while True:
        # get input from user
        user_one_x = input("Enter a point for x1: ")
        user_one_y = input("Enter a point for y1: ")
        user_two_x = input("Enter a point for x2: ")
        user_two_y = input("Enter a point for y2: ")
        # catch any strings
        try:
            user_x_one = float(user_one_x)
            user_y_one = float(user_one_y)
            user_x_two = float(user_two_x)
            user_y_two = float(user_two_y)
        except (Exception):
            print(
                "Invalid, no strings allowed".format(
                    user_one_x, user_one_y, user_two_x, user_two_y
                )
            )
        else:
            # decision, if user wants distance or not
            decision = input("Do you also want the distance? (y,n): ")
            if decision == "Y" or decision == "y":  # when there is distance
                # call functions
                calc_midpoint = midpoint(user_x_one, user_y_one, user_x_two, user_y_two)
                calc_distance = distance(user_x_one, user_y_one, user_x_two, user_y_two)
                print("")
                # display midpoint and distance
                print("the midpoint is {}".format(calc_midpoint))
                print("the distance is {}".format(calc_distance))
            else:  # when there isn't a distance\
                # call function
                calc_midpoint = midpoint(user_x_one, user_y_one, user_x_two, user_y_two)
                print("")
                # display midpoint
                print("the midpoint is {}".format(calc_midpoint))
        print("")
        # asking the user if they want to play again
        print("Do you want to continue if not")
        play_again = input("press q to quit: ")
        if play_again == "q":
            print("Thanks for playing")
            break


if __name__ == "__main__":
    main()
