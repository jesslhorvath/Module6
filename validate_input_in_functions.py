"""
Program: validate_input_in_functions.py
Author: Jessie Horvath
Last date modified: 02/26/2022

The purpose of this program is to determine the validity of an entered test score.
The function determines if the score is valid in terms of in range and if
the value passed in is numeric. It then returns the test name and score if
valid, an error message if the score is numeric but not in range, or a ValueError 
if the score is not numeric.
"""

def score_input(test_name, test_score = -1, invalid_message="Invalid test score!"):
    try:
        test_score_int = int(test_score)
        if test_score_int > 100 or test_score_int < 0:
            return_string = "Test Name: " + test_name + ", " + invalid_message
            return return_string
    except ValueError:
        return "ValueError encountered!"
    else:
        string_score = str(test_score)
        return_string = "Test Name: " + test_name + ", Test Score: " + string_score
        return return_string

if __name__ == '__main__':
    run1 = score_input("Test 1", 70)
    print(run1)

    run2 = score_input("Test 1", -10)
    print(run2)

    run3 = score_input("Test 1", 105)
    print(run3)

    run4 = score_input("Test 1", "one hundred")
    print(run4)
