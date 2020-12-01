# code for advent of code day 1 part 1
# https://adventofcode.com/2020/day/1
import random, sys

def getNum():
    lines = open("numbers.txt").read().splitlines()
    return int(random.choice(lines))

while True:
    try:
        first_num = getNum()
        second_num = getNum()
        if (first_num + second_num) == 2020:
            print("NUMBERS FOUND: {} {}".format(first_num, second_num))
            print("SOLUTION: {}".format((first_num * second_num)))
            sys.exit()
    except KeyboardInterrupt:
        sys.exit()
