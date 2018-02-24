#!/usr/bin/python3
# -*- coding: utf-8 -*-
# """
# == Лото ==
# Правила игры в лото.
# Игра ведется с помощью специальных карточек, на которых отмечены числа,
# и фишек (бочонков) с цифрами.
# Количество бочонков — 90 штук (с цифрами от 1 до 90).
# Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
# расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
# --------------------------
#     9 43 62          74 90
#  2    27    75 78    82
#    41 56 63     76      86
# --------------------------
# В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
# случайная карточка.
# Каждый ход выбирается один случайный бочонок и выводится на экран.
# Также выводятся карточка игрока и карточка компьютера.
# Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
# Если игрок выбрал "зачеркнуть":
# 	Если цифра есть на карточке - она зачеркивается и игра продолжается.
# 	Если цифры на карточке нет - игрок проигрывает и игра завершается.
# Если игрок выбрал "продолжить":
# 	Если цифра есть на карточке - игрок проигрывает и игра завершается.
# 	Если цифры на карточке нет - игра продолжается.
#
# Побеждает тот, кто первый закроет все числа на своей карточке.
# Пример одного хода:
# Новый бочонок: 70 (осталось 76)
# ------ Ваша карточка -----
#  6  7          49    57 58
#    14 26     -    78    85
# 23 33    38    48    71
# --------------------------
# -- Карточка компьютера ---
#  7 87     - 14    11
#       16 49    55 88    77
#    15 20     -       76  -
# --------------------------
# Зачеркнуть цифру? (y/n)
# Подсказка: каждый следующий случайный бочонок из мешка удобно получать
# с помощью функции-генератора.
# Подсказка: для работы с псевдослучайными числами удобно использовать
# модуль random: http://docs.python.org/3/library/random.html
# """


import random


class Card:

    def __init__(self, name):
        self.name = name
        print('Привет игрок, {}!'.format(self.name))
        self.card, self.line1, self.line2, self.line3 = Card.create_card(self)

    def _generate_line(self, line_except, arr, new_arr, line_range):
        double_space = '  '
        space = ' '
        line = ' '
        for i in line_range:
            if i in line_except:
                line += double_space + space
            else:
                if len(str(arr[i])) == 2:
                    line += str(arr[i]) + space
                else:
                    line += str(arr[i]) + double_space
                new_arr.append(arr[i])
        return line

    def create_card(self):

        fact_digits = []

        line1_except = random.sample(range(0, 8), 4)
        line2_except = random.sample(range(9, 17), 4)
        line3_except = random.sample(range(18, 26), 4)

        digits = random.sample(range(1, 91), 27)
        line1 = Card._generate_line(line1_except, digits, fact_digits, range(0, 9))
        line2 = Card._generate_line(line2_except, digits, fact_digits, range(9, 18))
        line3 = Card._generate_line(line3_except, digits, fact_digits, range(18, 27))

        print(' ------ Карточка {} -----\n'.format(self.name)
              + line1 + '\n' + line2 + '\n' + line3 + '\n'
              + ' --------------------------'
              )
        return fact_digits, line1, line2, line3

    def print_card(self):
        print(' ------ Карточка {} -----\n'.format(self.name)
              + self.line1 + '\n' + self.line2 + '\n' + self.line3 + '\n'
              + ' --------------------------'
              )


def game(player, enemy):
    game_digits = random.sample(range(1, 91), 90)

    for digit in game_digits:

        digit_str = str(digit)
        if player.card:
            player_case = input('{}, выпал бочонок {}, хотите зачеркнуть?'.format(player.name, digit_str)).upper()
            if digit in player.card and player_case == 'Y':
                print('Игрок {} вычеркивает значение {}'.format(player.name, digit_str))
                player.card.remove(digit)
                player.line1 = player.line1.replace(' ' + digit_str + ' ', ' -  ')
                player.line2 = player.line2.replace(' ' + digit_str + ' ', ' -  ')
                player.line3 = player.line3.replace(' ' + digit_str + ' ', ' -  ')
                player.print_card()
            else:
                print('Вы пропустили свой ход или такого хода нет!')
        else:
            print('Игрок  {}  победил!'.format(player.name))
            return

        if enemy.card:
            if digit in enemy.card:
                print('Игрок {} (компьютер) вычеркивает значение {}'.format(enemy.name, digit_str))
                enemy.card.remove(digit)
                enemy.line1 = enemy.line1.replace(' ' + digit_str + ' ', ' -  ')
                enemy.line2 = enemy.line2.replace(' ' + digit_str + ' ', ' -  ')
                enemy.line3 = enemy.line3.replace(' ' + digit_str + ' ', ' -  ')
                enemy.print_card()
        else:
            print('Игрок  {} (компьютер) победил!'.format(enemy.name))
            return


game(Card('John'), Card('Sam'))
