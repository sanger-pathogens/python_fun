import unittest
from unittest.mock import patch, call

from fun_lib.main import count


class TestCount(unittest.TestCase):

    @patch("fun_lib.main.read_sequence_file")
    @patch("fun_lib.main.compute_stats")
    @patch("fun_lib.main.write_stats")
    def test_should_count(self, mock_write_stats, mock_compute_stats, mock_read_sequence_file):
        mock_read_sequence_file.return_value = ["ACGT", "CGTA"]
        mock_compute_stats.return_value = [("ACGT", 1), ("CGTA", 1)]
        count("input", "output", 4)
        self.assertEqual(mock_read_sequence_file.call_args_list, [call("input")])
        self.assertEqual(mock_compute_stats.call_args_list, [call(4, ["ACGT", "CGTA"])])
        self.assertEqual(mock_write_stats.call_args_list, [call([("ACGT", 1), ("CGTA", 1)], "output")])
