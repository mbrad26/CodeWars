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


"""Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done 
before, or after the addition.

The binary number returned should be a string.

"""


def add_binary(a,b):
    return bin(a + b)[2:]


"""Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except for the last two names, which should be 
separated by an ampersand.

Example:

namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

namelist([ {'name': 'Bart'} ])
# returns 'Bart'

namelist([])
# returns ''
"""


def namelist(names):
    a = [name.get('name') for name in names]
    last = a[-2:]
    first = a[:-2]
    last = ' & '.join(last)
    first.append(last)
    return ', '.join(first)


"""Write Number in Expanded Form
You will be given a number and you will need to return it as a string in Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
NOTE: All numbers will be whole numbers greater than 0."""


def expanded_form(num):
    a = [str(int(k) * pow(10, i))for i, k in enumerate(list(str(num))[::-1])][::-1]
    return ' + '.join([number for number in a if number != '0'])


print(expanded_form(70304))


"""Your goal in this kata is to implement a difference function, which subtracts one list from another and returns 
the result.

It should remove all values from list a, which are present in list b.

array_diff([1,2],[1]) == [2]
If a value is present in b, all of its occurrences must be removed from the other:

array_diff([1,2,2,2,3],[2]) == [1,3]"""


def array_diff(a, b):
    return [x for x in a if x not in b]


array_diff([1,2,2], [])