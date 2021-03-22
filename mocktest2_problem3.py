__author__ = 'Kalyan'

max_marks = 30

problem_notes = '''
For this problem you have to implement a generator which returns all k digit 
numbers whose sum of digits is n. 

Note that you must not generate the entire solution set at one go (ie) the 
result should be generated on demand (when next is called on generator). This means that 
I can call it with large values of n and k like 1000 and 500 and still 
its use of memory must be modest.

Notes:
1. raise TypeError if n and k are not ints.  
2. if n or k are not positive, raise ValueError 
3. the result numbers must be yield'ed in increasing order. 
4. you are free (encouraged :-) ) to define additional sub-routines as you see fit as long as you do not   
   violate the generator semantics given above

Examples:
 for n = 2 and k = 2, the generator must yield 11, 20 in that order
 for n = 4 and k = 2, the generator must yield 13, 22,31,40 in that order
 
Note that numbers starting with 0 are not valid For e.g. 02 is not a valid 2 digit number
'''
import math
def sum_digits(n):
        r = 0
        while n:
            r, n = r + n % 10, n // 10
        return r
def digits(n):
    if n > 0:
       return int(math.log10(n)) + 1
    elif n == 0:
        return 1
    else:
        return int(math.log10(-n)) + 2
#Implement this generator.
def kdigitnums(n, k):
    """
    This is a generator returns all k digit numbers whose sum is n. The numbers are yielded in
    increasing order
    """
    try:
        if not isinstance(n, int): raise TypeError
        if not isinstance(k, int): raise TypeError
        if n < 0 or  k < 0: raise ValueError
        if n == 0 and k == 0: raise ValueError
        ans = int(math.pow(10, k-1))
        if digits(ans) == 1:
            yield n
            return
        while digits(ans) == k:
            while True:
                if sum_digits(ans) == n:
                    yield ans
                    ans += 1
                    break
                else:
                    ans += 1
                    if digits(ans) != k: break
            ans+=1
            if digits(ans) != k: break
    except ValueError:
        raise ValueError
    except TypeError:
        raise TypeError
    pass


# write more tests
def test_kdigitnums():
    assert [11, 20] == list(kdigitnums(2,2))
    assert [ 1] == list(kdigitnums(1, 1))
