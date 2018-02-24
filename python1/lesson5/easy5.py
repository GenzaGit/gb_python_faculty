#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os


def create_dir():
    print('Создаем папки')
    for i in range(9):
        os.mkdir('dir_' + str(i + 1))


def delete_dir():
    print('Удаляем папки')
    for i in range(9):
        os.rmdir('dir_' + str(i + 1))


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def current_dir():
    current_path = '.'
    for dir in os.listdir(current_path):
        print(dir)


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copy_run_file():
    name_run_file = os.path.basename(__file__)
    command_str = 'cp ' + name_run_file + ' copy_' + name_run_file
    if os.path.isfile('copy_' + name_run_file):
        print('Такой файл уже существует')
    else:
        os.system(command_str)


# --------------------------------------------------------------------------
# Скрипты для normal5.py
def change_dir():
    сur_dir = os.getcwd()
    print('Вы находитесь в директории', сur_dir, '\n')
    path = input('Введите путь до директории: ')
    if os.path.exists(path):
        os.chdir(path)
        сur_dir = os.getcwd()
        print('Вы перешли в', сur_dir, '\n')
    else:
        print('Такой директории не существует\n')


def look_dir():
    current_path = '.'
    for dir_name in os.listdir(current_path):
        print(dir_name)


def create_one_dir():
    dir_name = input('Создать директорию с именем: ')
    if os.path.isdir(dir_name):
        print('Директория с таким именем уже существует\n')
    else:
        os.mkdir(dir_name)
        print('Директория создана!\n')


def delete_one_dir():
    dir_name = input('Удалить директорию с именем: ')
    if os.path.isdir(dir_name):
        os.rmdir(dir_name)
        print('Директория удалена!\n')
    else:
        print('Такой директории не существует\n')
