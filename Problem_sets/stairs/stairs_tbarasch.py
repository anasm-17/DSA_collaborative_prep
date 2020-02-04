#Author: Tani Barasch

from test_script.test import test_stairs


def stairs(N):
    stairs_ = list()
    for i in range(1,N+1):
        symb = "#"*(i) 
        empty = " "*(N-i)
        stairs_.append(symb + empty)
    return stairs_


 
if __name__ == '__main__':
    test_stairs(stairs)
