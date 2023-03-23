import json
import itertools
import yaml


def generate_diff(file1, file2):  # noqa: C901
    if file1.endswith('.json') and file2.endswith('.json'):
        file1 = json.load(open(file1))
        file2 = json.load(open(file2))
    elif file1.endswith('.yml') or file1.endswith('.yaml') \
            and file2.endswith('.yaml') or file2.endswith('yml'):
        file1 = yaml.safe_load(open(file1, 'r'))
        file2 = yaml.safe_load(open(file2, 'r'))

    keys = file1.keys() | file2.keys()
    lines = []
    for key in sorted(keys):
        if key not in file1:
            lines.append(f' + {key} : {file2[key]}')
        elif key not in file2:
            lines.append(f' - {key}: {file1[key]}')
        elif key in file1 and key in file2 and file1[key] != file2[key]:
            lines.append(f' - {key}: {file1[key]}')
            lines.append(f' + {key}: {file2[key]}')
        elif file1[key] == file2[key]:
            lines.append(f'   {key}: {file1[key]}')
        else:
            lines.append(f'   {key}: {file2[key]}')
        result = itertools.chain('{', lines, '}')
    return '\n'.join(result)
