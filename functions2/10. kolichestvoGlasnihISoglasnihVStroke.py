def func(a):
    h = 0
    d = 0
    for i in a:
        if i.isalpha():
            if i in "aeoiu":
                h += 1
            else:
                d += 1
    print("Гласные:", h)
    print("Согласные:", d)

func(input("Введите строку: "))