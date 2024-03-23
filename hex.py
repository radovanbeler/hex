#!/usr/bin/python3
import argparse
import random
import sys
import time


def clear():
    """
    Clear screen and set cursor to top left corner using ANSII escape codes
    """
    print("\x1b[2J", end="", flush=True)
    print("\x1b[H", end="")


def check(number, answer, base):
    try:
        answer = int(answer, base)
        if number == answer:
            print("Correct")
        else:
            print("Incorrect")
    except:
        print("Invalid format")


def get_number(nibbles):
    return random.randint(0, 2 ** (4 * nibbles) - 1)


def from_hex(nibbles):
    while True:
        clear()
        number = get_number(nibbles)
        print(f"0x{number:0{nibbles}x}")
        answer = input("0b").strip()
        if answer == "q":
            break
        check(number, answer, 2)
        time.sleep(1)


def from_bin(nibbles):
    while True:
        clear()
        number = get_number(nibbles)
        print(f"0b{number:0{nibbles * 4}b}")
        answer = input("0x").strip()
        if answer == "q":
            break
        check(number, answer, 16)
        time.sleep(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="hex", epilog="To exit hex enter 'q'")
    parser.add_argument(
        "-b",
        dest="binary",
        action="store_true",
        help="From binary to hex",
    )
    parser.add_argument(
        "-n",
        dest="nibbles",
        type=int,
        default=1,
        help="Number of nibbles (one nibble is four bits)",
    )
    args = parser.parse_args()

    if not (1 <= args.nibbles <= 16):
        print("Allowed range of nibbles is <1, 16>", file=sys.stderr)
        exit(1)

    if args.binary:
        from_bin(args.nibbles)
    else:
        from_hex(args.nibbles)

    clear()
