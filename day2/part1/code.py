# code for advent of code day 2 part 1
# https://adventofcode.com/2020/day/2
import sys, time
start_time = time.time() # get the start time

def solve(file):
    counter = 0
    file = open(file).read().splitlines() # open the text file
    for line in file: # sort through each line, this helped a lot https://www.programiz.com/python-programming/methods/string/partition
        divider = str(line.partition(":")[0])
        pw_max = int(divider.partition("-")[2].partition(' ')[0])
        pw_min = int(divider.partition("-")[0])
        pw_letter = str(divider.partition("-")[2].partition(' ')[2])
        pw_string = str(line.partition(":")[2])
        if (pw_string.count(pw_letter) <= pw_max) == True: # does the string contain the maximum amount of pw_letter?
            if (pw_string.count(pw_letter) >= pw_min) == True: # does the string contain the minimum amount of pw_letter?
                counter += 1
                print("{} VALID | {} {} {} {}".format(counter, pw_string, pw_letter, pw_max, pw_min)) # print the valid password and its specs
            else: # doesn't match the minimum pw_letter amount
                continue
        else: # doesn't match the maximum pw_letter amount
            continue

try:
    solve(file="pw_list.txt") # run the solve function
    print("\nCompleted in {}".format((time.time() - start_time)))
except:
    print("\nStopping")
    sys.exit()
