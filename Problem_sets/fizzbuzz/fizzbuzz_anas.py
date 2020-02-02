# Authored by A. Muhammad - github: anasm-17 - anas.m.017@gmail.com
# date: 2020-02-01
from test_script.test import test_fizzbuzz

def fizzbuzz(int_list):
    out_list = []
    for i in int_list:
        output = ""
        if i%3 == 0:
            output+="Fizz"
        if i%5 == 0:
            output+="Buzz"
        if output:
            out_list.append(output)
        else:
            out_list.append(i)
    
    return out_list

if __name__ == '__main__':
    test_fizzbuzz(fizzbuzz)