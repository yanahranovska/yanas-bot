# -*- coding: cp1251 -*-
import re
from colorama import init, Fore
import math
import datetime
import random

init(autoreset=True)


def printBot(text):
    print(Fore.RED + text)


def writetofile(text, filename):
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text + "\n")


def point3d(f):
    x1 = float(input("Введіть x1: "))
    y1 = float(input("Введіть y1: "))
    z1 = float(input("Введіть z1: "))
    x2 = float(input("Введіть x2: "))
    y2 = float(input("Введіть y2: "))
    z2 = float(input("Введіть z2: "))
    return ("Результат d=" + str(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)))


def arc():
    r = float(input("Введіть радіус кола: "))
    teta = float(input("Введіть кут між двома точками на колі: "))
    return ("Результат L=" + str(r * teta))


def point2d():
    x1 = float(input("Введіть x1: "))
    y1 = float(input("Введіть y1: "))
    x2 = float(input("Введіть x2: "))
    y2 = float(input("Введіть y2: "))
    return ("Результат d=" + str(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)))


def trapezoid():
    a = float(input("Введіть сторону а: "))
    b = float(input("Введіть сторону b: "))
    h = float(input("Введіть сторону h: "))
    S = 0.5 * (a + b) * h
    return ("Результат S=" + str(S))


def pi():
    return ("Число П=" + str(math.pi))


def vectors():
    Ax = float(input("Введіть координату x для вектора A: "))
    Ay = float(input("Введіть координату y для вектора A: "))
    Az = float(input("Введіть координату z для вектора A: "))
    Bx = float(input("Введіть координату x для вектора B: "))
    By = float(input("Введіть координату y для вектора B: "))
    Bz = float(input("Введіть координату z для вектора B: "))
    result = [
        Ay * Bz - Az * By,
        Az * Bx - Ax * Bz,
        Ax * By - Ay * Bx
    ]

    return 'Векторний добуток A x B: '+str(result)


def kulon():
    k = 8.9875 * (10 ** 9)
    q1 = float(input("Введіть q1: "))
    q2 = float(input("Введіть q2: "))
    r = float(input("Введіть r: "))
    return ('Результат F=' + str(k * q1 * q2 * r))


def amper():
    m = 4 * math.pi * 10 ** -7
    I = float(input("Введіть I: "))
    r = float(input("Введіть r: "))
    B = (m * I) / (2 * math.pi * r)
    return ('Результат B=' + str(B) + 'Тл')


def stalaG():
    return ("Значення гравітаційної сталої (G) приблизно дорівнює 6.67430(15) ? 10^(-11) Н·м?/кг?")


def stalaK():
    return ("Значення Кулонівської сталої ?? приблизно дорівнює 8.8541878128(13) ? 10^(-12) Ф/м.")


def greateLake():
    return ("Найбільше озеро в світі за площею - це Каспійське море")


def watershed():
    return ("Дві держави, які мають найбільшу кількість водосховищ в світі, це країна 404 та Канада (Canada)")


def pathetic_sentences():
    return ("Питальні речення в англійській мові формуються шляхом розміщення допоміжного дієслова перед підметом або за допомогою інверсії порядку слів.")

def azimut():
    x1=float(input("Введіть координату x для точки А: "))
    y1=float(input("Введіть координату y для точки А: "))
    x2=float(input("Введіть координату x для точки В: "))
    y2=float(input("Введіть координату y для точки В: "))

    dx = x2 - x1
    dy = y2 - y1

    azimuth_rad = math.atan2(dy, dx)
    azimuth_deg = math.degrees(azimuth_rad)

    azimuth_deg = (azimuth_deg + 360) % 360

    return ("Азимут дорівнює "+str(azimuth_deg))


def unique():
    input_filename = input("Введіть ім'я вхідного файлу: ")
    output_filename = input("Введіть ім'я вихідного файлу: ")

    try:
        with open(input_filename, 'r', encoding='utf-8') as input_file:
            content = input_file.read()

        text = re.sub(r'[^\w\s]', '', content)
        words = text.split()

        words = [word.lower() for word in words]

        unique_words = str(list(set(words)))

        with open(output_filename, 'w', encoding='utf-8') as output_file:
            output_file.write(unique_words)

        return ("Результат був записаний у файл " + output_filename)
    except FileNotFoundError:
        return ("Помилка: Файл не знайдено.")
    except Exception as e:
        return ("Помилка: Виникла помилка при обробці файлу." + str(e))


