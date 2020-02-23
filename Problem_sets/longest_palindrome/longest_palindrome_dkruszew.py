# Authored by Derek Kruszewski - github: dkruszew
# Date: 2020-02-19
from test_script.test import test_longest_palindrome

def longestPalindrome(text):
    """
    Finds the longest instance of a palindrome in a string
    """
    ngrams = {}
    longest_palin = None
    for i in list(reversed(range(1,len(text)+1))):
        ngrams[i] = list()
        ngram = text
        while len(ngram) >= i:
            ngrams[i].append(ngram[0:i])
            ngram = ngram[1:]
        for text in ngrams[i]:
            if text == text[::-1]:
                longest_palin = text
                break
            else:
                continue
        if longest_palin == None:
            continue
        else:
            break            
    return longest_palin
        
if __name__ == '__main__':
    test_longest_palindrome(longestPalindrome)