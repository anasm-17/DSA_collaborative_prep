from test_script.test import test_fizzbuzz

"""

A classic Data Structures an algorithms problem, you are given an input array of integers from 1 to 100 (inclusive). 
You have to write a fizzbuzz function that takes in an input array and iterates over it. When your function receives 
a number that is a factor of 3 you should store 'Fizz' in the output array, if the number is a factor of 5 then you 
should store 'Buzz' in the output array. Additionally, if the number is a factor of both 3 and 5, you must store 
'FizzBuzz' in the output array. For all other cases, you must store the numbers as they are. Return the output array 
from your function.

"""



def jaybuzz(some_input):
    """ This function consumes a LIST of integers from 1 to 100 (inclusive) and produces a LIST with values
        corresponding to the following rules:

        For a number that is a factor of 3, output 'Fizz'
        For a number that is a factor of 5, output 'Buzz'
        For a number that is a factor of 3 and 5, output 'Fizzbuzz'
        For all other numbers return them as is

    Paramaters:
    some_input - A list

    Example:
    jaybuzz([1,2,3,5,15]) = [1,2,'Fizz', 'Buzz', 'Fizzbuzz']
    """
    result = []

    if len(some_input) == 0:
        return result

    for i in some_input:
        assert(type(i)== int), "Invalid input provided. Numbers must be integers"
        assert(1 <= i <= 100),"Invalid input provided. Function should consume an array of integers from 1 to 100 (inclusive)"

        if i % 15 == 0:
            result.append('FizzBuzz')
            continue
        
        elif i % 3 == 0:
            result.append('Fizz')
            continue

        elif i % 5 == 0:
            result.append('Buzz')
            continue

        else:
            result.append(i)
    
    return result
 
 
if __name__ == '__main__':
    test_fizzbuzz(jaybuzz)