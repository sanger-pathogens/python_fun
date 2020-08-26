import unittest

from fun_lib.counting import kmer_count, sort_stats


class TestKmerCount(unittest.TestCase):

    def test_should_count_kmers(self):
        actual = kmer_count(5, ["ACGTACAAG", "TCACGTACAAG"])
        self.assertDictEqual(actual, {
            "ACGTA": 2,
            "CGTAC": 2,
            "GTACA": 2,
            "TACAA": 2,
            "ACAAG": 2,
            "TCACG": 1,
            "CACGT": 1,
        })

    def test_should_sort_stats(self):
        actual = sort_stats({
            "ACGTA": 2,
            "CGTAC": 2,
            "GTACA": 2,
            "TACAA": 2,
            "ACAAG": 2,
            "TCACG": 1,
            "CACGT": 1,
        })
        self.assertEqual(actual, [("ACGTA", 2), ("CGTAC", 2), ("GTACA", 2), ("TACAA", 2), ("ACAAG", 2), ("TCACG", 1),
                                  ("CACGT", 1)])



