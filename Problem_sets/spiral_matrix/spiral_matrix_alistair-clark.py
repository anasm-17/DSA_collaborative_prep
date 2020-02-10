# Authored by Alistair Clark - github:alistair-clark
# date: February 9, 2020
from test_script.test import test_spiral_matrix

def spiral_matrix(N):
    nums = [i for i in reversed(range(1, N*N+1))]
    result = [[0 for i in range(N)] for i in range(N)]
    for a in range((N + 1)//2):
        i, j = a, a # set starting point
        for j in range(a, N): # fill top row
            result[i][j] = nums.pop()
        for i in range(a+1, N-1): # fill right column
            result[i][j] = nums.pop()
        i += 1
        if not nums: # for special case of N = 1
            return result
        for j in reversed(range(a, N)): # fill bottom row
            result[i][j] = nums.pop()
        for i in reversed(range(a+1, N-1)): # fill left column
            result[i][j] = nums.pop()
        N-=1
    return result
 
if __name__ == '__main__':
    test_spiral_matrix(spiral_matrix)