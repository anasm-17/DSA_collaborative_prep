from test_script.test import test_fizzbuzz
import numpy as np

def fizzbuzz(my_array):
    """
    Returns a fizzbuzz array using vectorization
    """
    
    my_array = np.array(my_array, dtype=object)
    
    fizz = my_array%3 == 0
    buzz = my_array%5 == 0
    fizzbuzz = fizz*buzz
    
    my_array[fizz == 1] = "Fizz"
    my_array[buzz == 1] = "Buzz"
    my_array[fizzbuzz == 1] = "FizzBuzz"
    
    return list(my_array)

if __name__ == '__main__':
    test_fizzbuzz(fizzbuzz)
