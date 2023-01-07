import numpy as np
from typing import List

class KmersStats:

    def __init__(self, text: str) -> None:
        self.text = text
        self.text_len = len(text)

    def get_kmers(self, k: int) -> List[str]:
        return [self.text[i:i+k] for i in range(0,self.text_len-k+1)]

    def pattern_count(self, pattern: str) -> int:
        k = len(pattern)
        kmers = self.get_kmers(k)
        matches = [kmer == pattern for kmer in kmers]
        return sum(matches)