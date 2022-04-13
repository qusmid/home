# два метода в классе, один принимает в себя либо строку, либо число
# если я передаю строку, то смотрим: если произведение гласных и согласных букв МЕНЬШЕ или РАВНО длине слова,
# выводить все гласные, иначе согласные. Если число, то произведение суммы чётных цифр на длину числа.
# длину строки и числа искать во втором методе

x = input()


class Methods:

    def __init__(self, x):
        self.x = x

    def lnt(self):
            return len(str(self.x))

    def typing(self):
        if self.x.isdigit():
            self.x = int(self.x)
            self.x = x
            lenght = methods.lnt()
            even = []
            for i in self.x:
                if int(i) % 2 == 0:
                    even.append(int(i))
            print(f"even numbers = {even}")
            amount = 0
            for self.x in even:
                amount += self.x
            print(f"amount = {amount}")
            multiplication = amount * lenght
            return multiplication
        else:
            self.x = str(self.x)
            self.x = self.x.lower()
            lenght = methods.lnt()
            vowels = []
            consonants = []
            methods.lnt()
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
                return result_vowels
            else:
                return result_consonants


methods = Methods(x)
print(methods.typing())
