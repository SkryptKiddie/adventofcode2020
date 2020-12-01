import random # golf-ied version of solution
def i():
    lines = open("numbers.txt").read().splitlines()
    return int(random.choice(lines))
while True:
    try:
        f = i()
        s = i()
        if (f + s) == 2020:
            print("NUMBERS FOUND: {} {} \nSOLUTION: {}".format(f, s, (f * s)))
            exit()
    except KeyboardInterrupt:
        exit()
