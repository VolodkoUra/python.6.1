"""Есть Алфавит, характеристиками которого являются:
1. Язык
2. Список букв

Для Алфавита можно:
1. Напечатать все буквы алфавита
2. Посчитать количество букв

Так же есть Английский алфавит, который обладает следующими свойствами:
1. Язык
2. Список букв
3. Количество букв

Для Английского алфавита можно:
1. Посчитать количество букв
2. Определить, относится ли буква к английскому алфавиту
3. Получить пример текста на английском языке

Задание

Класс Alphabet
1. Создайте класс Alphabet
2. Создайте метод __init__(), внутри которого будут определены два динамических свойства:
1) lang - язык и 2) letters - список букв. Начальные значения свойств берутся из входных параметров метода.
3. Создайте метод print(), который выведет в консоль буквы алфавита
4. Создайте метод letters_num(), который вернет количество букв в алфавите

Класс EngAlphabet
1. Создайте класс EngAlphabet путем наследования от класса Alphabet
2. Создайте метод __init__(), внутри которого будет вызываться родительский метод __init__().
В качестве параметров ему будут передаваться обозначение языка(например, 'En') и строка,
состоящая из всех букв алфавита(можно воспользоваться свойством ascii_uppercase из модуля string).
3. Добавьте приватное статическое свойство __letters_num, которое будет хранить количество букв в алфавите.
4. Создайте метод is_en_letter(), который будет принимать букву в качестве параметра и определять,
относится ли эта буква к английскому алфавиту.
5. Переопределите метод letters_num() - пусть в текущем классе классе он будет возвращать значение
свойства __letters_num.
6. Создайте статический метод example(), который будет возвращать пример текста на английском языке.

Тесты:
1. Создайте объект класса EngAlphabet
2. Напечатайте буквы алфавита для этого объекта
3. Выведите количество букв в алфавите
4. Проверьте, относится ли буква F к английскому алфавиту
5. Проверьте, относится ли буква Щ к английскому алфавиту
6. Выведите пример текста на английском языке

"""
import string


class Alphabet:

    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = list(letters)

    def print(self):
        print("Список букв: ", self.letters)

    def letters_num(self):
        print("Количество букв в алфавите: ", len(self.letters))


class EngAlphabet(Alphabet):
    __leters_num = 26
    def __init__(self):
        super().__init__('En', string.ascii_uppercase)

    def is_en_letter(self, l):
        if l.upper() in self.letters:
            return True
        else:
            return False

    def letters_num(self):
        return EngAlphabet.__leters_num

    @staticmethod
    def example():
        print("English Example:\nDon't judge a book by it's cover.")


if __name__ == '__main__':
    e = EngAlphabet()
    e.print()
    print(e.letters_num())
    print(e.is_en_letter("F"))
    print(e.is_en_letter("Щ"))
    e.example()
