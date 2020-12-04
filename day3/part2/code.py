# 2020 advent of code day 3 part 2
# https://adventofcode.com/2020/day/3#part2
import sys, time
map_1 = [] # map_1 is the instructions.txt file
map_2 = [] # map_2 is the map once we have expanded it
start_time = time.time()
count = 0 # tree encounter count
x = 0 # x coordinate
y = 0 # y coordinate

try:
    with open("instructions.txt", "r") as map:
        for line in map:
            map_1.append(line.rstrip())
        
    for coord_y in range(len(map_1)): # lets fix the size of this map
        to_append = (len(map_1)*3) * map_1[coord_y]
        map_2.append(to_append) # lets add the bigger map to the map_2 variable

    limit_x = len(map_2[0])
    limit_y = len(map_2)    
    while y < limit_y:
        if x < limit_x:
            if((map_2[y][x] == '#') == True):
                count+=1
            x = x + 3 # move right by 3
            y = y + 1 # move down by 1

    print("moving 1 right, 1 down")
    count1_1 = 0
    x, y = 0, 0
    while y < limit_y:
        if x < limit_x:
            if((map_2[y][x] == '#') == True):
                count1_1+=1
            x = x + 1 # move right 1
            y = y + 1 # move down 1
        else:
            continue

    print("moving 5 right, 1 down")
    count5_1 = 0
    x, y = 0, 0
    while y < limit_y:
        if x < limit_x:
            if((map_2[y][x] == '#') == True):
                count5_1+=1
            x = x + 5 # move right 5
            y = y + 1 # move down 1
        else:
            continue

    print("moving 7 right, 1 down")
    count7_1 = 0
    x, y = 0, 0
    while y < limit_y:
        if x < limit_x:
            if((map_2[y][x] == '#') == True):
                count7_1+=1
            x = x + 7
            y = y + 1
        else:
            continue

    print("moving 1 right, 2 down")
    count1_2 = 0
    x, y = 0, 0
    while y < limit_y:
        if x < limit_x:
            if((map_2[y][x] == '#') == True):
                count1_2+=1
            x = x + 1
            y = y + 2
        else:
            continue

    print("TOTAL: {}".format((count1_1 * count * count5_1 * count7_1 * count1_2))) # how many trees did we encounter in total?
    print("TIME TAKEN: {}".format((start_time - time.time())))
except:
    sys.exit()
