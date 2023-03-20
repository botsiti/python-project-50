from gendiff import generate_diff


def test_gendiff():
    fl1 = 'fixtures/file1.json'
    fl2 = 'fixtures/file2.json'
    result = 'fixtures/test1_result'
    assert generate_diff(fl1, fl2) == result
