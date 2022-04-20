student_Ruslan = ("Ruslan", 44, 6, "Minsk")
student_Aleksey = ("Aleksey", 30, 9, "Sofia")
student_Vladimir = ("Vladimir", 64, 3, "Seoul")
student_Petr = ("Petr", 23, 10, "Khartoum")
student_Klim = ("Klim", 65, 5, "Zurich")
student_Ekaterina = ("Ekaterina", 31, 4, "Tokyo")
student_Vasiliy = ("Vasiliy", 43, 8, "Bishkek")
students = (student_Ruslan, student_Aleksey, student_Vladimir, student_Petr,
            student_Klim, student_Ekaterina, student_Vasiliy)

def good_students(students):
    scores = 0
    i = 0

    while i < len(students):
        scores += students[i][2]
        i = i + 1
    scores = scores / len(students)
    scores = round(scores, 2)
    print(f"Средний балл учащихся: {scores}.")
    scores = round(scores)

    best = []
    k = 0

    while k < len(students):
        if scores <= students[k][2]:
            best.append(students[k][0])
            k = k + 1
        else:
            k = k + 1
    print(f"Ученики {best} в этом семестре хорошо учатся!")

good_students(students)