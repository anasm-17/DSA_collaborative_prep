# Authored by Roc Zhang - github:Zhang-Haipeng - email:roc_zhang@hotmail.com
# date: 2020-02-20
from test_script.test import test_longest_palindrome

def longestPalindrome(s):
    """
    The idea is to iterate and check through all possible combinations, **from the longest to the shortest**, 
    and stop and return as soon as we find one (so that it's the longest one).
    """    
    for i in range(len(s),1,-1):
        for j in range(len(s)):
            if i%2 != 0:
                if (s[j:int((i-1)/2+j)] == s[int((i-1)/2+1+j):int(i+j)][::-1]):
                        return s[j:(i+j)]
            if i%2 == 0:
                if (s[j:int(i/2+j)] == s[int(i/2+j):(i+j)][::-1]):
                        return s[j:(i+j)]
    return 'no palindromic found'


if __name__ == '__main__':
    test_longest_palindrome(longestPalindrome)