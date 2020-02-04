from test_script.test import test_stairs

def stairs(num):
    return ['#'*(i+1)+' '*(num-(i+1)) for i in range(num)]

if __name__ == '__main__':
    test_stairs(stairs)