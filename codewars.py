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


"""Is Prime
Define a function isPrime/is_prime() that takes one integer argument and returns true/True or false/False depending on
if the integer is a prime.

Per Wikipedia, a prime number (or a prime) is a natural number greater than 1 that has no positive divisors other than 
1 and itself.

Example
bool isPrime(5) = return true
mov edi, 1
call is_prime    ; EAX <- 0 (false)

mov edi, 2
call is_prime    ; EAX <- 1 (true)

mov edi, -1
call is_prime    ; EAX <- 0 (false)
Assumptions
You can assume you will be given an integer input.
You can not assume that the integer will be only positive. You may be given negative numbers as well (or 0).
"""


def is_prime(num):
    if num < 1:
        return False
    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
                break
        else:
            return True


print(is_prime(165548546549844515158564498879454148979456155485517)


"""Given two arrays a and b write a function comp(a, b) (compSame(a, b) in Clojure) that checks whether the two arrays have the "same" elements, with the same multiplicities. "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.

Examples
Valid arrays
a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
comp(a, b) returns true because in b 121 is the square of 11, 14641 is the square of 121, 20736 the square of 144, 361 the square of 19, 25921 the square of 161, and so on. It gets obvious if we write b's elements in terms of squares:

a = [121, 144, 19, 161, 19, 144, 19, 11] 
b = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
Invalid arrays
If we change the first number to something else, comp may not return true anymore:

a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [132, 14641, 20736, 361, 25921, 361, 20736, 361]
comp(a,b) returns false because in b 132 is not the square of any number of a.

a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [121, 14641, 20736, 36100, 25921, 361, 20736, 361]
comp(a,b) returns false because in b 36100 is not the square of any number of a.

Remarks
a or b might be [] (all languages except R, Shell). a or b might be nil or null or None or nothing (except in Haskell, Elixir, C++, Rust, R, Shell).

If a or b are nil (or null or None), the problem doesn't make sense so return false.

If a or b are empty the result is evident by itself.

"""


def comp(array1, array2):
    if array1 is None or array2 is None:
        return False
    a1 = [pow(x, 2) for x in array1]
    return sorted(array2) == sorted(a1)


a = [121, 144, 19, 161, 19, 144, 19, 11, 7]
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
comp(a, b)


"""Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number
 of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef']"""


def solution(s):
    s_list = list(s)
    if len(s_list) % 2 != 0:
        s_list.append('_')
    new_s = []
    k = 0
    for i in range(int(len(s_list) / 2)):
        new_s.append(''.join(s_list[i*2: (k + i) + 2]))
        k += 1
    return new_s





































