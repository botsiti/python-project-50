def diff_seeker(file1, file2):
    diff = list()
    sorted_keys = sorted(list(set(file1.keys()) | set(file2.keys())))
    for key in sorted_keys:
        if key not in file1:
            diff.append(
                {'key': key,
                 'operation': 'add',
                 'new': str(file2[key])
                 })
        elif key not in file2:
            diff.append(
                {'key': key,
                 'operation': 'remove',
                 'removed': str(file1[key])})
        elif isinstance(file1[key], dict) and isinstance(file2[key], dict):
            children = diff_seeker(file1[key], file2[key])
            diff.append(
                {'key': key,
                 'operation': 'nest',
                 'value': children})
        elif key in file1 and key in file2 and file1[key] != file2[key]:
            diff.append(
                {'key': key,
                 'operation': 'remove',
                 'removed': str(file1[key])})
            diff.append(
                {'key': key,
                 'operation': 'add',
                 'new': str(file2[key])})
        elif key in file1 and key in file2 and file1[key] == file2[key]:
            diff.append(
                {'key': key,
                 'operation': 'same',
                 'value': file1[key]})
    return diff
