# два метода в классе, один принимает в себя либо строку, либо число
# если я передаю строку, то смотрим: если произведение гласных и согласных букв МЕНЬШЕ или РАВНО длине слова,
# выводить все гласные, иначе согласные. Если число, то произведение суммы чётных цифр на длину числа.
# длину строки и числа искать во втором методе

x = input()
x = x.lower()
vowels = []
consonants = []
result_vowels = 0
result_consonants = 0
lenght = len(x)
for letter in x:
    if letter.isalpha():
        if letter.lower() in "aeyuioуеыаоэяиюё":
            vowels.append(letter)
        else:
            consonants.append(letter)
print(f"vowels = {vowels}, consonants = {consonants}")
result_vowels = len(vowels)
result_consonants = len(consonants)
print(f"result_vowels = {result_vowels}, result_consonants = {result_consonants}")
result = result_vowels * result_consonants
print(f"result = result_vowels * result_consonants = {result}")
if result < lenght or result == lenght:
    print(f"result_vowels = {result_vowels}")
else:
    print(f"result_consonants = {result_consonants}")