#!/usr/bin/python3
from gendiff.gendiff_gen import generate_diff
from gendiff.cli import cli_diff


def main():
    first_file, second_file = cli_diff()
    print(generate_diff(first_file, second_file))


if __name__ == '__main__':
    main()
