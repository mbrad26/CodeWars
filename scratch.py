h = 30.00
b = 0.66
w = 1.50

r = 1
flag = True
while flag:
    new_h = h * b
    if new_h > w:
        r += 1
        new_h *= b
    else:
        flag = False
