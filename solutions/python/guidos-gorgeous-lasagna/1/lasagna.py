"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO (student): define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.
EXPECTED_BAKE_TIME = 40 
print(EXPECTED_BAKE_TIME)
PREPARATION_TIME = 30
print(PREPARATION_TIME)

#TODO (student): Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.
    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.
    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.
    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    REMAINING_TIME = EXPECTED_BAKE_TIME-elapsed_bake_time
    return REMAINING_TIME
    
bake_time_remaining(30)


#TODO (student): Define the 'preparation_time_in_minutes()' function below.
# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.
def preparation_time_in_minutes(number_of_layers):
    """Calculate the preperation time in minutes
    Parameters: number_of_layers(int) : the amount of lasgana sheets used
    Returns:
    int: multiples number_of_layers by 2 since it assumes 2 mins is taken by one sheet
    and returns the total time taken"""
    total = number_of_layers*2
    return total 
preparation_time_in_minutes(2)
#TODO (student): define the 'elapsed_time_in_minutes()' function below.

def elapsed_time_in_minutes(number_of_layers,elapsed_bake_time):
    """Calculate the elapsed time in minutes
    Parameters: number of layers and elapsed bake time
    Returns: a int by multipying number_of_layers by 2 and adding it to elapsed bake time
    to return total time"""
    total = (number_of_layers*2)+elapsed_bake_time
    return total
    
elapsed_time_in_minutes(3,20)
# TODO (student): Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
