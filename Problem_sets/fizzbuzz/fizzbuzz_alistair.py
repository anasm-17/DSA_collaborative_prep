from test_script.test import test_fizzbuzz

def fizzbuzz(array):
    result = []
    for i in array:
        x = ''
        if i % 3 == 0:
            x += 'Fizz'
        if i % 5 == 0:
            x += 'Buzz'
        if not x:
            x = i
        result.append(x)
    return result

if __name__ == '__main__':
    test_fizzbuzz(fizzbuzz)