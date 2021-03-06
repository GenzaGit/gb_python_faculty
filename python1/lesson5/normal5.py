#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import easy5 as a


def dir_tool():
    while True:
        try:
            choice = int(input('Выберите пункт:\n'
                               '1. Перейти в папку\n'
                               '2. Просмотреть содержимое текущей папки\n'
                               '3. Удалить папку\n'
                               '4. Создать папку\n'
                               'Все остальное выход из программы!\n'
                               '=========================================\n'
                               'Строка ввода: '))
        except:
            print('Выход с ошибкой')
            return

        if choice == 1:
            a.change_dir()
        elif choice == 2:
            a.look_dir()
        elif choice == 3:
            a.delete_one_dir()
        elif choice == 4:
            a.create_one_dir()
        else:
            print('Выход')
            break


dir_tool()
