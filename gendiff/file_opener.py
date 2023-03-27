import json
import yaml


def file_opener(file1, file2):
    if file1.endswith('.json'):
        file1 = json.load(open(file1))
    elif file1.endswith('.yaml') or file1.endswith('yml'):
        file1 = yaml.safe_load(open(file1, 'r'))
    else:
        raise ValueError('Invalid format')

    if file2.endswith('.json'):
        file2 = json.load(open(file2))
    elif file2.endswith('yaml') or file2.endswith('yml'):
        file2 = yaml.safe_load(open(file2, 'r'))
    else:
        raise ValueError('Invalid format')
    return file1, file2
