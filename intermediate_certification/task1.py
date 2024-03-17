"""
Напишите программу которая использует модуль logging для
вывода сообщения об ошибке в файл.
Например отлавливаем ошибку деления на ноль.
"""
import logging


logging.basicConfig(
    filename='log/log.log',
    # encoding='utf-8',
    format='{asctime} {levelname} {funcName}->{lineno}: {msg}',
    style='{',
    level=logging.ERROR)

logger = logging.getLogger(__name__)


def division(a, b):
    res = None
    try:
        res = a / b
    except ZeroDivisionError as e:
        logger.error(e)
    return res


print(division(5, 0))

with open('log/log.log', 'r') as f:
    for line in f.readlines():
        print(line)
