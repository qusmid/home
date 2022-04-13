# два метода в классе, один принимает в себя либо строку, либо число
# если я передаю строку, то смотрим: если произведение гласных и согласных букв МЕНЬШЕ или РАВНО длине слова,
# выводить все гласные, иначе согласные. Если число, то произведение суммы чётных цифр на длину числа.
# длину строки и числа искать во втором методе
x = input()
lenght = len(str(x))
multiplication = 1
even = []
for i in x:
    if int(i) % 2 == 0:
        even.append(int(i))
amount = 0
for x in even:
    amount += x
print(amount)
multiplication = amount * lenght
print(multiplication)
