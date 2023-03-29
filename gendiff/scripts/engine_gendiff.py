#!/usr/bin/python3
from gendiff.generate_diff import generate_diff
from gendiff.cli import cli_diff


def main():
    args = cli_diff()
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
