from gendiff.diff_seeker import diff_seeker
import itertools


def stringify(val, depth):
    """
    transforms values to string and translates bool & None
    values to correct JavaScript names.
    """
    if isinstance(val, bool):
        return 'true' if val else 'false'
    elif val is None:
        return 'null'
    elif type(val) != dict:
        return val
    replacer = ' '
    deep_indent_size = depth + 1
    deep_indent = deep_indent_size * replacer
    current_indent = replacer * depth
    lines = []
    if isinstance(val, dict):
        for key in val:
            lines.append(f'{deep_indent}{key}: {stringify(val.get(key), depth + 1)}')
        result = itertools.chain('{', lines, [current_indent + '}'])
        return '\n'.join(result)


def basic_indent(depth):
    size = depth * 4 - 2
    return ' ' * size


def stylish(dict1, dict2):
    """
    Compares the old and new dictionaries and builds an diff string
    If changes occur, a substring '+', '-' is added before the key: val pair.
    :param dict1: old dictionary
    :param dict2: new dictionary
    :return: diff string with of dictionaries
    """
    diff_list = diff_seeker(dict1, dict2)

    def iter_(lst, depth=0):
        lines = []
        for elem in lst:
            indent = basic_indent(depth)
            key_elem = elem['key']
            if elem['operation'] == 'add':
                new_elem = stringify(elem['new'], depth + 4)
                lines.append(f'{indent}+ {key_elem}: {new_elem}')
            elif elem['operation'] == 'remove':
                removed_elem = stringify(elem['removed'], depth + 4)
                lines.append(f'{indent}- {key_elem}: {removed_elem}')
            elif elem['operation'] == 'same':
                same_elem = stringify(elem['value'], depth + 4)
                lines.append(f'{indent}  {key_elem}: {same_elem}')
            elif elem['operation'] == 'nest':
                children = elem['value']
                inside = iter_(children, depth + 1)
                key_elem_dict = elem['key']
                lines.append(f'{indent}{key_elem_dict}: {inside}')
                depth += 1
        current_indent = ' ' * depth
        result = itertools.chain('{', lines, [current_indent + '}'])
        return '\n'.join(result)
    return iter_(diff_list, 1)
