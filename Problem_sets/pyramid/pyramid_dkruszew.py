# Derek, Kruszewski, 2020-02-04
# Github User: dkruszew
from test_script.test import test_pyramid

def pyramid(N):
    """
    Produces pyramid array of size N
    """
    pyramid = []
    for i in range(0,N):
        block = ('#'*(2*i+1)).join([' '*(N-i-1)]*(2))
        pyramid.append(block)
    return pyramid      

if __name__ == '__main__':
    test_pyramid(pyramid)