x = int(input("Введите начало диапазона: "))
y = int(input("Введите окончание диапазона: "))
l = []

for j in range(x, y + 1):
    l.append(j)
print("Диапазон сформирован.")


def is_prime():
    prime = []
    for k in l:
        if k > 1:
            for i in range(2, int(k / 2) + 1):
                if (k % i) == 0:
                    break
            else:
                prime.append(k)
    print("Простые числа в данном диапазоне:", prime)


is_prime()
