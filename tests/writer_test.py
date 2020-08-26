import io
import unittest

from fun_lib.writer import write_stats_to_stream


class TestWriteStats(unittest.TestCase):

    def setUp(self) -> None:
        self.test_stream = io.StringIO()

    def test_should_write_output(self):
        write_stats_to_stream([("A", 1), ("B", 2)], self.test_stream)
        actual = self.extract_written_content()
        self.assertEqual(actual, """A: 1
B: 2
""")

    def extract_written_content(self):
        self.test_stream.seek(0)
        return "".join(self.test_stream.readlines())
