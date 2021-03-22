__author__ = 'Kalyan'

max_marks = 20

problem_notes = '''
Palindrome is a word which spells the same from both ends.

Create the smallest palindrome from a given word by appending characters to its end.

Examples:
- Malayalam -> Malayalam
- Malayal -> Malayalam (we want smallest palindrome)


Notes:
1. Don't change the letters of the initial word, only add new small letters
2. The palindrome is case-insensitive (ie) Tat is a valid palindrome
3. Only letters are allowed, any other characters should raise a ValueError
4. Non strings should raise a TypeError
5. Empty string is considered as a palindrome.
'''

def smallest_palindrome(word):

    try:
        if not isinstance(word, str): raise TypeError
        if word.strip() == "" :return word
        #if not word.isalpha(): raise ValueError
        my_str = word.casefold()
        for i in range(len(word)):
            y = (my_str[:i])[::-1]
            if (not y.isalpha()) and i >0: raise ValueError
            x = my_str + (my_str[:i])[::-1]
            rev_str = (x)[::-1]
            if rev_str == x:
                return word + (my_str[:i])[::-1]
    except ValueError:
        raise  ValueError
    except TypeError:
        raise TypeError


# write your own tests
def test_smallest_palindrome():
    assert "" == smallest_palindrome("")
    assert "Malayalam" == smallest_palindrome("Malayal")
    assert 'aIbohPhoBia' == smallest_palindrome('aIbohPhoBi')
    #assert "Malayalam" == smallest_palindrome("Malay9al")
    #assert "Malayalam" == smallest_palindrome([])
