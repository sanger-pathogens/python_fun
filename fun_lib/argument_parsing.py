import argparse


class ArgumentParserBuilder:

    @staticmethod
    def new_instance(factory=lambda: argparse.ArgumentParser()):
        return ArgumentParserBuilder(factory())

    def __init__(self, parser):
        self.parser = parser
        self.subparsers = self.parser.add_subparsers(help='sub-command help')

    def with_version(self, version):
        self.parser.add_argument(
            '--version', action='version', version=version)
        return self

    def with_counting(self, counting):
        count_parser = self.subparsers.add_parser("count", help='k-mer counting')
        count_parser.add_argument('--input', '-i', dest='input', required=True,
                                  help='Input fasta file')
        count_parser.add_argument('--output', '-o', dest='output', required=True,
                                  help='Output statistic file')
        count_parser.add_argument(
            '--size', '-s', dest='size', required=True, type=int,
            help='k-mer size/length')
        count_parser.set_defaults(func=counting)
        return self

    def build(self):
        return self.parser
