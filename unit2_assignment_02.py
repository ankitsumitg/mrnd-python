__author__ = 'Kalyan'

notes = '''
Write your own implementation of converting a number to a given base. It is important to have a good logical
and code understanding of this.

Till now, we were glossing over error checking, for this function do proper error checking and raise exceptions
as appropriate.

Reading material:
    http://courses.cs.vt.edu/~cs1104/number_conversion/convexp.html
'''

def convert(number, base):
    """
    Convert the given number into a string in the given base. valid base is 2 <= base <= 36
    raise exceptions similar to how int("XX", YY) does (play in the console to find what errors it raises).
    Handle negative numbers just like bin and oct do.
    """
    try:
        if base<=1 or base >36: raise ValueError
        elif type(number).__name__ != 'int' or type(base).__name__ != 'int': raise TypeError
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
            return '-' + new_num if number<0 else new_num
    except ValueError:
        raise  ValueError('Invalid Base')
    except TypeError:
        raise TypeError('Invalid Type')

def test_convert():
    assert "100" == convert(4,2)
    assert "FF" == convert(255,16)
    assert "377" == convert(255, 8)
    assert "JJ" == convert(399, 20)
    assert "-JJ" == convert(-399, 20)

    try:
        convert(10,1)
        assert False, "Invalid base <2 did not raise error"
    except ValueError as ve:
        print(ve)

    try:
        convert(10, 40)
        assert False, "Invalid base >36 did not raise error"
    except ValueError as ve:
        print(ve)

    try:
        convert("100", 10)
        assert False, "Invalid number did not raise error"
    except TypeError as te:
        print(te)

    try:
        convert(None, 10)
        assert False, "Invalid number did not raise error"
    except TypeError as te:
        print(te)


    try:
        convert(100, "10")
        assert False, "Invalid base did not raise error"
    except TypeError as te:
        print(te)
