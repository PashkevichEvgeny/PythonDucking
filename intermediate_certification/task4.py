"""
Функция получает на вход текст вида: “1-й четверг ноября”, “3-я среда мая” и т.п.
Преобразуйте его в дату в текущем году.
Логируйте ошибки, если текст не соответсвует формату.
"""
import calendar
import locale
import logging
locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

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
        except IndexError as e:
            logger.error(f'{e} name: {func.__name__}, args: {args}, result: {res}')
        return res
    return wrapper


def date_to_tuple(date_string):
    names_day = [n for n in calendar.day_name]
    names_month = [n[:3] for n in calendar.month_name]

    number_week, name_day, month = date_string.split()
    number_week = int(number_week.split('-')[0]) - 1
    number_day_week = names_day.index(name_day)
    number_month = names_month.index(month[:3].capitalize())
    return number_week, number_day_week, number_month


@logging_decorator
def what_day(date_string):
    number, name, month = date_to_tuple(date_string)
    year = 2024
    cl = calendar.Calendar()
    if not cl.monthdays2calendar(year, month)[0][name][0]:
        number = number + 1
    day = cl.monthdays2calendar(2024, month)[number][name][0]
    return day, month, year


a = '1-я среда марта'
b = '2-я среда марта'
c = '3-я среда марта'
d = '4-я среда марта'
e = '5-я среда марта'
print(what_day(a), what_day(b), what_day(c), what_day(d), what_day(e))

"""
'среда марта' '5-я среда марта' '5-я среда марта'
"""