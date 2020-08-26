import argparse
import unittest
from unittest.mock import MagicMock

from fun_lib.argument_parsing import ArgumentParserBuilder


class TestCountParser(unittest.TestCase):

    def setUp(self):
        self.counting_function = MagicMock()
        self.under_test = ArgumentParserBuilder.new_instance(lambda: ErrorRaisingArgumentParser()) \
            .with_counting(self.counting_function) \
            .build()

    def test_count(self):
        args = self.under_test.parse_args(
            ['count', '--input', 'infile', '--output', 'outfile', '--size', '5'])
        self.assertEqual(args,
                         argparse.Namespace(func=self.counting_function, input='infile', output='outfile', size=5))

    def test_count_short_options(self):
        args = self.under_test.parse_args(
            ['count', '-i', 'infile', '-o', 'outfile', '-s', '5'])
        self.assertEqual(args,
                         argparse.Namespace(func=self.counting_function, input='infile', output='outfile', size=5))

    def test_count_input_file_missing(self):
        with self.assertRaises(ValueError) as cm:
            self.under_test.parse_args(['count', '--output', 'outfile', '--size', '5'])
        self.assertEqual(cm.exception.args[0], 'the following arguments are required: --input/-i')

    def test_count_output_file_missing(self):
        with self.assertRaises(ValueError) as cm:
            self.under_test.parse_args(['count', '--input', 'infile', '--size', '5'])
        self.assertEqual(cm.exception.args[0], 'the following arguments are required: --output/-o')

    def test_count_size_missing(self):
        with self.assertRaises(ValueError) as cm:
            self.under_test.parse_args(['count', '--input', 'infile', '--output', 'outfile'])
        self.assertEqual(cm.exception.args[0], 'the following arguments are required: --size/-s')

    def test_count_size_invalid(self):
        with self.assertRaises(ValueError) as cm:
            self.under_test.parse_args(['count', '--input', 'infile', '--output', 'outfile', '--size', 'invalid'])
        self.assertEqual(cm.exception.args[0], "argument --size/-s: invalid int value: 'invalid'")


class ErrorRaisingArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        raise ValueError(message)
