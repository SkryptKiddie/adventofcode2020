# Advent of Code 2020 Day 1 Part 1 Challenge Write-up by SkryptKiddie

## Approach

With this task, I decided to take a basic approach and use the Python 3.9.0 library random to get a random number from the `numbers.txt` file, and then add it together with another random number.  

## Testing numbers

I created a function called `getNum()` which would return a random number from the text file. These numbers were stored as intgers within the loop.  

```python
def getNum(): # chooses a random number from the numbers.txt file
    lines = open("numbers.txt").read().splitlines()
    return int(random.choice(lines))

first_num = getNum()
second_num = getNum()
if (first_num + second_num) == 2020:
    # we found a valid number, print success output
```

## Sum found

The premise for this was simple. Once the valid sum was found, they would be multiplied and returned in the "success" output, like follows:

```python
print("NUMBERS FOUND: {} {}".format(first_num, second_num))
print("SOLUTION: {}".format((first_num * second_num)))
print("TIME TAKEN: {}".format((start_time - time.time())))
sys.exit()
```

And that, was how I solved part 1 the first Advent of Code 2020 challenge!
