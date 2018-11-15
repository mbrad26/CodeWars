from collections import Counter


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


print(is_prime(165548546549844515158564498879454148979456155485517))


"""Given two arrays a and b write a function comp(a, b) (compSame(a, b) in Clojure) that checks whether the two arrays
 have the "same" elements, with the same multiplicities. "Same" means, here, that the elements in b are the elements in
  a squared, regardless of the order.

Examples
Valid arrays
a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
comp(a, b) returns true because in b 121 is the square of 11, 14641 is the square of 121, 20736 the square of 144, 361 
the square of 19, 25921 the square of 161, and so on. It gets obvious if we write b's elements in terms of squares:

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
a or b might be [] (all languages except R, Shell). a or b might be nil or null or None or nothing (except in Haskell,
 Elixir, C++, Rust, R, Shell).

If a or b are nil (or null or None), the problem doesn't make sense so return false.

If a or b are empty the result is evident by itself."""


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
    for i in range(int(len(s_list) / 2)):
        new_s.append(''.join(s_list[i: i + 2]))
    return new_s


print(solution('abc')) # should return ['ab', 'c_']
print(solution('abcdefgj')) # should return ['ab', 'cd', 'ef']


"""You are going to be given an array of integers. Your job is to take that array and find an index N where the sum of
the integers to the left of N is equal to the sum of the integers to the right of N. If there is no index that would 
make this happen, return -1.

For example:

Let's say you are given the array {1,2,3,4,3,2,1}:
Your function will return the index 3, because at the 3rd position of the array, the sum of left side of the index 
({1,2,3}) and the sum of the right side of the index ({3,2,1}) both equal 6.

Let's look at another one.
You are given the array {1,100,50,-51,1,1}:
Your function will return the index 1, because at the 1st position of the array, the sum of left side of the index ({1}) 
and the sum of the right side of the index ({50,-51,1,1}) both equal 1.

Last one:
You are given the array {20,10,-80,10,10,15,35}
At index 0 the left side is {}
The right side is {10,-80,10,10,15,35}
They both are equal to 0 when added. (Empty arrays are equal to 0 in this problem)
Index 0 is the place where the left side and right side are equal.

Note: Please remember that in most programming/scripting languages the index of an array starts at 0.

Input:
An integer array of length 0 < arr < 1000. The numbers in the array can be any integer positive or negative.

Output:
The lowest index N where the side to the left of N is equal to the side to the right of N. If you do not find an index 
that fits these rules, then you will return -1.

Note:
If you are given an array with multiple answers, return the lowest correct index.
An empty array should be treated like a 0 in this problem."""


def find_even_index(arr):
    for i in enumerate(arr):
        if sum(arr[:i[0]]) == sum(arr[i[0] + 1:]):
            return i[0]
    else:
        return -1


"""Pete likes to bake some cakes. He has some recipes and ingredients. Unfortunately he is not good in maths. Can you 
help him to find out, how many cakes he could bake considering his recipes?

Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object) and returns 
the maximum number of cakes Pete can bake (integer). For simplicity there are no units for the amounts (e.g. 1 lb of 
flour or 200 g of sugar are simply 1 or 200). Ingredients that are not present in the objects, can be considered as 0.

Examples:

# must return 2
cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})
# must return 0
cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000})
"""


