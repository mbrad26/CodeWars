"""Achtung !!!
        Infinite Loop
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

num = 0
while True:
    if is_prime(num):
        print(num)
    num += 1
