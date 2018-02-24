# -*- coding: utf-8 -*-
import sys

from socket import socket, AF_INET, SOCK_STREAM
from jim.utils import send_message, get_message
from jim.config import *


def presence_response(presence_message):
    # Делаем проверки
    if ACTION in presence_message and \
            presence_message[ACTION] == PRESENCE and \
            TIME in presence_message and \
            isinstance(presence_message[TIME], float):
        # Если всё хорошо шлем ОК
        return {RESPONSE: 200}
    else:
        # Шлем код ошибки
        return {RESPONSE: 400, ERROR: 'Не верный запрос'}


if __name__ == '__main__':
    server = socket(AF_INET, SOCK_STREAM)  # Создает сокет TCP
    # Получаем аргументы скрипта
    try:
        addr = sys.argv[1]
    except IndexError:
        addr = ''
    try:
        port = int(sys.argv[2])
    except IndexError:
        port = 7777
    except ValueError:
        print('Порт должен быть целым числом')
        sys.exit(0)

    server.bind((addr, port))  # Присваивает порт 8888
    server.listen(5)
    while True:
        client, addr = server.accept()  # Принять запрос на соединение
        # получаем сообщение от клиента
        presence = get_message(client)
        print(presence)
        # формируем ответ
        response = presence_response(presence)
        # отправляем ответ клиенту
        send_message(client, response)
        client.close()
