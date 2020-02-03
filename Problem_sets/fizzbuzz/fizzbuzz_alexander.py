from test_script.test import test_fizzbuzz

def fizzy(in_list):
 """
 Cheeky one-liner solution 
 """
        return ["FizzBuzz" if i%3==0 and i%5==0 else "Fizz" if i%3==0 else "Buzz" if i%5==0 else i for i in in_list]
    
if __name__ == '__main__':
    test_fizzbuzz(fizzy)