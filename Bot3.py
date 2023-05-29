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
    x1 = float(input("������ x1: "))
    y1 = float(input("������ y1: "))
    z1 = float(input("������ z1: "))
    x2 = float(input("������ x2: "))
    y2 = float(input("������ y2: "))
    z2 = float(input("������ z2: "))
    return ("��������� d=" + str(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)))


def arc():
    r = float(input("������ ����� ����: "))
    teta = float(input("������ ��� �� ����� ������� �� ���: "))
    return ("��������� L=" + str(r * teta))


def point2d():
    x1 = float(input("������ x1: "))
    y1 = float(input("������ y1: "))
    x2 = float(input("������ x2: "))
    y2 = float(input("������ y2: "))
    return ("��������� d=" + str(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)))


def trapezoid():
    a = float(input("������ ������� �: "))
    b = float(input("������ ������� b: "))
    h = float(input("������ ������� h: "))
    S = 0.5 * (a + b) * h
    return ("��������� S=" + str(S))


def pi():
    return ("����� �=" + str(math.pi))


def vectors():
    Ax = float(input("������ ���������� x ��� ������� A: "))
    Ay = float(input("������ ���������� y ��� ������� A: "))
    Az = float(input("������ ���������� z ��� ������� A: "))
    Bx = float(input("������ ���������� x ��� ������� B: "))
    By = float(input("������ ���������� y ��� ������� B: "))
    Bz = float(input("������ ���������� z ��� ������� B: "))
    result = [
        Ay * Bz - Az * By,
        Az * Bx - Ax * Bz,
        Ax * By - Ay * Bx
    ]

    return '��������� ������� A x B: '+str(result)


def kulon():
    k = 8.9875 * (10 ** 9)
    q1 = float(input("������ q1: "))
    q2 = float(input("������ q2: "))
    r = float(input("������ r: "))
    return ('��������� F=' + str(k * q1 * q2 * r))


def amper():
    m = 4 * math.pi * 10 ** -7
    I = float(input("������ I: "))
    r = float(input("������ r: "))
    B = (m * I) / (2 * math.pi * r)
    return ('��������� B=' + str(B) + '��')


def stalaG():
    return ("�������� ����������� ����� (G) ��������� ������� 6.67430(15) ? 10^(-11) ͷ�?/��?")


def stalaK():
    return ("�������� ���������� ����� ?? ��������� ������� 8.8541878128(13) ? 10^(-12) �/�.")


def greateLake():
    return ("�������� ����� � ��� �� ������ - �� ��������� ����")


def watershed():
    return ("�� �������, �� ����� �������� ������� ���������� � ���, �� ����� 404 �� ������ (Canada)")


def pathetic_sentences():
    return ("������� ������� � ��������� ��� ���������� ������ ��������� ���������� 䳺����� ����� ������� ��� �� ��������� ������ ������� ���.")

def azimut():
    x1=float(input("������ ���������� x ��� ����� �: "))
    y1=float(input("������ ���������� y ��� ����� �: "))
    x2=float(input("������ ���������� x ��� ����� �: "))
    y2=float(input("������ ���������� y ��� ����� �: "))

    dx = x2 - x1
    dy = y2 - y1

    azimuth_rad = math.atan2(dy, dx)
    azimuth_deg = math.degrees(azimuth_rad)

    azimuth_deg = (azimuth_deg + 360) % 360

    return ("������ ������� "+str(azimuth_deg))


def unique():
    input_filename = input("������ ��'� �������� �����: ")
    output_filename = input("������ ��'� ��������� �����: ")

    try:
        with open(input_filename, 'r', encoding='utf-8') as input_file:
            content = input_file.read()

        text = re.sub(r'[^\w\s]', '', content)
        words = text.split()

        words = [word.lower() for word in words]

        unique_words = str(list(set(words)))

        with open(output_filename, 'w', encoding='utf-8') as output_file:
            output_file.write(unique_words)

        return ("��������� ��� ��������� � ���� " + output_filename)
    except FileNotFoundError:
        return ("�������: ���� �� ��������.")
    except Exception as e:
        return ("�������: ������� ������� ��� ������� �����." + str(e))


