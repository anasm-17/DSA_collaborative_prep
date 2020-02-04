# Derek, Kruszewski, 2020-02-02
# Github User: dkruszew
from test_script.test import test_fizzbuzz

def fizzbuzz(my_array):
    """
    Returns a fizzbuzz array
    """
    
    out_array = list()
    
    for i in my_array:
        if i%3 == 0:
            if i%5 == 0:
                out_array.append("FizzBuzz")
            else:
                out_array.append("Fizz")
        elif i%5 == 0:
            out_array.append("Buzz")
        else:
            out_array.append(i)
            
    return out_array

if __name__ == '__main__':
    test_fizzbuzz(fizzbuzz)
