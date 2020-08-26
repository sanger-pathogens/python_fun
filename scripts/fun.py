#!/usr/bin/env python3

import enum
import sys

from fun_lib.argument_parsing import ArgumentParserBuilder
from fun_lib.main import count, fun_version


class Action(enum.Enum):
    count = 1


def main():
    parser = ArgumentParserBuilder.new_instance() \
        .with_counting(Action.count) \
        .with_version(fun_version()) \
        .build()
    arguments = dict(vars(parser.parse_args()))
    if arguments['func'] == Action.count:
        count(arguments['input'], arguments['output'], arguments['size'])
    else:
        parser.print_help()


if __name__ == '__main__':
    sys.exit(main())
