import math

def square(a):
    p = 4 * a # периметр квадрата
    s = a ** 2 # площадь квадрата
    d = math.sqrt(2) * a # диагональ квадрата

    return p, s, d

print(square(int(input("Input the side of square: "))))