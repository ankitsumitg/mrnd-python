
__author__ = 'Kalyan'

max_marks = 20

problem_notes = '''
Given 2 strings str1 and str2, find out the minimum number of right rotations str1 needs to undergo
to create str2. If is not possible, return -1

Notes:
1. Assume inputs are either None or valid strings
2. Write plain brute force code.
3. result should be -1 if not possible
4. If it is possible then give the 'minimum rotations' required.
5. No need for type checking.
'''

def get_right_rotations(str1, str2):
    if str1 == None or str2 == None: return -1
    from collections import Counter
    if Counter(str1) == Counter(str2):
        c = 0
        x = len(str2)
        while x >= 0:
            if str1 == str2:
                return c
            str1 = str1[ -1: ] + str1[ :-1 ]
            x -= 1
            c += 1
    return -1

# basic test given, write more tests to ensure correctness.
def test_get_right_rotations():
    assert 1 == get_right_rotations("abcd", "dabc")
    assert 2 == get_right_rotations("abcd ", "d abc")
    assert -1 == get_right_rotations(None, "d abc")
    assert 0 == get_right_rotations('patpat','patpat')
