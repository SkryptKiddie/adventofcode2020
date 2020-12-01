import random
def i():
    lines = open("numbers.txt").read().splitlines()
    return int(random.choice(lines))
while True:
    try:
        f = i()
        s = i()
        t = i()
        if (f + s) == 2020:
            print("NUMBERS FOUND: {} {} {}\nSOLUTION: {}".format(f, s, t, (f * s * t)))
            exit()
    except KeyboardInterrupt:
        exit()
