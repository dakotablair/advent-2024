#!/usr/bin/env python3

""" day 3 """

import re

from pprint import pprint as pp


def pt1(code):
    """day three part one"""
    prods = re.findall(r"mul\(([0-9]+),([0-9]+)\)", code)
    total = sum((int(absc) * int(ordi) for absc, ordi in prods), 0)
    return total


def pt2(code):
    """day three part two"""
    prods = re.findall(r"(do\(\)|don't\(\)|mul\(([0-9]+),([0-9]+)\))", code)
    enabled = True
    vals = []
    for inst, absc, ordi in prods:
        if inst == "don't()":
            enabled = False
            continue
        if inst == "do()":
            enabled = True
            continue
        if enabled:
            vals.append(int(absc) * int(ordi))
    return sum(vals, 0)


def main(prefix=""):
    """day three"""
    with open(f"{prefix}input.txt", encoding="utf-8") as i_f:
        code = i_f.read()

    print("Part 1")
    example_one = "".join(
        (
            "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)",
            "+mul(32,64]then(mul(11,8)mul(8,5))",
        )
    )
    assert pt1(example_one) == 161
    print(pt1(code))

    print("Part 2")
    example_two = "".join(
        (
            "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+",
            "mul(32,64](mul(11,8)undo()?mul(8,5))",
        )
    )
    assert pt2(example_two) == 48
    print(pt2(code))


if __name__ == "__main__":
    main()
