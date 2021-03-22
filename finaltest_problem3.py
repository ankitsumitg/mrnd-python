__author__ = 'Kalyan'

max_marks = 25

problem_notes = '''
For this problem you have to implement a staircase jumble as described below. 

1. You have n stairs numbered 1 to n. You are given some text to jumble.
2. You repeatedly climb down and up the stairs and on each step k you add/append starting k chars from 
   the text you have (and remove them from the text). 
3. You repeat this process till you finish the whole text.
4. Finally you climb up from step 1 and collect all chars to get the jumbled text.

E.g.  if the text is "Ashokan" and n = 2.  You have the following text on the steps. First you drop 

 "As" on step 2, then "h" on step 1, then you get to the ground and you 
 climb back again droping "o" on step 1 and "ka" on step2 and finally "n" on step2 
 (since you have run out of chars and you dont have 2 chars).
  
 So sequence of steps is 2, 1 then 1, 2 then 2, 1 and so on...
 
(step2)As;ka;n
       ----
   (step 1)|h;o
           ----
Final jumbled text is hoAskan (all text on step1 followed by all text on step2, the ; is shown above only to visually 
distinguish the segments of text dropped on the stair at different times)

Notes:
1. Raise ValueError if n <= 0
2. Raise TypeError if text is not a str
3. Note that spaces, punctuation or any other chars are all treated like regular chars and 
   they will be jumbled in same way.
'''

def jumble(text, n):
    try:
        if not isinstance(text, str): raise TypeError
        if n <=0 :raise ValueError
        ans= list()
        for i in range(0,n):
            ans.append("")
        stair = n
        top = 1
        temp = str(text)
        while len(temp) > 0:
            if top == 1:
                ans[stair-1] +=(temp[0:stair])
                temp = temp.replace(temp[0:stair],"")
                stair = stair - 1
                if stair == 0:
                    top = 0
                    stair = 1
            else:
                ans[ stair - 1 ] += (temp[ 0:stair ])
                temp = temp.replace(temp[ 0:stair ], "")
                stair = stair + 1
                if stair == n+1:
                    top = 1
                    stair = n
        finalans = ""
        for i in ans:
            finalans += i
        return finalans


    except ValueError:
        raise  ValueError
    except TypeError:
        raise TypeError


def test_jumble():
    assert "hoAskan" == jumble("Ashokan", 2)
    assert "kiAnt" == jumble("Ankit", 2)
    assert "fgdehiabcj" == jumble("abcdefghij", 3)