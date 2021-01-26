# loto
'''
== Лото ==

Правила игры в лото.

Игра ведется с помощью спе циальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
    Если цифра есть на карточке - она зачеркивается и игра продолжается.
    Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
    Если цифра есть на карточке - игрок проигрывает и игра завершается.
    Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html
'''

from random import randint, shuffle

'''создать список списков из 3 элементов по 9 значений, 5 значений это числа от 1 до 90, все 15 чисел уникальны
12 нулей в списке списков, по 4 в списке, при этом 3 нуля с одинаковым индексом не допусается, и в списках 
на одном индексе должен быть хоть один ноль
'''
class Card:
    def __init__(self, name):
        self.__row_90 = [element for element in range(1, 91)]
        self.card_row = [[], [], []]
        self.generate_card()
        self.__name = name if len(name) else 'Vasyula'

    def more_spaces(self, line_one, line_two, line_three):
        while line_one.count(' ') < 4:
            rand_number = randint (0, 8)
            if (line_two[rand_number] == ' ' and line_three[rand_number] == ' '):
                continue
            else:
                line_one[rand_number] = ' '
        return line_one

    def generate_card(self):
        for element in range (0, 63, 7):
            (self.card_row[0]).append (self.__row_90.pop (randint (element, (element + 9) if element < 53
            else (element + 9))))
            (self.card_row[1]).append (self.__row_90.pop (randint (element, (element + 8) if element < 53
            else (element + 8))))
            (self.card_row[2]).append (self.__row_90.pop (randint (element, (element + 7) if element < 53
            else (element + 7))))
        '''
        раскидываем первые 9 пробелов рандомно по рядам
        '''
        for count in range (9):
            rand_number = randint (1, 3)
            if (rand_number == 1 and (self.card_row[0]).count (' ') < 4):
                (self.card_row[0])[count] = ' '
            elif (rand_number == 2 and (self.card_row[1]).count (' ') < 4):
                (self.card_row[1])[count] = ' '
            elif (rand_number == 3 and (self.card_row[2]).count (' ') < 4):
                (self.card_row[2])[count] = ' '
        '''
        Добиваем чтобы в каждом ряду было не менее 4 пробела, с условием чтобы не было рядом три пробела сверху-вниз
        '''
        for count in range (3):
            self.more_spaces (self.card_row[count], self.card_row[(count - 2) if count == 2 else (count + 1)],
                              self.card_row[(count + 2) if count == 0 else (count - 1)])

    def __str__(self):
        show_view = '-Карточка игрока ' + self.__name + '--' + '\n'
        for line in self.card_row:
            answer = ''
            for element in line:
                if len (str (element)) == 2:
                    answer += ''.join (str (element)) + ' '
                else:
                    answer += ' ' + ''.join (str (element)) + ' '
            show_view += answer + '\n'
        show_view += '--------------------------' + '\n'
        return show_view

class Game:
    def __init__(self, cls_one, cls_two):
        self.gamer_one = cls_one
        self.gamer_two = cls_two
        self.__barrel = []
        self.generate_barrel()
        self.start_game()


    def generate_barrel(self):
        self.__barrel = [element for element in range (1, 91)]
        shuffle(self.__barrel)

    def start_game(self):
        for count in range(len(self.__barrel)):
            small_barrel = self.__barrel.pop()
            print (f'Новый бочонок: {small_barrel} осталось {len(self.__barrel)}')
            print (self.gamer_one)
            print (self.gamer_two)
            answer_user = input('Зачеркнуть цифру? (y/n)').lower()
            if (answer_user == 'y') and (small_barrel in self.gamer_one.card_row):
                print ('ura')


card_user = Card(input('Введите ваше имя '))
card_comp = Card('Компьютер')
game = Game(card_user, card_comp)



