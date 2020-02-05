# Authored by Alistair Clark - github:alistair-clark
# date: 2020-02-04
from test_script.test import test_stairs

# def stairs(N):
#     spaces = [' '*i for i in range(N)]
#     numbers = ['#'*i for i in range(1, N+1)]
#     return [i + j for i, j in zip(numbers, reversed(spaces))]

def stairs(N):
    return ['#'*i + ' '*(N - i) for i in range(1, N + 1)]

if __name__ == '__main__':
    test_stairs(stairs)