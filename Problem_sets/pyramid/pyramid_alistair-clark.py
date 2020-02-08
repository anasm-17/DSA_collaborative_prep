# Authored by Alistair Clark - github: alistair-clark
# date: <date>
from test_script.test import test_pyramid

# def pyramid(N):
#     """Readable solution."""
#     result = []
#     for i in range(N):
#         spaces = ' '* (N-i-1)
#         nums = '#'*(1+2*i)
#         result.append(spaces+nums+spaces)
#     return result


def pyramid(N):
    """Oneline solution."""
    return [' '*(N - i - 1) + '#'*(1 + 2*i) + ' '* (N - i - 1) for i in range(N)]
 
 
if __name__ == '__main__':
    test_pyramid(pyramid)