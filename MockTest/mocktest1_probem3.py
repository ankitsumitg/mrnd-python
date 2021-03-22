__author__ = 'Kalyan'

max_marks = 35 # 15 marks for encode and 20 for decode

problem_notes ='''
 This problem deals with number conversion into a custom base 5 notation and back.
 In this notation, the vowels a e i o u are used for digits 0 to 4.

 E.g. decimal 10 in this custom base 5 notation is "ia", decimal 5 is "ea" etc.

 Your job is to write encoding and decoding (both) routines to deal with this notation.
'''
def convert(number):
    base  = 5
    try:
        if type(number).__name__ != 'int' or type(base).__name__ != 'int': raise TypeError
        else:
            upper = list(range(ord('A'), ord('Z') + 1))
            num_rep= dict(zip(list(range(10, 37)),list(map(chr, upper))))
            new_num = ''
            current = abs(number)
            while current != 0:
                remainder = current % base
                if 36 > remainder > 9:
                    remainder_string = num_rep[ remainder ]
                elif remainder >= 36:
                    remainder_string = '(' + str(remainder) + ')'
                else:
                    remainder_string = str(remainder)
                new_num = remainder_string + new_num
                current //= base
            if new_num == '': return '0'
            return '-' + new_num if number<0 else new_num
    except TypeError:
        raise TypeError('Invalid Type')
# Notes:
# - If number is not a valid int raise TypeError
# - Negative numbers should result in a - prefix to the result similar to how bin works
#  use lower case letters in your result [aeiou].
def to_custom_base5(number):
    arr = ['a','e','i','o','u']
    num = convert(number)
    for i in range(len(arr)):
        num = num.replace(str(i), arr[ i ])
    return num

# Notes:
# - if s is not a string, raise TypeError
# - if the encoding is not right or empty string, raise ValueError
# - allow both - and + as prefixes which represent sign.
# - allow trailing and starting spaces (but not once the sign or number starts)
# - allow both capital and small letters.
# - return a int that corresponds to the number.
def from_custom_base5(s):
    try:
        if not isinstance(s, str): raise TypeError
        s = s.casefold()
        arr = [ 'a', 'e', 'i', 'o', 'u','-'," ",'+']
        for i in s:
            if i not in arr:raise ValueError
        if s.strip() == "": raise ValueError
        s = s.replace('+','')
        s = s.strip();
        s = s.replace('a','0')
        s = s.replace('e', '1')
        s = s.replace('i', '2')
        s = s.replace('o', '3')
        s = s.replace('u', '4')
        num = int(s)
        other2dec = lambda n, other: sum([ (int(v) * other ** i) for i, v in enumerate(list(str(n))[ ::-1 ]) ])
        new_num = num if num >=0 else -1*num
        ans = other2dec(new_num,5)
        return ans if num >=0 else -1*ans
    except ValueError:
        raise  ValueError
    except TypeError:
        raise TypeError

# a basic test is given, write your own tests based on constraints.
def test_to_custom_base5():
    assert "ia" == to_custom_base5(10)
    assert "-ia" == to_custom_base5(-10)
    assert 'a' == to_custom_base5(0)

# a basic test is given, write your own tests based on constraints.
def test_from_custom_base5():
    assert 10 == from_custom_base5(" iA ")
    assert -10 == from_custom_base5(" -ia")
    assert 1101 == from_custom_base5(' +eouae ')
    try:
        from_custom_base5(10)
    except TypeError:
        TypeError
