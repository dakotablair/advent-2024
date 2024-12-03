#!/usr/bin/env python3
""" Advent of Code 2024 """
from day01 import main as day01
from day02 import main as day02
from day03 import main as day03


def main():
    """main"""
    print("Day 1")
    day01(prefix="./day01/")

    print("Day 2")
    day02(prefix="./day02/")

    print("Day 3")
    day03(prefix="./day03/")


if __name__ == "__main__":
    main()
