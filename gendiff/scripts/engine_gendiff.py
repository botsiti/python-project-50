from gendiff import parser, args
from gendiff import generate_diff

parser


def main():
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == '__main__':
    main()