def reverse():
    input_filename = input("Введіть ім'я вхідного файлу: ")

    try:
        with open(input_filename, 'r', encoding='utf-8') as input_file:
            content = input_file.read()

        reversed_lines = list(reversed(content))

        return "Кількість речень у тексті: " + str(reversed_lines)
    except FileNotFoundError:
        return ("Помилка: Файл не знайдено.")
    except:
        return ("Помилка: Виникла помилка при обробці файлу.")


def max_sentence():
    input_filename = input("Введіть ім'я вхідного файлу: ")

    try:
        with open(input_filename, 'r', encoding='utf-8') as input_file:
            content = input_file.read()

        sentences = content.split('. ')
        longest_sentence = max(sentences, key=len)
        return ("Найдовше речення в тексті: " + str(longest_sentence))
    except FileNotFoundError:
        return ("Помилка: Файл не знайдено.")
    except:
        return ("Помилка: Виникла помилка при обробці файлу.")


def vowel():
    input_filename = input("Введіть ім'я вхідного файлу: ")
    output_filename = input("Введіть ім'я вихідного файлу: ")

    try:
        with open(input_filename, 'r', encoding='utf-8') as input_file:
            content = input_file.read()

        words = content.split()
        longest_words = []

        for word in words:
            if all(letter.lower() not in 'aeiouаеєиіїоуюя' for letter in word):
                if not longest_words or len(word) > len(longest_words[0]):
                    longest_words = [word]
                elif len(word) == len(longest_words[0]):
                    longest_words.append(word)

        with open(output_filename, 'w', encoding='utf-8') as output_file:
            output_file.write(str(longest_words))

        return ("Результат був записаний у файл" + output_filename)
    except FileNotFoundError:
        return ("Помилка: Файл не знайдено.")
    except:
        return ("Помилка: Виникла помилка при обробці файлу.")


def season():
    now = datetime.datetime.now()
    month = now.month

    if month in range(3, 6):
        current_season = "весна"
    elif month in range(6, 9):
        current_season = "літо"
    elif month in range(9, 12):
        current_season = "осінь"
    else:
        current_season = "зима"

    return "Поточна пора року- " + str(current_season)


def month():
    now = datetime.datetime.now()
    current_month = now.strftime("%B")

    return "Поточний місяць - " + str(current_month)


def guess_number_game():
    number_to_guess = random.randint(1, 10)
    attempts = 0

    printBot("Гра 'Вгадай число від 1 до 10'")
    printBot("Я загадав число. Спробуйте вгадати!")

    while True:
        guess = int(input("Введіть вашу догадку: "))
        attempts += 1

        if guess == number_to_guess:
            return ("Вітаю! Ви вгадали число" + str(number_to_guess) + "за" + str(attempts) + "спроб!")
        else:
            return ("На жаль, ви не вгадали. Загадане число - " + str(number_to_guess))


def rock_scissors_paper():
    player_choice = input("Введіть свій вибір (камінь, ножиці, папір): ")

    choices = ["камінь", "ножиці", "папір"]
    computer_choice = random.choice(choices)

    print("Ваш вибір:", player_choice)
    print("Вибір комп'ютера:", computer_choice)

    if player_choice == computer_choice:
        result = "Нічия"
    elif (player_choice == "камінь" and computer_choice == "ножиці") or (
            player_choice == "ножиці" and computer_choice == "папір") or (
            player_choice == "папір" and computer_choice == "камінь"):
        result = "Ви виграли!"
    else:
        result = "Ви програли."

    return result


def capitalFrance():
    return "Столиця Франції - Париж.\n"


def fe():
    return ("Хімічний елемент з символом 'Fe' в періодичній системі елементів - це залізо.")


def get_random():
    random_number = random.randint(1, 12)
    return str(random_number)


def anagram():
    words = ["слово", "фраза", "анаграма", "код", "програмування"]

    def shuffle_word(word):
        word_list = list(word)
        random.shuffle(word_list)
        return ''.join(word_list)

    random_index = random.randint(0, len(words) - 1)
    random_word = words[random_index]

    shuffled_word = shuffle_word(random_word)

    print("Знайди анаграму:", shuffled_word)
    guess = input("Введи свою відповідь: ")

    if guess.lower() == random_word:
        return "Відповідь вірна!"
    else:
        return "Відповідь невірна. Правильне слово: " + str(random_word)


def lang():
    return ("Найбільш поширена мова у світі за кількістю носіїв - це китайська мова.")


