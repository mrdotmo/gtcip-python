from array import array
from math import pow
from typing import List


class Solution:
    def findRepeatedDnaSequences(self, seq: str) -> List[str]:
        """
        LeetCode Problem 187: Repeated Dna Sequences
        https://leetcode.com/problems/repeated-dna-sequences
        """
        rv: List[str] = []
        mapping: dict[str, int] = {"A": 1, "C": 2, "G": 3, "T": 4}
        iseq = array("B", (mapping[ch] for ch in seq))
        count: dict[int, int] = {}
        m: int = 10
        base: int = 4
        subseq_hash: int = 0
        prev_subseq_hash: int = 0
        for i in range(len(seq) - m + 1):
            if i == 0:
                for j in range(m):
                    subseq_hash += int(iseq[j] * pow(base, m - j - 1))
            else:
                prev_subseq_hash = subseq_hash
                subseq_hash = (
                    int(base * (prev_subseq_hash - iseq[i - 1] * pow(base, m - 1)))
                    + iseq[i + m - 1]
                )
            if count.get(subseq_hash, 0) == 1:
                rv.append(seq[i : i + m])
            count[subseq_hash] = count.get(subseq_hash, 0) + 1
        return rv