def reverse():
    input_filename = input("������ ��'� �������� �����: ")

    try:
        with open(input_filename, 'r', encoding='utf-8') as input_file:
            content = input_file.read()

        reversed_lines = list(reversed(content))

        return "ʳ������ ������ � �����: " + str(reversed_lines)
    except FileNotFoundError:
        return ("�������: ���� �� ��������.")
    except:
        return ("�������: ������� ������� ��� ������� �����.")


def max_sentence():
    input_filename = input("������ ��'� �������� �����: ")

    try:
        with open(input_filename, 'r', encoding='utf-8') as input_file:
            content = input_file.read()

        sentences = content.split('. ')
        longest_sentence = max(sentences, key=len)
        return ("�������� ������� � �����: " + str(longest_sentence))
    except FileNotFoundError:
        return ("�������: ���� �� ��������.")
    except:
        return ("�������: ������� ������� ��� ������� �����.")


def vowel():
    input_filename = input("������ ��'� �������� �����: ")
    output_filename = input("������ ��'� ��������� �����: ")

    try:
        with open(input_filename, 'r', encoding='utf-8') as input_file:
            content = input_file.read()

        words = content.split()
        longest_words = []

        for word in words:
            if all(letter.lower() not in 'aeiou��賿����' for letter in word):
                if not longest_words or len(word) > len(longest_words[0]):
                    longest_words = [word]
                elif len(word) == len(longest_words[0]):
                    longest_words.append(word)

        with open(output_filename, 'w', encoding='utf-8') as output_file:
            output_file.write(str(longest_words))

        return ("��������� ��� ��������� � ����" + output_filename)
    except FileNotFoundError:
        return ("�������: ���� �� ��������.")
    except:
        return ("�������: ������� ������� ��� ������� �����.")


def season():
    now = datetime.datetime.now()
    month = now.month

    if month in range(3, 6):
        current_season = "�����"
    elif month in range(6, 9):
        current_season = "���"
    elif month in range(9, 12):
        current_season = "����"
    else:
        current_season = "����"

    return "������� ���� ����- " + str(current_season)


def month():
    now = datetime.datetime.now()
    current_month = now.strftime("%B")

    return "�������� ����� - " + str(current_month)


def guess_number_game():
    number_to_guess = random.randint(1, 10)
    attempts = 0

    printBot("��� '������ ����� �� 1 �� 10'")
    printBot("� ������� �����. ��������� �������!")

    while True:
        guess = int(input("������ ���� �������: "))
        attempts += 1

        if guess == number_to_guess:
            return ("³���! �� ������� �����" + str(number_to_guess) + "��" + str(attempts) + "�����!")
        else:
            return ("�� ����, �� �� �������. �������� ����� - " + str(number_to_guess))


def rock_scissors_paper():
    player_choice = input("������ ��� ���� (�����, ������, ����): ")

    choices = ["�����", "������", "����"]
    computer_choice = random.choice(choices)

    print("��� ����:", player_choice)
    print("���� ����'�����:", computer_choice)

    if player_choice == computer_choice:
        result = "ͳ���"
    elif (player_choice == "�����" and computer_choice == "������") or (
            player_choice == "������" and computer_choice == "����") or (
            player_choice == "����" and computer_choice == "�����"):
        result = "�� �������!"
    else:
        result = "�� ��������."

    return result


def capitalFrance():
    return "������� ������� - �����.\n"


def fe():
    return ("ճ����� ������� � �������� 'Fe' � ��������� ������ �������� - �� �����.")


def get_random():
    random_number = random.randint(1, 12)
    return str(random_number)


def anagram():
    words = ["�����", "�����", "��������", "���", "�������������"]

    def shuffle_word(word):
        word_list = list(word)
        random.shuffle(word_list)
        return ''.join(word_list)

    random_index = random.randint(0, len(words) - 1)
    random_word = words[random_index]

    shuffled_word = shuffle_word(random_word)

    print("������ ��������:", shuffled_word)
    guess = input("����� ���� �������: ")

    if guess.lower() == random_word:
        return "³������ ����!"
    else:
        return "³������ ������. ��������� �����: " + str(random_word)


def lang():
    return ("������� �������� ���� � ��� �� ������� ���� - �� ��������� ����.")


