__author__ = 'Kalyan'

max_marks = 25  # encrypt -> 13, decrypt 12

problem_notes = '''
Write encryption and decryption routines according to the given scheme. 

A secret key is used to encrypt a text message in the following manner: 
- key is a string of letters in which each letter represents the right displacement of the source character (a -> 0, z-> 25)
- text -> input text to be sent 

Letters of the input text are mapped to the letters in the key in a round robin manner. For e.g:

For: key = "abcde", text="hi there", the mapping is 
h->a, i -> b, (space is ignored) t ->c, h -> d, e-> e, (go back to starting a here) r -> a, e->b 

now to get the encrypted text, you move h by 0, i by 1, t by 2, h by 3 etc. So you finally get the text "hj vkirf"

The decryption works in the reverse way and returns the original text.

Notes:
- Preserve the casing(lower case remains lower case, Upper case remains Upper case).
- Ignore non-letters and punctuations, i.e., leave them as is in the final result
- For displacement, both small and large letters represent the same displacement. For e.g. b and B both represent 1
- raise TypeError if text and key are not strings.
- raise ValueError if key is empty or has non alphabet characters

Write helper sub routines as required. Make good use of the available datatypes!
'''

# do type checking, non-str should raise TypeException
def get_encoding_dict():
    lower = list(range(ord('a'), ord('z') + 1))
    upper = list(range(ord('A'), ord('Z') + 1))
    #new syntax
    return {**dict(zip(list(map(chr,lower)),list(range(0,26)))),**dict(zip(list(map(chr,upper)),list(range(0,26))))}
def encrypt(text, key):
    try:
        if not isinstance(text, str): raise TypeError
        if not isinstance(key, str): raise TypeError
        if key == None or key.strip() == "":raise ValueError
        d = get_encoding_dict()
        finalMessage = ""
        j = 0
        for x in range(0, len(text)):
            if text[ x ].isalpha():
                x1 = key[ j % len(key) ]
                y1 = int(d[ x1 ])
                if ord(text[x]) >= 97 and ord(text[x]) <= 122:
                    z1 = ord(text[ x ]) + y1
                    if z1>122:
                        finalMessage += (chr((z1)%123 + 97))
                    else:finalMessage += chr((z1))
                    j += 1
                else:
                    z1 = ord(text[ x ]) + y1
                    if z1 > 90:
                        finalMessage += (chr((z1) % 91 + 65))
                    else:
                        finalMessage += chr((z1))
                    j += 1
            else: finalMessage += text[ x ]
        return finalMessage
    except ValueError:
        raise  ValueError
    except TypeError:
        raise TypeError

def decrypt(text, key):
    try:
        if not isinstance(text, str): raise TypeError
        if not isinstance(key, str): raise TypeError
        if key == None or key.strip() == "":raise ValueError
        d = get_encoding_dict()
        finalMessage = ""
        j = 0
        for x in range(0, len(text)):
            if text[ x ].isalpha():
                x1 = key[ j % len(key) ]
                y1 = int(d[ x1 ])
                if ord(text[ x ]) >= 97 and ord(text[ x ]) <= 122:
                    z1 = ord(text[ x ]) - y1
                    if z1 < 97:
                        finalMessage += (chr(123-(z1 - 97)))
                    else:
                        finalMessage += chr((z1))
                    j += 1
                else:
                    z1 = ord(text[ x ]) - y1
                    if z1 < 65:
                        finalMessage += (chr(91-(z1 - 65)))
                    else:
                        finalMessage += chr((z1))
                    j += 1
            else:
                finalMessage += text[ x ]
        return finalMessage
    except ValueError:
        raise  ValueError
    except TypeError:
        raise TypeError

def test_encrypt():
    assert "hj vkirf" == encrypt("hi there", "abcde")

def test_decrypt():
    assert "hi there" == decrypt("hj vkirf", "abcde")
""" s = s.replace('+','')
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
        return ans if num >=0 else -1*ans"""
