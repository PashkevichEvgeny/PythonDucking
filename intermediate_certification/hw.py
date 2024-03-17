"""
Решить задачи, которые не успели решить на семинаре.
Возьмите любые 1-3 задачи из прошлых домашних заданий.
Добавьте к ним логирование ошибок и полезной информации.
Также реализуйте возможность запуска из командной строки с передачей параметров.
"""
import argparse
import calendar
import datetime
import locale
import logging
from os.path import dirname, join

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')


def logging_decorator(func):
    logging.basicConfig(
        filename=join(dirname(__file__), 'log', 'log.log'),
        format='level: {levelname}, date: {asctime}, {msg}',
        datefmt='%Y-%m-%d %H:%M:%S',
        style='{',
        level=logging.ERROR,
        encoding='UTF-8'
    )
    logger = logging.getLogger(__name__)

    def wrapper(*args):
        res = None
        try:
            res = func(*args)
        except IndexError as e:
            logger.error(f'{e} name: {func.__name__}, args: {args}, result: {res}')
        return res
    return wrapper


parser = argparse.ArgumentParser(description='Parser string date to format %d-%m-%y')
parser.add_argument('str_date', metavar='StrDate', type=str, nargs=1, help='enter date, like: "1-й вторник марта"')
date_args = parser.parse_args().str_date[0]

days = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
month_ya = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
month_b = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']


def shorten_date(date_string):
    lst = date_string.split()
    number_day = '1'
    name_day, month = map(str.lower, datetime.datetime.now().strftime('%A %B').split())
    month = month_ya[month_b.index(month)]
    if len(lst) == 3:
        return tuple(map(str.lower, lst))
    for n in lst:
        if '-' in n:
            number_day = n
        elif n in days:
            name_day = n
        elif n in month_ya or n in month_b:
            month = n
    return tuple(map(str.lower, [number_day, name_day, month]))


def date_to_tuple(date_string):
    number_day, name_day, month = shorten_date(date_string)
    number_day = int(number_day.split('-')[0]) - 1
    number_day_week = days.index(name_day)
    number_month = month_ya.index(month) + 1
    return number_day, number_day_week, number_month


@logging_decorator
def what_day(date_string):
    number, name, month = date_to_tuple(date_string)
    year = 2024
    cl = calendar.Calendar()
    if not cl.monthdays2calendar(year, month)[0][name][0]:
        number = number + 1
    if not cl.monthdays2calendar(year, month)[number][name][0]:
        number = number + 1
    day = cl.monthdays2calendar(year, month)[number][name][0]
    return f'{day}-{month}-{year}'


print(what_day(date_args))
