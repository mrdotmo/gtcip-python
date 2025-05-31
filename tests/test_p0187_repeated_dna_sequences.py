from solutions.p0187_repeated_dna_sequences import Solution


def test_Repeated_Dna_Sequences():
    s = Solution()

    assert s.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT") == [
        "AAAAACCCCC",
        "CCCCCAAAAA",
    ]
    assert s.findRepeatedDnaSequences("AAAAAAAAAAA") == ["AAAAAAAAAA"]
