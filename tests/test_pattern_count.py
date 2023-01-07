import pytest
from thiago_lib import KmersStats


class TestThiagoLib:

    def test_should_list_all_3mers(self):
        text = "CGCT"
        expected = ["CGC", "GCT"]
        result = KmersStats(text).get_kmers(3)
        assert result == expected

    def test_should_count_pattern_freq(self):
        nucleotides = "GCGCGATTATAT"
        expected = 2
        result = KmersStats(nucleotides).pattern_count("TAT")
        assert result == expected