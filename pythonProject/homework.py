# дано число n -> вывести число n + nn + nnn
str1 = '222222'


def func(str1):
    A = 1
    result = []
    for i in range(0, len(str1), A):
        result.append(str(str1[i: i + A]))
    n1 = result[0]
    n2 = result[1]
    n3 = result[2]
    n4 = result[3]
    n5 = result[4]
    n6 = result[5]
    n10 = n2 + n3
    n20 = n4 + n5 + n6
    x = int(n1) + int(n10) + int(n20)
    print(n1, "+", n2 + n3, "+", n4 + n5 + n6, "=", x)
    return


func(str1)
