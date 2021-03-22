__author__ = 'Kalyan'

max_marks = 25

problem_notes = '''
Imagine a line starting from 0 to infinity.

You color parts of that line green by specifying it as an interval. For e.g  (0, 2) will cover the segment from 0 to 2 
green.

You are given a list of tuples that have to be colored green. If the tuples are overlapping 
and part of the line is already green, the uncolored part is colored green.

For e.g. if input is (20, 21) (5,11) and (45, 47) then effectively 9 units will be colored green.

Your job is to figure out how much length of the line has been colored green if these tuples are applied.

Notes:
1. No type checking required, assume low and high are ints > 0. Assume you are given a valid list of tuples
2. The intervals can be long, so you must not timeout for large values.

'''

def get_green_length(segments):
    try:
        segments = sorted(segments, key=lambda x: x[ 0 ])
        check = 0
        """
        ans.pop()
                        ans.append((previous[ 0 ], interval[ 1 ]))
        """
        ans = [ ]
        for interval in segments:
            if ans == [ ]:
                ans.append(interval)
                previous = interval
            else:
                #checking if the interval coincide
                if (previous[ 1 ] > interval[ 0 ]):
                    if (previous[ 1 ] > interval[ 1 ]):
                        pass
                    else:
                        ans.pop()
                        ans.append((previous[ 0 ], interval[ 1 ]))
                        previous = (previous[ 0 ], interval[ 1 ])
                else:
                    ans.append(interval)
                    previous = interval
        count = 0
        for i in ans:
            count = count + (i[ 1 ] - i[ 0 ])
        return count
    except ValueError:
        raise  ValueError
def test_get_green_length():
    assert 11 == get_green_length([(20,21), (5,11), (1,10)])
    assert 9 == get_green_length([(20,21), (5,11), (45,47)])