from typing import Generator, Sequence


def cut_into_chunks(seq: Sequence, k: int) -> Generator:
    """
    Time:   O(n)
    Memory: O(k)

    n - length of seq
    """
    for i in range(0, len(seq), k):
        yield seq[i:i + k]