class Bot:
    def __init__(self):
        self.f = ''
        self.branch = ''
        self.branches = {
            '����������': {
                '����� ��������': trapezoid,
                '����� �': pi,
                '��������� ������� �������': vectors},
            '������': {'����� ������': kulon,
                       '������� ������': amper,
                       '����������� �����': stalaG,
                       "���������� �����": stalaK,
                       },
            '���������': {'�������� �� ������ �����': greateLake,
                          '�� �������, �� ����� �������� ������� ���������� � ���': pathetic_sentences,
                          '������': azimut},
            '��������': {
                          '�� ����������� ������� �������': azimut},
            '������ � �������': {'������ ��� ��������� ��� � �����': unique,
                                 '���� ����� � ���������� �������': reverse,
                                 '�������� ������� � �����': max_sentence,
                                 '�������� �����, �� �� ������ �������� ����': vowel},
            '��������': {'���� ����': season,
                         '�������� �����': month,
                         '������ ����� �� 1 �� 10': guess_number_game,
                         '�����-������-����': rock_scissors_paper,
                         '������� �������?': capitalFrance,
                         'ճ����� ������� Fe': fe,
                         '��������� ����� �� 1 �� 12': get_random,
                         '��� ��������': anagram,
                         '������� �������� ���� � ���': lang}
        }

    def start(self):
        while (1):
            printBot(
                "�� ������ ������ ��� ������� � ��������� �������: ����������, ������, ���������, ������ � �������, ��������.")
            writetofile(
                "�� ������ ������ ��� ������� � ��������� �������: ����������, ������, ���������, ������ � �������, ��������.",
                self.f)
            theme = input().lower()
            writetofile(theme, self.f)
            if theme.lower() == '�����':
                printBot("�� ���������")
                writetofile("�� ���������", self.f)
                exit()
            elif theme.lower() == '��������':
                printBot(
                    "�� ��������� ���� �����. ��� ������� ������ �� �� �������� ��������� �����������. ���������!\n")
                writetofile(
                    "�� ��������� ���� �����. ��� ������� ������ �� �� �������� ��������� �����������. ���������!\n",
                    self.f)
            elif theme.lower() == '�����':
                printBot("ͳ���� �����������. �� �������� ����. ��� ������ �������� �����\n")
                writetofile("ͳ���� �����������. �� �������� ����. ��� ������ �������� �����\n", self.f)
            else:
                if theme in self.branches.keys():
                    self.branch = theme
                    break
                else:
                    printBot("�������, � �� ���� ���� �����! ��������� �� ��� �� ������.")
                    writetofile("�������, � �� ���� ���� �����! ��������� �� ��� �� ������.", self.f)
        self.themes()

    def hi(self):
        printBot("�����, ���� � �������.")
        writetofile("�����, ���� � �������.", self.f)
        self.start()

    def themes(self):
        while (1):
            printBot("\n�� ������ ������ <" + self.branch + ">. �� ������ ������ ��� ������� � ��������� ���:")
            writetofile("\n�� ������ ������ <" + self.branch + ">. �� ������ ������ ��� ������� � ��������� ���:",
                        self.f)
            for text in self.branches[self.branch].keys():
                printBot("\t" + text)
                writetofile("\t" + text, self.f)
            theme = input()
            writetofile(theme, self.f)
            if theme.lower() == "�����":
                printBot("�� ���������\n")
                writetofile("�� ���������\n", self.f)
                exit()
            elif theme.lower() == "��������":
                printBot(
                    "�� ������ ������ <" + self.branch + ">. ��� ������� ������ ���� �� �������� ��������� �����������. ������� ���� �����!\n")
                writetofile(
                    "�� ������ ������ <" + self.branch + ">. ��� ������� ������ ���� �� �������� ��������� �����������. ������� ���� �����!\n",
                    self.f)
            elif theme.lower() == "�����":
                self.start()
            else:
                if theme in self.branches[self.branch].keys():
                    temp = self.branches[self.branch][theme]()
                    printBot(temp)
                    writetofile(temp, self.f)
                else:
                    printBot("�������, � �� ���� ���� ����! ��������� �� ��� �� ������.")
                    writetofile("�������, � �� ���� ���� ����! ��������� �� ��� �� ������.", self.f)


def main():
    b = datetime.datetime.now()
    date = b.strftime("%d-%m-%Y %H-%M-%S")

    bot = Bot()
    bot.f = 'dialog-' + date + '.txt'
    bot.hi()


if __name__ == '__main__':
    main()
