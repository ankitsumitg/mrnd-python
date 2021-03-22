__author__ = 'Kalyan'

max_marks = 30

problem_notes = '''
This problem is the reverse of problem3. Given the jumbled text created 
according to the rules given in problem 3 and number of steps, create the original text.

Notes:
1. Raise ValueError if n <= 0
2. Raise TypeError if text is not a str
3. Do not search for mathematical patterns, solve this programatically
'''


def unjumble(jumbled_text, n):
    try:
        if not isinstance(jumbled_text, str): raise TypeError
        if n <=0 :raise ValueError
        ans= list()
        for i in range(0,n):
            ans.append("")
        countp = list()
        for i in range(0,n):
            countp.append(0)
        stair = n
        top = 1
        temp = str(jumbled_text)
        while len(temp) > 0:
            if top == 1:
                countp[stair-1] += 1
                ans[ stair - 1 ] += (temp[ 0:stair ])
                temp = temp.replace(temp[0:stair],"")
                stair = stair - 1
                if stair == 0:
                    top = 0
                    stair = 1
            else:
                countp[ stair - 1 ] += 1
                ans[ stair - 1 ] += (temp[ 0:stair ])
                temp = temp.replace(temp[ 0:stair ], "")
                stair = stair + 1
                if stair == n+1:
                    top = 1
                    stair = n
        temp = str(jumbled_text)
        ans2 = list()
        qq =0
        for i in countp:
            ans2.append(temp[0:len(ans[qq])])
            temp = temp.replace(temp[0:len(ans[qq])],"")
            qq +=1
        finalans = ""
        stair = n
        top = 1
        temp = str(jumbled_text)
        while len(temp) != len(finalans):
            if top == 1:
                finalans += ans2[stair-1][0:stair]
                ans2[ stair - 1 ] = ans2[stair - 1].replace(ans2[stair - 1][0:stair],"")
               # temp = temp.replace(ans2[stair - 1][0:stair], "")
                stair = stair - 1
                if stair == 0:
                    top = 0
                    stair = 1
            else:
                finalans += ans2[ stair - 1 ][ 0:stair ]
                ans2[ stair - 1 ] = ans2[ stair - 1 ].replace(ans2[ stair - 1 ][ 0:stair ], "")
              #  temp = temp.replace(ans2[ stair - 1 ][ 0:stair ], "")
                stair = stair + 1
                if stair == n+1:
                    top = 1
                    stair = n
        return finalans
    except ValueError:
        raise  ValueError
    except TypeError:
        raise TypeError


def test_unjumble():
    assert "Ashokan" == unjumble("hoAskan", 2)
    assert "Ankit" == unjumble("kiAnt", 2)
    assert "abcdefghij" == unjumble("fgdehiabcj", 3)