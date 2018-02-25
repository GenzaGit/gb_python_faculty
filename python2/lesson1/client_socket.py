# -*- coding: utf-8 -*-

from socket import *
from jim.config import *
from jim.utils import send_message, get_message
from errors import UsernameToLongError, ResponseCodeLenError, MandatoryKeyError, ResponseCodeError
import sys
import time


def create_presence(name='Guest'):
    CUR_TIME = time.time()
   
    if len(name) > 20:
        raise UsernameToLongError
    if isinstance(name, int):
        raise TypeError
    res = {
        ACTION: PRESENCE,
        TIME: CUR_TIME,
        USER: {
            ACCOUNT_NAME: name
        }
    }
    return res


def translate_message(message):
    if not isinstance(message, dict):
        raise TypeError
    for key in message.keys():
        if key not in KEY_TUPLE:
            raise MandatoryKeyError
    if len(str(message[RESPONSE])) != 3:
        raise ResponseCodeLenError
    if message[RESPONSE] not in RESPONSE_CODES:
        raise ResponseCodeError

    return message


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

    message = create_presence(None)
    server.connect((addr, port))
    send_message(server, message)
    response = get_message(server)
    res_response = translate_message(response)
    print('Ответ сервера {}'.format(res_response))
    server.close()
