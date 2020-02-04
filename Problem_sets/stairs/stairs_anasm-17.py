# Author: Anas Muhammad - github:anasm-17 
# date: 2020-02-03
from test_script.test import test_stairs

def steps(n):
    out_list = []
    
    for i in range(n):
        out = "#"*(i+1) + " "*(n-i-1)
        out_list.append(out)
    
    return out_list
 
 
if __name__ == '__main__':
    test_stairs(steps)

