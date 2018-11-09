"""Your task is to sort a given string. Each word in the string will contain a single number.
This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string.
The words in the input String will only contain valid consecutive numbers."""


def order(sentence):
    c = {}
    for word in sentence.split():
        i = int(sorted(word)[0])
        c[i] = word
    return ' '.join([v for (k, v) in sorted(c.items())])


print(order("is2 Thi1s T4est 3a"))
print(order("4of Fo1r pe6ople g3ood th5e the2"))
print(order("khli4of jhFo1r pubve6ople adsg3ood tjgfh5e fvkthe2"))


"""Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case 
insensitive. The string can contain any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false"""


def xo(s):
    s = s.lower()
    if s.count('x') == s.count('o'):
        return True
    else:
        return False


"""Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.

The binary number returned should be a string.

"""


def add_binary(a,b):
    return bin(a + b)[2:]