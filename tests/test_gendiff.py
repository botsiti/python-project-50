from gendiff.scripts.gendiff_gen import generate_diff


fl1 = 'tests/fixtures/file1.json'
fl2 = 'tests/fixtures/file2.json'
result1 = 'tests/fixtures/result1.txt'
read_result1 = open(result1, 'r')


def test_gendiff_flat():
    assert generate_diff(fl1, fl2) == read_result1.read()
