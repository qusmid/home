def season(num):
    if num == 12 or 1 <= num <= 2:
        print("Winter")

    elif 3 <= num <= 5:
        print("Spring")

    elif 6 <= num <= 8:
        print("Summer")

    elif 9 <= num <= 11:
        print("Autumn")

    else:
        print("Неверно введён номер месяца!")

n = int(input("Введите номер месяца (1-12): "))
season(n)