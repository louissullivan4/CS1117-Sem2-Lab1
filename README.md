# Y1-Sem2-Lab1
1. Pass 3 numbers to a function called three_numbers(number_1, number_2, number_3). If all the numbers are the same return True, 
otherwise return False.  Example of what is returned by the function call is shown: 
a. three_numbers(3, 3, 3)  -> True (This is the boolean True and not the string "True") 
b. three_numbers(3, 2, 3) -> False 
c. three_numbers(3, "a", 3) -> False 
 
2. Write a function called seasons(), that has a parameter called number.  Depending on the number passed to the function, 
the function will return the corresponding season of the year where 1=Winter, 2=Spring, 3=Summer, and 4 = Autumn. 
Within this function, define a list or dictionary of the seasons, and select the season based on the input value 
where 1=Winter, 2=Spring, 3=Summer, and 4=Autumn.  Remember list indexing begins at 0.  Add code to return an error message 
if any other number is entered, so examples below (make sure the error message is identical to below): 
a. seasons(1) -> "Winter" 
b. seasons(5) -> 'Number entered, 5, is outside of input values' 
c. seasons('a') -> 'Input value must be a number' 
 
3. The letter corresponding to a numerical grade percentage is shown below. Pass a number to a function called grades(), 
which will return the corresponding grade letter. If the user enters a value outside of 0-100 the grade should return ‘X’.   
f a user enters a non-number, return an error message 'Input value must be a number' The function will also take a Letter 
Grade and should return the Numerical Grade range.  Example of what is returned by the 
function call is shown:   grades(86) -> "A" (the string A is returned) grades("A") -> "85-100" 
(the string 85-100 is returned)   grades(110) -> "The input numerical grade is outside the range supported"   
grades("H") -> "The input letter grade is outside the range supported" Update error message handling 
in the new function to handle the different inputs. 
 
4. This question examines string slicing. Write a function, slice_reverse(input_value), which determine if the input_value 
parameter is a palindrome i.e. reads the same backwards as forwards. The program should return True or False depending on the input.
Do not use the Python reverse() function. Examples: 
a. 12321 returns True (This is the boolean True and not the string "True") 
b. [1, 2, 3, 2, 1] returns True 
c. “rotavator” returns True 
d. ("r","o","t","a","v","a","t","o","r”) returns True 
e. “ ” (space) returns True 
f. “abcdba” returns False 
 
5. I want you to create a function called add_to_list(value, list), which will return a sorted list.  The function 
will add value to the list if the list does not already contain the value e.g.,  a. add_to_list(5, [1,3,7,9]) 
returns [1,3,5,7,9]  b. add_to_list("c", ["a","b","d","e"]) returns ["a","b","c","d","e"]  c. add_to_list(5, [1,3,5,7,9]) 
returns [1,3,5,7,9]
