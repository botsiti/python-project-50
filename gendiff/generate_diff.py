import itertools
from gendiff.file_opener import file_opener
from gendiff.stylish_format import stylish


def generate_diff(file1, file2, formatter='stylish'):
    file1, file2 = file_opener(file1, file2)
    if formatter == 'stylish':
        return stylish(file1, file2)