def cakes(recipe, available):
    r = sorted(recipe)
    a = sorted(available)
    results = [available[key] // recipe[key] for key in r if key in a and recipe[key] <= available[key]]
    if len(r) > len(a) or len(results) < len(r):
        return 0
    elif len(results) == len(r):
        return min(results)


"""Given two arrays of strings a1 and a2 return a sorted array r in lexicographical order of the strings of a1 which 
are substrings of strings of a2.

#Example 1: a1 = ["arp", "live", "strong"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

returns ["arp", "live", "strong"]

#Example 2: a1 = ["tarp", "mice", "bull"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

returns []

Notes:
Arrays are written in "general" notation. See "Your Test Cases" for examples in your language.

In Shell bash a1 and a2 are strings. The return is a string where words are separated by commas.

Beware: r must be without duplicates.
Don't mutate the inputs.
"""


# def in_array(array1, array2):
#     r = []
#     for substr in array1:
#         for str in array2:
#             if substr in str:
#                 r.append(substr)
#     return list(sorted(set(r)))

def in_array(array1, array2):
    return [substr for substr in sorted(set(array1)) if substr in ''.join(array2)]


"""Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to 
match str2, otherwise returns false.

Notes:

Only lower case letters will be used (a-z). No punctuation or digits will be included.
Performance needs to be considered"""

# 513 out of 520

# def scramble(s1, s2):
#     r = []
#     for char in s2:
#         if char in s1:
#             r.append(char)
#     return len(r) == len(s2)


# Time: 11739ms Passed: 514 Failed: 6 Exit Code: 1

# def scramble(s1, s2):
#     return all(map(lambda char: True if char in s1 else False, s2))


# Time: 10643ms Passed: 514 Failed: 6 Exit Code: 1

# def scramble(s1, s2):
#     return all([char if char in s1 else False for char in s2])


def scramble(s1, s2):
    letters = Counter(s1)
    word = Counter(s2)
    diff = word - letters
    return len(diff) == 0


"""A child is playing with a ball on the nth floor of a tall building. The height of this floor, h, is known.

He drops the ball out of the window. The ball bounces (for example), to two-thirds of its height (a bounce of 0.66).

His mother looks out of a window 1.5 meters from the ground.

How many times will the mother see the ball pass in front of her window (including when it's falling and bouncing?

Three conditions must be met for a valid experiment:
Float parameter "h" in meters must be greater than 0
Float parameter "bounce" must be greater than 0 and less than 1
Float parameter "window" must be less than h.
If all three conditions above are fulfilled, return a positive integer, otherwise return -1.

Note: The ball can only be seen if the height of the rebounding ball is stricty greater than the window parameter.

Example:

h = 3, bounce = 0.66, window = 1.5, result is 3

h = 3, bounce = 1, window = 1.5, result is -1 (Condition 2) not fulfilled)."""


def bouncing_ball(h, b, w):
    r = 0
    if h > 0 and 0 < b < 1 and w < h:
        while h > w:
            r += 1
            h *= b
        return 2 * r - 1
    else:
        return -1


print(bouncing_ball(3, 0.66, 1.5))

print(bouncing_ball(30, 0.66, 1.5))


"""My friend John and I are members of the "Fat to Fit Club (FFC)". John is worried because each month a list with the 
weights of members is published and each month he is the last on the list which means he is the heaviest.

I am the one who establishes the list so I told him: "Don't worry any more, I will modify the order of the list". 
It was decided to attribute a "weight" to numbers. The weight of a number will be from now on the sum of its digits.

For example 99 will have "weight" 18, 100 will have "weight" 1 so in the list 100 will come before 99. Given a string 
with the weights of FFC members in normal order can you give this string ordered by "weights" of these numbers?

Example:
"56 65 74 100 99 68 86 180 90" ordered by numbers weights becomes: "100 180 90 56 65 74 68 86 99"

When two numbers have the same "weight", let us class them as if they were strings and not numbers: 100 is before 180 
because its "weight" (1) is less than the one of 180 (9) and 180 is before 90 since, having the same "weight" (9) it 
comes before as a string.

All numbers in the list are positive numbers and the list can be empty.

Notes
it may happen that the input string have leading, trailing whitespaces and more than a unique whitespace between two 
consecutive numbers
Don't modify the input
For C: The result is freed."""


def order_weight(strng):
    str = [list(x) for x in strng.split()]
    a = []
    for x in str:
        a.append([int(y) for y in x])
    a = [sum(x) for x in a]
    return ' '.join([''.join(x[1]) for x in sorted(zip(a, str))])

print(order_weight("103 123 4444 99 2000") # "2000 103 123 4444 99")
print(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123") # "11 11 2000 10003 22 123 1234000 44444444 9999")



















