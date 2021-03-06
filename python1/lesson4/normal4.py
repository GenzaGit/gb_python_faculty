#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

# Эти задачи необходимо решить используя регулярные выражения!

# Задача - 1
# Запросите у пользователя имя, фамилию, email. Теперь необходимо совершить проверки, имя и фамилия должны иметь \
# заглавные первые буквы.
# email - не должен иметь заглавных букв и должен быть в формате: текст в нижнем регистре, допускается нижнее \
#  подчеркивание и цифры, потом @, потом текст, допускаются цифры, точка, ru или org или com.
# Например:
# Пупкин василий - неверно указано имя, te$T@test.net - неверно указан email (спецсимвол, заглавная буква, .net), \
#  te_4_st@test.com - верно указан.

name, last_name, email = input('Введите имя, фамилию и эл. почту через пробел: ').split()

if re.match('^[a-z0-9_]+[^A-Z]@[a-z0-9_]+.(ru|org|com)$', email):
    print(email + ' - верно указан e-mail')
else:
    print(email + ' - НЕ верно указан e-mail')

if re.match('^[А-Я][а-я]+$', name) and re.match('^[А-Я][а-я]+$', last_name):
    print(name, last_name, '- имя и фамилия указаны верно')
elif re.match('^[А-Я][а-я]+$', last_name):
    print(name, last_name, '- имя указано НЕ верно')
elif re.match('^[А-Я][а-я]+$', name):
    print(name, last_name, '- фамилия указана НЕ верно')
else:
    print(name, last_name, '- имя и фамилия указаны НЕ верно')

# Задача - 2:
# Вам дан текст:

some_str = '''
Мороз и солнце; день чудесный!
Еще ты дремлешь, друг прелестный —
Пора, красавица, проснись:
Открой сомкнуты негой взоры
Навстречу северной Авроры,
Звездою севера явись!
Вечор, ты помнишь, вьюга злилась,
На мутном небе мгла носилась;
Луна, как бледное пятно,
Сквозь тучи мрачные желтела,
И ты печальная сидела —
А нынче... погляди в окно:
Под голубыми небесами
Великолепными коврами,
Блестя на солнце, снег лежит;
Прозрачный лес один чернеет,
И ель сквозь иней зеленеет,
И речка подо льдом блестит.
Вся комната янтарным блеском
Озарена. Веселым треском
Трещит затопленная печь.
Приятно думать у лежанки.
Но знаешь: не велеть ли в санки
Кобылку бурую запречь?
Скользя по утреннему снегу,
Друг милый, предадимся бегу
Нетерпеливого коня
И навестим поля пустые,
Леса, недавно столь густые,
И берег, милый для меня.'''

if re.search('\.{2,}', some_str):
    print('В строке встречается более одной точки подряд!')
else:
    print('В строке НЕ встречается более одной точки подряд!')
# Необходимо с помощью регулярных выражений определить есть ли в тексте подряд
# более одной точки, при любом исходе сообщите результат пользователю!
