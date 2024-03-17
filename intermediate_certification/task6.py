"""
Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
Соберите информацию о содержимом в виде объектов namedtuple.
Каждый объект хранит:
 - имя файла без расширения или название каталога,
 - расширение, если это файл,
 - флаг каталога,
 - название родительского каталога.
В процессе сбора сохраните данные в текстовый файл используя логирование.
"""
import argparse
import os


parser = argparse.ArgumentParser(description='My first argument parser')
parser.add_argument('path', metavar='NumDay', type=str, nargs='*', help='press some date')
date_args = parser.parse_args()

path = date_args.path[0]

for dir_path, dir_name, file_name in os.walk(path):
    print(f'{dir_path=}, {file_name=}, {dir_name=}')