class Bot:
    def __init__(self):
        self.f = ''
        self.branch = ''
        self.branches = {
            'математика': {
                'Площа трапеції': trapezoid,
                'Число П': pi,
                'Векторний добуток векторів': vectors},
            'фізика': {'Закон Кулона': kulon,
                       'Формула ампера': amper,
                       'Гравітаційна стала': stalaG,
                       "Кулонівська стала": stalaK,
                       },
            'географія': {'Найбільше за площею озеро': greateLake,
                          'Дві держави, які мають найбільшу кількість водосховищ в світі': pathetic_sentences,
                          'Азимут': azimut},
            'філологія': {
                          'Як утворюються питальні речення': azimut},
            'робота з текстом': {'Список всіх унікальних слів у тексті': unique,
                                 'Вміст файлу в зворотному порядку': reverse,
                                 'Найдовше речення в тексті': max_sentence,
                                 'Найдовші слова, які не містять голосних літер': vowel},
            'загальна': {'Пора року': season,
                         'Поточний місяць': month,
                         'Вгадай число між 1 та 10': guess_number_game,
                         'Камінь-ножиці-папір': rock_scissors_paper,
                         'Столиця Франції?': capitalFrance,
                         'Хімічний елемент Fe': fe,
                         'Випадкове число від 1 до 12': get_random,
                         'Гра Анаграми': anagram,
                         'Найбільш поширена мова у світі': lang}
        }

    def start(self):
        while (1):
            printBot(
                "Ви можете задати мені питання з наступних галузей: математика, фізика, географія, робота з текстом, загальна.")
            writetofile(
                "Ви можете задати мені питання з наступних галузей: математика, фізика, географія, робота з текстом, загальна.",
                self.f)
            theme = input().lower()
            writetofile(theme, self.f)
            if theme.lower() == 'вихід':
                printBot("До побачення")
                writetofile("До побачення", self.f)
                exit()
            elif theme.lower() == 'допомога':
                printBot(
                    "Ви розпочали вибір галузі. Вам потрібно обрати її та слідувати наступним інструкціям. Спробуйте!\n")
                writetofile(
                    "Ви розпочали вибір галузі. Вам потрібно обрати її та слідувати наступним інструкціям. Спробуйте!\n",
                    self.f)
            elif theme.lower() == 'назад':
                printBot("Нікуди повертатись. Це стартове меню. Для виходу напишіть вихід\n")
                writetofile("Нікуди повертатись. Це стартове меню. Для виходу напишіть вихід\n", self.f)
            else:
                if theme in self.branches.keys():
                    self.branch = theme
                    break
                else:
                    printBot("Помилка, я не знаю цієї галузі! Спробуйте ще раз її ввести.")
                    writetofile("Помилка, я не знаю цієї галузі! Спробуйте ще раз її ввести.", self.f)
        self.themes()

    def hi(self):
        printBot("Привіт, вітаю в програмі.")
        writetofile("Привіт, вітаю в програмі.", self.f)
        self.start()

    def themes(self):
        while (1):
            printBot("\nВи обрали галузь <" + self.branch + ">. Ви можете задати мені питання з наступних тем:")
            writetofile("\nВи обрали галузь <" + self.branch + ">. Ви можете задати мені питання з наступних тем:",
                        self.f)
            for text in self.branches[self.branch].keys():
                printBot("\t" + text)
                writetofile("\t" + text, self.f)
            theme = input()
            writetofile(theme, self.f)
            if theme.lower() == "вихід":
                printBot("До побачення\n")
                writetofile("До побачення\n", self.f)
                exit()
            elif theme.lower() == "допомога":
                printBot(
                    "Ви обрали галузь <" + self.branch + ">. Вам потрібно обрати тему та слідувати наступним інструкціям. Вводьте тему чітко!\n")
                writetofile(
                    "Ви обрали галузь <" + self.branch + ">. Вам потрібно обрати тему та слідувати наступним інструкціям. Вводьте тему чітко!\n",
                    self.f)
            elif theme.lower() == "назад":
                self.start()
            else:
                if theme in self.branches[self.branch].keys():
                    temp = self.branches[self.branch][theme]()
                    printBot(temp)
                    writetofile(temp, self.f)
                else:
                    printBot("Помилка, я не знаю цієї теми! Спробуйте ще раз її ввести.")
                    writetofile("Помилка, я не знаю цієї теми! Спробуйте ще раз її ввести.", self.f)


def main():
    b = datetime.datetime.now()
    date = b.strftime("%d-%m-%Y %H-%M-%S")

    bot = Bot()
    bot.f = 'dialog-' + date + '.txt'
    bot.hi()


if __name__ == '__main__':
    main()
