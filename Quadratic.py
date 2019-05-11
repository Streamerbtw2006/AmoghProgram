import math

a = input ("enter A")
b = input ("enter B")
c = input ("enter C")

a = int(a, 10)
b = int(b, 10)
c = int(c, 10)

disc = b*b - 4 * a * c
if disc < 0: 
    print("Undefined")
else:
    sqrt = math.sqrt(disc)

    tp = -1 * b + sqrt
    tp2 = -1* b - sqrt

    ans = tp / 2 * a
    ans2 = tp2 / 2 *a

    print("Answers are " + ans + " and " + ans2)
