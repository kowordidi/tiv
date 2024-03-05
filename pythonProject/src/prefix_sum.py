from typing import List


def prefixSum(nums: List[int]):
    s = 0
    res = []
    for num in nums:
        s += num
        res.append(s)
    return res

# if __name__ == "__main__":
