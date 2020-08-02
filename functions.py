# ScriptName: functions.py
# Author: Louis Sullivan 119363083

def three_numbers(number_1, number_2, number_3):
    if number_1 == number_2 == number_3 and type(number_1) == int:
        return True
    return False


def seasons(number):
    if type(number) == int:
        if number == 1:
            return "Winter"
        elif number == 2:
            return "Spring"
        elif number == 3:
            return "Summer"
        elif number == 4:
            return "Autumn"
        return "Number entered, " + str(number) + ", is outside of input values"
    return "Input value must be a number"

def grades(number):
    if type(number) == int:
        if 85 <= number <= 100:
            return "A"
        elif 70 <= number <= 84:
            return "B"
        elif 55 <= number <= 69:
            return "C"
        elif 40 <= number <= 54:
            return "D"
        elif 25 <= number <= 39:
            return "E"
        elif 0 <= number <= 24:
            return "F"
        return "The input numerical grade is outside the range supported"
    return "The input letter grade is outside the range supported"


def slice_reverse(reversible):
    if type(reversible) == int or type(reversible) == float:
        reversible = str(reversible)
    if reversible == reversible[:: -1]:
        return True
    return False

def add_to_list(value, list):
    if value not in list:
        list.append(value)
    list.sort()
    return list
