import pytest

from kmp import (kmp_concatenation, kmp_two_pointers, prefix_function_naive,
                 prefix_function_On, prefix_function_On2)

test_cases_prefix = [
    ("abcabcd", [0, 0, 0, 1, 2, 3, 0]),
    ("aabaaab", [0, 1, 0, 1, 2, 2, 3]),
]

test_case_kmp = [
    ("pattern", "text", []),
    ("ab", "ababab", [0, 2, 4]),
    ("na", "banananobano", [2, 4]),
    ("foobarfoo", "barfoobarfoobarfoobarfoobarfoo", [3, 9, 15, 21]),
    ("AABA", "AABAACAADAABAABA", [0, 9, 12]),
]


def test_prefix_function_naive():

    for i, (inp, ans) in enumerate(test_cases_prefix):
        assert prefix_function_naive(inp) == ans


def test_prefix_function_On2():
    for i, (inp, ans) in enumerate(test_cases_prefix):
        assert prefix_function_On2(inp) == ans


def test_prefix_function_On():
    for i, (inp, ans) in enumerate(test_cases_prefix):
        assert prefix_function_On(inp) == ans


def test_kmp_concatenation():
    for i, (pattern, text, ans) in enumerate(test_case_kmp):
        assert kmp_concatenation(pattern, text) == ans


def test_kmp_two_pointers():
    for i, (pattern, text, ans) in enumerate(test_case_kmp):
        assert kmp_two_pointers(pattern, text) == ans
