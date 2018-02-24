#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.


class Person:

    def __init__(self, health, damage, armor, name):
        self.health = health
        self.damage = damage
        self.armor = armor
        self.name = name

    def attack(self, target):
        if target.armor < 0 or target.armor > 1:
            print('Неправильно выбрана броня')
            return
        else:
            damage = self.damage
            target.health -= damage * target.armor

        if target.health > 0:
            print('Атака игрока {}'.format(self.name))
        else:
            print('Победил игрок {}!!!'.format(self.name))
        print('Здоровье игрока {} стало {}'.format(target.name, target.health))
        return target.health


class Player(Person):

    def __init__(self, health, damage, armor, name):
        super().__init__(health, damage, armor, name)


class Enemy(Person):

    def __init__(self, health, damage, armor, name):
        super().__init__(health, damage, armor, name)


player = Player(120, 30, 0.4, 'Kelly')
enemy = Enemy(150, 20, 0.25, 'Den')

while enemy.attack(player) > 0 and player.attack(enemy) > 0:
    enemy.attack(player)
    player.attack(enemy)
