"""  prefix_sum tests """
from typing import List

from src.prefix_sum import prefixSum


def _prefix_sum(in_arr: List[int], expect_arr: List[int], msg: str = ""):
    psum = prefixSum(in_arr)
    ok = (psum == expect_arr)
    print(f"Test for prefixSum returned: {ok}, expected: {expect_arr}, got: {psum} in {msg}")
    assert ok


def test_prefix_one():
    in_array = [3, 6, 2, 8, 1, 4, 1, 5]
    expect_array = [3, 9, 11, 19, 20, 24, 25, 30]
    _prefix_sum(in_array, expect_array, msg="sized array")


def test_prefix_two():
    in_array = [3]
    expect_array = [3]
    _prefix_sum(in_array, expect_array, msg="single array")


def test_prefix_three():
    in_array = [3, 2]
    expect_array = [3, 5]
    _prefix_sum(in_array, expect_array, msg="single array")
