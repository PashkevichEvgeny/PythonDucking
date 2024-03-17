"""
На семинаре про декораторы был создан логирующий
декоратор. Он сохранял аргументы функции и результат её
работы в файл.
Напишите аналогичный декоратор, но внутри используйте
модуль logging.
"""
import logging



def logging_decorator(func):
    def wrapper(*args):
        res = None
        logging.basicConfig(
            filename='log/log.log',
            level=logging.ERROR
        )
        logger = logging.getLogger(__name__)

        try:
            res = func(*args)
        except ZeroDivisionError as e:
            logger.error(e)
        return res
    return wrapper


@logging_decorator
def division(a, b):
    return a / b


print(division(5, 2))
