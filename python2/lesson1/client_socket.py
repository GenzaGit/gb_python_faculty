# -*- coding: utf-8 -*-
from socket import *
from jim.utils import get_message, send_message
import sys
from jim.config import *
from datetime import datetime

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

    time_float = float(datetime.now().microsecond)
    server.connect((addr, port))
    message = {ACTION: PRESENCE,
               TIME: time_float,
               ACCOUNT_NAME: 'Dmitry Seregin',
               RESPONSE: 'Give me Time, server!',
               USER: 'Admin',
               ERROR: None}
    send_message(server, message)
    response = get_message(server)['response']
    print("Ответ сервера {}".format(response))
    server.close()
