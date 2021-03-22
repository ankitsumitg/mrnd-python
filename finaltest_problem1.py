__author__ = 'Kalyan'

max_marks = 20

problem_notes = '''
Given a string of digits, you must return a list of all (substring, count) in the input string such that count >=2 and 
len(substring) >= 2. count represents the number of times the substring repeats in the input string (non-overlapping 
occurances).

The result must be sorted by count first (descending) and then in case of a tie the numerical value of 
substring (descending)

For e.g. if input is "123451236786712" you must return [("12", 3), ("123", 2), ("67", 2), ("23", 2)]

Notes:
1. if input is not a str, raise TypeError
2. Write clean bruteforce code to do this using python features. Do not devise new algorithms in the exam!
3. Write your own test cases 
'''

def repeats(digits):
    try:
        if not isinstance(digits, str): raise TypeError
        ans = list()
        for i in range(2,int(len(digits)/2)+1):
            j = i
            check = 0
            while j < len(digits):
                x = digits[check:j]
                c = digits.count(x)
                if c >= 2:
                    if (x,c) not in ans:
                        ans.append((x,c))
                j += 1
                check += 1
        ans = sorted(ans, key=lambda x: (-1*x[ 1 ], -1*int(x[ 0 ])))
        return ans
    except TypeError:
        raise TypeError


def test_repeats():
    assert [("12", 3), ("123", 2), ("67", 2), ("23",2)] == repeats("123451236786712")
    assert [('45', 4), ('56', 3), ('568', 2), ('123', 2), ('68', 2), ('54', 2), ('23', 2), ('12', 2)] == repeats("123123456454545568568")