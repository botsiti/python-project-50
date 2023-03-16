import json
import itertools
j1 = json.load(open('file1.json'))
j2 = json.load(open('file2.json'))

def generate_diff(file1, file2):
    # file1 = json.load(open(fl1))
    # file2 = json.load(open(fl2))
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






print(generate_diff(j1, j2))





