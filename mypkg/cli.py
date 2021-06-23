import argparse
import sys

from mypkg.some_class import SomeClass


def parse_args(args):
    """
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--date")
    parser.add_argument("-n", "--number", help="message", type=int, default=1)
    parser.add_argument("-t", "--test", action="store_true")
    return parser.parse_args(args)


def main():
    """
    """
    args = parse_args(sys.argv[1:])
    mypkg = SomeClass(args)
    mypkg.run()


if __name__ == "__main__":
    main()
