#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.


class Car:

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name


class TownCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = False

    def get_car(self):
        print('Автомобиль {} городского класса, {} цвет, скорость -  {}'.format(self.name, self.color, self.speed))


class SportCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = False

    def get_car(self):
        print('Автомобиль {} спортивного класса, {} цвет, скорость -  {}'.format(self.name, self.color, self.speed))


class WorkCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = False

    def get_car(self):
        print('Автомобиль {} рабочего класса, {} цвет, скорость -  {}'.format(self.name, self.color, self.speed))


class PoliceCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True

    def get_car(self):
        print('Автомобиль {} полицейского класса, {} цвет, скорость -  {}'.format(self.name, self.color, self.speed))


town_car = TownCar(130, 'красный', 'Charley')
sport_car = TownCar(256, 'желтый', 'Willey')
work_car = TownCar(46, 'фиолетовый', 'Sam')
police_car = TownCar(190, 'черный', 'Cop')

town_car.get_car()
sport_car.get_car()
work_car.get_car()
police_car.get_car()