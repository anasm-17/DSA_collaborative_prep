# Author: Anas Muhammad - github: anasm-17
# date: 2020-02-03
from test_script.test import test_pyramid

def pyramids(n):
    pyr_list = list(" "*((2*n) - 1))
    out_list = []
    for i in range(n):
        pyr_list[(2*n - 1)//2 + i] = '#'
        pyr_list[(2*n - 1)//2 - i] = '#'
        out_list.append("".join(pyr_list))
    return out_list
 
if __name__ == '__main__':
    test_pyramid(pyramids)