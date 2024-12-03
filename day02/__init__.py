#!/usr/bin/env python3

""" day 2 """

from collections import Counter
from textwrap import dedent


def sign(number):
    """compute the sign of a number"""
    if number > 0:
        return 1
    if number < 0:
        return -1
    return 0


def safe(report):
    """Is this report safe?"""
    diffs = [
        int(report[i]) - int(report[i - 1]) for i in range(1, len(report))
    ]
    return (
        (all(diff > 0 for diff in diffs) or all(diff < 0 for diff in diffs))
        and all(abs(diff) >= 1 for diff in diffs)
        and all(abs(diff) <= 3 for diff in diffs)
    )


def checks(diff):
    """Gather stats on a diff"""
    return [
        diff > 0,
        diff < 0,
        abs(diff) >= 1,
        abs(diff) <= 3,
    ]


def safety_profile(report, dampen=1):
    """Is this report safe? If not, why not?"""
    diffs = [
        int(report[i]) - int(report[i - 1]) for i in range(1, len(report))
    ]

    checks_ = [checks(diff) for diff in diffs]
    [checks_[i][j] for i in range(len(diffs)) for j in range(4)]
    print(checks_)

    """
    n = len(diffs)
    st_inc_c = Counter(diff > 0 for diff in diffs)
    st_dec_c = Counter(diff < 0 for diff in diffs)
    gaps_sm_c = Counter(abs(diff) >= 1 for diff in diffs)
    gaps_lg_c = Counter(abs(diff) <= 3 for diff in diffs)
    for counts in [st_inc_c, st_dec_c, gaps_sm_c, gaps_lg_c]:
        if counts[False] > dampen:
            return False
    st_inc = st_inc_c[True] == n
    st_dec = st_dec_c[True] == n
    gaps_sm = gaps_sm_c[True] == n
    gaps_lg = gaps_lg_c[True] == n
    safe_report = (st_inc or st_dec) and all(gaps_sm) and all(gaps_lg)
    if safe_report:
        return True
    if not st_inc:
        return st
    return
    """


def pt1(lines):
    """day 2 part one"""
    reports = [line.split(" ") for line in lines if safe(line.split(" "))]
    return len(reports)


def pt2(lines):
    """day 2 part two"""
    reports = []
    for line in lines:
        report = line.split(" ")
        if safe(report):
            reports.append(report)
            continue
        # safety_profile(report)
        for i in range(len(report)):
            if safe(report[:i] + report[i + 1 :]):  # noqa
                reports.append(report)
                break
    return len(reports)


def main(prefix=""):
    """day 2"""
    with open(f"{prefix}input.txt", encoding="utf-8") as i_f:
        lines = i_f.read().split("\n")[:-1]

    print("Part 1")
    example_one = dedent(
        """
        7 6 4 2 1
        1 2 7 8 9
        9 7 6 2 1
        1 3 2 4 5
        8 6 4 4 1
        1 3 6 7 9
        """
    )[1:-1]
    example_one_lines = example_one.split("\n")
    assert pt1(example_one_lines) == 2
    print(pt1(lines))

    print("Part 2")
    example_two = example_one
    example_two_lines = example_two.split("\n")
    assert pt2(example_two_lines) == 4
    print(pt2(lines))


if __name__ == "__main__":
    main()
