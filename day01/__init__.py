#!/usr/bin/env python3

""" day 1 """

from collections import Counter
from textwrap import dedent


def pt1(lines):
    """day 1 part one"""
    pairs = [line.split("   ") for line in lines]
    lists = list(zip(*pairs))
    cola = sorted(lists[0])
    colb = sorted(lists[1])
    diffs = [abs(int(cola[i]) - int(colb[i])) for i in range(len(cola))]
    return sum(diffs)


def pt2(lines):
    """day 1 part two"""
    pairs = [line.split("   ") for line in lines]
    lists = list(zip(*pairs))
    cola = sorted(lists[0])
    colb = sorted(lists[1])
    counts = Counter(colb)
    return sum(int(val) * int(counts[val]) for val in cola)


def main(prefix=""):
    """day 1"""
    with open(f"{prefix}input.txt", encoding="utf-8") as i_f:
        lines = i_f.read().split("\n")[:-1]

    print("Part 1")
    example_one = dedent(
        """
        3   4
        4   3
        2   5
        1   3
        3   9
        3   3
        """
    )[1:-1]
    example_one_lines = example_one.split("\n")
    assert pt1(example_one_lines) == 11
    print(pt1(lines))

    print("Part 2")
    example_two = example_one
    example_two_lines = example_two.split("\n")
    assert pt2(example_two_lines) == 31
    print(pt2(lines))


if __name__ == "__main__":
    main()
