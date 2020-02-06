#Author: Tani Barasch

from test_script.test import test_pyramid


def pyramid(N):
    lvl = list()
    for i in range(N):
        temp = ' '*(N-i-1) + '#'*(1+2*i) + ' '*(N-i-1)
        lvl.append(temp)
    return lvl


 
if __name__ == '__main__':
    test_pyramid(pyramid)
