#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, persoтn2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.
player_name = input('Введите свое имя: ')
enemy_name = input('Как думаешь, кто твой враг? ')

player = {'name': player_name, 'health': 100, 'damage': 50, 'armor': 1.2}
enemy = {'name': enemy_name, 'health': 120, 'damage': 30, 'armor': 1.2}


def write_file(person):
    with open(str(person['name']) + '.txt', 'w') as file:
        for index, value in person.items():
            file.write(str(index) + ' - ' + str(value) + '\n')
    return file.name


def read_file(person_filename):
    keys = []
    values = []
    with open(person_filename) as file:
        for line in file:
            keys.append(line.split(' - ')[0])
            if line.split(' - ')[0] == 'name':
                values.append(line.split(' - ')[1].strip())
            else:
                values.append(float(line.split(' - ')[1].strip()))
    return dict(zip(keys, values))


def attack(person1, person2):
    while True:
        if person2['health'] > 0:
            person1['health'] = person1['health'] - round(person2['damage'] / person1['armor'], 1)
            print(
                'После атаки игрока {} уровень жизни игрока {} опустился до {}'.format(person2['name'], person1['name'],
                                                                                       round(person1['health'], 1)))
        else:
            print('Победил игрок {}!!! ({} очков жизней)'.format(person1['name'], round(person1['health'], 1)))
            break

        if person1['health'] > 0:
            person2['health'] = person2['health'] - round(person1['damage'] / person2['armor'], 1)
            print('Ответный удар по щиту - {} урона!!! Уровень жизни {} составляет {}'.format(
                round(person1['damage'] / person2['armor'], 1), person2['name'], round(person2['health'], 1)))
        else:
            print('Победил игрок {}!!! ({} очков жизней)'.format(person2['name'], round(person2['health'], 1)))
            break


player_filename = write_file(player)
enemy_filename = write_file(enemy)

player = read_file(player_filename)
enemy = read_file(enemy_filename)

attack(player, enemy)

# def attack1(person1, person2):
#     person1['health'] = person1['health'] - person2['damage']
#     print('После атаки игрока {} уровень жизни игрока {} опустился до {}'.format(person2['name'], person1['name'],
#                                                                                  person1['health']))
#     person2['health'] = person2['health'] - person1['damage']
#     print('Сокрушительные ответный удар - {} урона!!!'.format(person1['damage']))
#
#
# attack1(player, enemy)


# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.

# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.

# def attack2(person1, person2):
#     print('Наши герои получили щиты! Посмотрим что будет!')
#     person1['health'] = person1['health'] - round(person2['damage'] / person1['armor'], 1)
#     print('После атаки игрока {} уровень жизни игрока {} опустился до {}'.format(person2['name'], person1['name'],
#                                                                                  person1['health']))
#     person2['health'] = person2['health'] - round(person1['damage'] / person2['armor'], 1)
#     print('Ответный удар по щиту - {} урона!!!'.format(round(person1['damage'] / person2['armor'], 1)))
#
#
# attack2(player, enemy)
