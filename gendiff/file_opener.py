import json
import yaml
"""
opens json and yaml files and returns them open
"""


def file_opener(file1, file2):
    def inner_(file):
        if file.endswith('.json'):
            file = json.load(open(file))
        elif file.endswith('.yaml') or file.endswith('.yml'):
            file = yaml.safe_load(open(file, 'r'))
        else:
            raise ValueError('Invalid format')
        return file
    file1 = inner_(file1)
    file2 = inner_(file2)
    return file1, file2
