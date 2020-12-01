# code for advent of code day 1 part 2
# https://adventofcode.com/2020/day/1#part2
import random, sys, time

def getNum():
    lines = open("numbers.txt").read().splitlines()
    return int(random.choice(lines))

start_time = time.time()
while True:
    try:
        first_num = getNum()
        second_num = getNum()
        third_num = getNum()
        if (first_num + second_num + third_num) == 2020:
            print("NUMBERS FOUND: {} {} {}".format(first_num, second_num, third_num))
            print("SOLUTION: {}".format((first_num * second_num * third_num)))
            print("TIME TAKEN: {}".format((start_time - time.time())))
            sys.exit()
    except KeyboardInterrupt:
        sys.exit()
