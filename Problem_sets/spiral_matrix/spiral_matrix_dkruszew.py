# Derek, Kruszewski, 2020-02-09
# Github User: dkruszew
from test_script.test import test_spiral_matrix

def spiral_matrix(N, my_list = None, my_int=1, dr="right", i = 0, j = 0):
    
    # make start matrix of zeros
    if my_list == None:
        my_list = [[0 for col in range(N)] for row in range(N)]

    my_list[i][j] = my_int
    
    # can we go right?
    if dr == "right" and j+1 < N and my_list[i][j+1] == 0:
        my_list = spiral_matrix(N, my_list, my_int+1, dr, i, j+1)
    else:
        dr = "down"
    
    # can we go down?
    if dr == "down" and i+1 < N and my_list[i+1][j] == 0:
        my_list = spiral_matrix(N, my_list, my_int+1, dr, i+1, j)
    else:
        dr = "left"
    
    # can we go left?
    if dr == "left" and j-1 >= 0 and my_list[i][j-1] == 0:
        my_list = spiral_matrix(N, my_list, my_int+1, dr, i, j-1)
    else:
        dr = "up"
        
    # can we go up?
    if dr == "up" and i-1 >= 0 and my_list[i-1][j] == 0:
        my_list = spiral_matrix(N, my_list, my_int+1, dr, i-1, j)
    
    # if can't go up and still not finished go right
    elif dr == "up" and j+1 < N and my_list[i][j+1] == 0 and max(list(map(max, my_list))) < N**2:
        dr = "right"
        my_list = spiral_matrix(N, my_list, my_int+1, dr, i, j+1)
        
    return my_list

if __name__ == '__main__':
    test_spiral_matrix(spiral_matrix)
