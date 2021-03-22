__author__ = 'Kalyan'

notes='''
Notes:
1. Don't use any additional modules from python library.
2. Don't change the signature of the function.
3. Review the relevant lessons if you are blocked.

Reading:
Python has an itertools modules which gives powerful utilities to work with iterators.It is a good exercise to read up
all the method implementations on this page: https://docs.python.org/3/library/itertools.html

For e.g. https://docs.python.org/3/library/itertools.html#itertools.chain

You can use ideas from there, but you cannot use itertools module itself in your code :)
'''

def generator_zip(seq1, seq2, *more_seqs):
    """Instead of returning a list of tuples, generate it incrementally
      by yielding a tuple at a time. Write elegant code using comprehensions.
      The generator ends when the smallest sequence is exhausted.
      Don't assume that the inputs are finite (ie) you cannot probe them for length or convert them to lists!

      Hint: This assignment requires you to use lists, list comprehensions, list to tuple conversion, yield
      statement, variable arguments and their manipulation etc.
    """
    s1 = seq1.__iter__()
    s2 = seq2.__iter__()
    if more_seqs == ():
        while True:
            yield (s1.__next__(), s2.__next__())
    else:
        y = list(map(iter, more_seqs))
        while True:
            z = tuple([s1.__next__(), s2.__next__()] + list([ y[ i ].__next__() for i in range(len(y)) ]))
            yield z
    """ s1 = list(seq1)
    s2 = list(seq2)
    if more_seqs == ():
        t = min(len(s1), len(s2))
        for x in range(t):
            yield (s1[ x ], s2[ x ])
    else:
        y = list(map(list, more_seqs))
        t = min(len(s1), len(s2), min(list(map(len, more_seqs))))
        for x in range(t):
            z = tuple([s1[ x ], s2[ x ]] + list([ y[ i ][ x ] for i in range(len(y)) ]))
            yield z"""

def check_generator(gen, max_count, tuple_length):
    for x in range(max_count):
        result = next(gen)
        assert len(result) == tuple_length, "invalid length"
        for element in result:
            assert x == element, "unexpected value"

    try:
        next(gen)
        assert False, "generator did not finish as expected"
    except StopIteration as se:
        pass

# an infinite generator of even numbers.
def evens():
    num = 0
    while True:
        yield num
        num += 2

def test_generator_zip():
    gen = generator_zip(range(5), range(3), range(4), range(5))
    assert type(gen).__name__ == 'generator'
    check_generator(gen, 3, 4)

    gen = generator_zip(range(5), range(3), range(2))
    assert type(gen).__name__ == 'generator'
    check_generator(gen, 2, 3)

    gen = generator_zip(range(1, 5), "abc", [1, 2])
    assert [(1, 'a', 1), (2, 'b', 2)] == list(gen)

    gen = generator_zip((1, 2), "abcd")
    assert [(1, 'a'), (2, 'b')] == list(gen)

    # test with an infinite sequence
    gen = generator_zip("abc", evens(), (1,2))
    assert [('a',0,1), ('b',2,2)] == list(gen)