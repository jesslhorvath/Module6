"""
Program: inner_functions_assignment.py
Author: Jessie Horvath
Last date modified: 02/26/2022

The purpose of this program is to create a function that takes a list.
Within the function are two inner functions that calculate the area
and perimeter of a quadrilateral shape. The outer function returns a string
with the calculated perimeter and area.
"""

def measurements(a_list):
    list_len = len(a_list)
    def area(a_list):
        if list_len < 2:
            area_value = a_list[0] * a_list[0]
        else:
            area_value = a_list[0] * a_list[1]
        return area_value

    def perimeter(a_list):
        if list_len < 2:
            perimeter_value = 4 * a_list[0]
        else:
            perimeter_value = (2 * a_list[0]) + (2 * a_list[1])
        return perimeter_value

    area_string = str(area(a_list))
    perimeter_string = str(perimeter(a_list))
    display_string = "Perimeter = " + perimeter_string + " Area = " + area_string
    return display_string

if __name__ == '__main__':
    rectangle = [2.1, 3.4]
    result = measurements(rectangle)
    print(result)

    square = [3.5]
    result2 = measurements(square)
    print(result2)