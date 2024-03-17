"""
Добавьте возможность запуска из командной строки. При этом значение любого параметра можно опустить.
В этом случае берётся первый в месяце день недели, текущий день недели и/или текущий месяц.
 *Научите функцию распознавать не только текстовое названия дня недели и месяца, но и числовые, т.е не мая, а 5
"""
import argparse
import calendar
import datetime
import locale
import logging


locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

logging.basicConfig(
    filename='log/log.log',
    format='level: {levelname}, date: {asctime}, {msg}',
    datefmt='%Y-%m-%d %H:%M:%S',
    style='{',
    level=logging.ERROR,
    encoding='UTF-8'
)
logger = logging.getLogger(__name__)

def logging_decorator(func):
    def wrapper(*args):
        res = None
        try:
            res = func(*args)
        except IndexError as e:
            logger.error(f'{e} name: {func.__name__}, args: {args}, result: {res}')
        return res
    return wrapper


days, month_ya, month_b = [['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье'],
                           ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
                            'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря'],
                           ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь',
                            'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']]


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
    # print(number_day, name_day, month)
    number_day = int(number_day.split('-')[0]) - 1
    number_day_week = days.index(name_day)
    number_month = month_ya.index(month) + 1
    # print(number_day, number_day_week, number_month)
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
    return day, month, year
    # return number, name, month


parser = argparse.ArgumentParser(description='My first argument parser')
parser.add_argument('date', metavar='NumDay', type=str, nargs='*', help='press some date')
date_args = parser.parse_args()
print(what_day(date_args.date[0]))
print(f'В скрипт передано: {date_args}')
