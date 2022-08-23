from bisect import bisect_left


def longest_increasing_subsequence(nums: list) -> int:
    """
    Time:   O(n*log(n))
    Memory: O(n)
    """
    seq = []

    for x in nums:
        if not seq or seq[-1] < x:
            seq.append(x)
        else:
            seq[bisect_left(seq, x)] = x

    return len(seq)
