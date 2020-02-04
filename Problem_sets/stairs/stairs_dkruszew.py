# Derek, Kruszewski, 2020-02-04
# Github User: dkruszew
from test_script.test import test_stairs

def stairs(N):
    """
    Produces stairs array of size N
    """
    stairs = []
    for i in range(0,N):
        # step = ''.join([str(N)]*(i+1)) + ''.join([' ']*(N-i-1))
        step = '#'*(i+1) + ' '*(N-i-1)
        stairs.append(step)
    return stairs        
 
if __name__ == '__main__':
    test_stairs(stairs)
