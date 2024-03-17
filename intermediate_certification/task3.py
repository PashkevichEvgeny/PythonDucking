"""
Сохраняйте в лог файл раздельно:
- уровень логирования,
- дату события,
- имя функции (не декоратора),
- аргументы вызова,
- результат.
"""
import logging


logging.basicConfig(
    filename='log/log.log',
    format='level: {levelname}, date: {asctime}, {msg}',
    datefmt='%Y-%m-%d %H:%M:%S',
    style='{',
    level=logging.ERROR
)
logger = logging.getLogger(__name__)


def logging_decorator(func):
    def wrapper(*args):
        res = None
        try:
            res = func(*args)
        except ZeroDivisionError as e:
            logger.error(f'name: {func.__name__}, args: {args}, result: {res}')
        return res
    return wrapper


@logging_decorator
def division(a, b):
    return a / b


print(division(5, 0))

with open('log/log.log', 'r') as f:
    for line in f.readlines():
        print(line)
