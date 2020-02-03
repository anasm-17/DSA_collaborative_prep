from test_script.test import test_fizzbuzz
import numpy as np

def fizzbuzz(my_array):
    """
    Returns a fizzbuzz array using vectorization
    """
    
    my_array = np.array(my_array, dtype=object)
    
    fizz = np.array(list(map(lambda x: 1 if x%3 == 0 else 0, my_array)))
    buzz = np.array(list(map(lambda x: 1 if x%5 == 0 else 0, my_array)))
    fizzbuzz = fizz*buzz
    
    my_array[fizz == 1] = "Fizz"
    my_array[buzz == 1] = "Buzz"
    my_array[fizzbuzz == 1] = "FizzBuzz"
    
    return list(my_array)

if __name__ == '__main__':
    test_fizzbuzz(fizzbuzz)