from gendiff.diff_seeker import diff_seeker
import itertools


def stylish(file1, file2):
    values = diff_seeker(file1, file2)
    lines = []

    def iter_(lst, depth):
        for elem in lst:
            key_elem = elem['key']
            if elem['operation'] != 'nest':
                if elem['operation'] == 'add':
                    new_elem = elem['new']
                    lines.append(f' + {key_elem}: {new_elem}')
                elif elem['operation'] == 'remove':
                    rmvd_elem = elem['removed']
                    lines.append(f' - {key_elem}: {rmvd_elem}')
                elif elem['operation'] == 'same':
                    same_elem = elem['value']
                    lines.append(f'   {key_elem}: {same_elem}')
            else:
                deep_indent_size = depth + 1
                deep_indent = deep_indent_size * ' '
                current_indent = ' ' * depth
                val_elem = elem['value']
                key_elem = elem['key']
                lines.append(f'{deep_indent}{key_elem}: {iter_(val_elem, deep_indent_size)}')
                result = itertools.chain('{', lines, [current_indent + '}'])
                return '\n'.join(result)
    return iter_(values, 0)
    # result = itertools.chain('{', lines, '}')
    # return result
