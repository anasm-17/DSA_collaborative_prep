# Authored by Roc Zhang - github:Zhang-Haipeng - email:roc_zhang@hotmail.com
# date: 2020-02-08
from test_script.test import test_spiral_matrix

def yoursolutionfunc(n):
#  --- Your solution ---
    x = [[0 for x in range(n)] for y in range(n)] # initalize x

    stop = n**2
    m  = 1 # the 12345678...stop 
    r = 0 # round

    # fill in the numbers brutally
    while m <= stop:
        # go right
        for i in range(r, n-r):
            x[r][i] = m
            m+=1
        # go down
        for i in range(r+1, n-r):
            x[i][n-r-1] = m
            m+=1
        # go left
        for i in range(n-r-2, r-1, -1):
            x[n-r-1][i] = m
            m+=1
        # go up
        for i in range(n-r-2, r, -1):
            x[i][r] = m
            m+=1
        # next round
        r+=1
    return x
 
if __name__ == '__main__':
    test_spiral_matrix(yoursolutionfunc)