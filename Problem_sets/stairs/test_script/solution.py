# Author: Anas Muhammad - github:anasm-17 
# date: 2020-02-03
def stairs(n):
    out_list = []
    
    for i in range(n):
        out = "#"*(i+1) + " "*(n-i-1)
        out_list.append(out)
    
    return out_list
 