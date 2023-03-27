from gendiff.gendiff_gen import generate_diff


fl1 = 'tests/fixtures/file1.json'
fl2 = 'tests/fixtures/file2.json'
result1 = 'tests/fixtures/result1.txt'
read_result1 = open(result1, 'r')
fl1_yaml = 'tests/fixtures/file1.yml'
fl2_yaml = 'tests/fixtures/file2.yaml'
yaml_result = open('tests/fixtures/result2.txt', 'r')


def test_gendiff_flat_json():
    assert generate_diff(fl1, fl2) == read_result1.read()


def test_gendiff_flat_yaml():
    assert generate_diff(fl1_yaml, fl2_yaml) == yaml_result.read()
