# 2020 advent of code day 3 part 1
# https://adventofcode.com/2020/day/3
import sys, time
map_1 = [] # map_1 is the instructions.txt file
map_2 = [] # map_2 is the map once we have expanded it
start_time = time.time()
count = 0 # tree encounter count
x = 0 # x coordinate
y = 0 # y coordinate

try:
    with open("instructions.txt") as map:
        for line in map:
            map_1.append(line.rstrip())
        
    for yCoord in range(len(map_1)):
        to_append = (len(map_1)*3) * map_1[yCoord]
        map_2.append(to_append)

    limit_x = len(map_2[0])
    limit_y = len(map_2)    
    while y < limit_y:
        if x < limit_x:
            if(map_2[y][x] == '#'):
                count+=1
            x = x + 3 # move right by 3
            y = y + 1 # move down by 1

    print("TOTAL: {}".format(count))
    print("TIME TAKEN: {}".format((start_time - time.time())))

except:
    sys.exit()
