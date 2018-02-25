class UsernameToLongError(Exception):

    def __init__(self):
        pass

    def __str__(self):
        return 'Имя должно содержать не более 20 символов'


class ResponseCodeLenError(Exception):

    def __init__(self):
        pass

    def __str__(self):
        return 'Код должен содержать 3 символа'


class MandatoryKeyError(Exception):

    def __init__(self):
        pass

    def __str__(self):
        return 'Такого ключа нет в конфиге'


class ResponseCodeError(Exception):

    def __init__(self):
        pass

    def __str__(self):
        return 'Такого кода ответа нет в конфиге'
