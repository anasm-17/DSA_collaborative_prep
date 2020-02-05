# Author: Alexander Hinton
# Pyramid problem
from test_script.test import test_pyramid

def pyramid(n):
    return [' '*(n-i)+'#'*(2*i-1)+(' '*(n-i)) for i in range(1,n+1)]

if __name__ == "__main__":
    test_pyramid(pyramid)