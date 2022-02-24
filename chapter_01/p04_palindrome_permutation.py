# O(N)
import string
import unittest
from collections import Counter


def clean_phrase(phrase):
    return [c for c in phrase.lower() if c in string.ascii_lowercase]


def is_palindrome_permutation(phrase):
    """checks if a string is a permutation of a palindrome"""
    # a-z , num of chars are 26
    NUM_OF_CHARS = 26
    table = [0] * NUM_OF_CHARS
    table = [0 for _ in range(ord("z") - ord("a") + 1)]
    countodd = 0
    for c in phrase: #abcba
        x = char_number(c)
        if x != -1:
            table[x] += 1
            if table[x] % 2: 
                countodd += 1
            else:
                countodd -= 1
    return countodd <= 1

#Using dictionary to maintain a frequency mapping of key:value
def is_palindrome_permutation_using_dict(phrase):
    """checks if a string is a permutation of a palindrome"""
    # a-z , num of chars are 26
    dict = {}
    countodd = 0
    for chars in phrase: #abcba
        if chars in dict:
            dict[chars]+=1 # dict{'a':2,'b':2,'c':1} # if it already exists
        else:
            dict[chars]=1 
    for occr in dict.values():
        if (occr % 2 !=0):
            countodd +=1
    if (countodd <=1)
        return True
    else
        return False    

def char_number(c):
    a = ord("a")
    z = ord("z")
    upper_a = ord("A")
    upper_z = ord("Z")
    val = ord(c) #97

    if a <= val <= z:
        return val - a #return 1

    if upper_a <= val <= upper_z:
        return val - upper_a
    return -1


def is_palindrome_bit_vector(phrase):
    """checks if a string is a permutation of a palindrome"""
    r = 0
    for c in clean_phrase(phrase):
        val = ord(c)
        mask = 1 << val
        if r & mask:
            r &= ~mask
        else:
            r |= mask
    return (r - 1) & r == 0


def is_palindrome_permutation_pythonic(phrase):
    """function checks if a string is a permutation of a palindrome or not"""
    counter = Counter(clean_phrase(phrase))
    return sum(val % 2 for val in counter.values()) <= 1


class Test(unittest.TestCase):
    test_cases = [
        ("aba", True),
        ("aab", True),
        ("abba", True),
        ("aabb", True),
        ("a-bba", True),
        ("a-bba!", True),
        ("Tact Coa", True),
        ("jhsabckuj ahjsbckj", True),
        ("Able was I ere I saw Elba", True),
        ("So patient a nurse to nurse a patient so", False),
        ("Random Words", False),
        ("Not a Palindrome", False),
        ("no x in nixon", True),
        ("azAZ", True),
    ]
    testable_functions = [
        is_palindrome_permutation,
        is_palindrome_bit_vector,
        is_palindrome_permutation_pythonic,
    ]

    def test_pal_perm(self):
        for f in self.testable_functions:
            for [test_string, expected] in self.test_cases:
                assert f(test_string) == expected


if __name__ == "__main__":
    unittest.main()
