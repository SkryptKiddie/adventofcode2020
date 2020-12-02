# Advent of Code 2020 Day 2 Part 1

## Approach

I'll admit, when I saw this challenge at first, [I didn't think it'd be possible for me](https://twitter.com/0x4a6f7368/status/1334008117349126145). But, it was... eventually.  

## Attempt 1

My first attempt was to try and parse all the data and at first, I was going in the complete wrong direction.  

```python
def solve():
    file = open(file).read().splitlines() # open the text file
    for line in lines:
        pw_min = line[1:-0]
        pw_max = line[3:-0]
        pw_letter = line[5:-0]
        pw_string = line[7:]
```

Yeah... I don't know what I was thinking with that one, but then I found out Python already had a module for handling data like that, [the `.partition` function](https://www.programiz.com/python-programming/methods/string/partition). This made my job so much easier.  

## Attempt 2  

Now that I knew how to actually handle the data and somewhat read it, this was what my code looked like.  

```python
def solve():
    file = open(file).read().splitlines()
    for line in file:
        divider = str(line.partition(":")[0])
        pw_max = int(divider.partition("-")[2].partition(' ')[0])
        pw_min = int(divider.partition("-")[0])
        pw_letter = str(divider.partition("-")[2].partition(' ')[2])
        pw_string = str(line.partition(":")[2])
```  

If you don't understand what that code is doing, to make it simple:

- It takes the divider to split the password specifications and the actual password string.
- With that, it then filters out the `pw_max`, `pw_min`, `pw_letter` and `pw_string` variables so that they can be compared.  

So with that, now to actually test the passwords.  

## Password testing  

This was by far, the easiest part of part 1. All I had to do was make sure the `pw_letter` character appeared between `pw_min` and `pw_max` times.  

```python
if (pw_string.count(pw_letter) <= pw_max) == True: # does the string contain the maximum amount of pw_letter?
    if (pw_string.count(pw_letter) >= pw_min) == True: # does the string contain the minimum amount of pw_letter?
        counter += 1
        print("{} VALID | {} {} {} {}".format(counter, pw_string, pw_letter, pw_max, pw_min)) # print the valid password and its specs
    else: # doesn't match the minimum pw_letter amount
        continue
else: # doesn't match the maximum pw_letter amount
    continue
```

I've left the comments in so you can better understand the logic behind it, but essentially, it's just checking whether the letter appears the right amount of times, and if it does, it prints the VALID message and increments 1 to the counter.  
