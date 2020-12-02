# Advent of Code 2020 Day 2 Part 2

## Approach  

Holy crap. This was an equally one. Mainly due to the password validation logic, because I didn't think to draw it out for planning, but I eventually managed to solve it.  

## Password validation  

Since the only code that had to be changed was the password validation code, that was all I changed.  

```python
if pw_string[pw_min] == pw_letter: # check if pw_min is the valid first letter, otherwise check pw_max at else
    if pw_string[pw_max] != pw_letter: # make sure pw_max isn't a match
        counter+=1
        print("{} VALID | {} {} {} {}".format(counter, pw_string, pw_letter, pw_max, pw_min))
else:
    if pw_string[pw_max] == pw_letter: # check if pw_max is the valid first letter
        if pw_string[pw_min] != pw_letter: # make sure pw_min isn't a match
            counter+=1
            print("{} VALID | {} {} {} {}".format(counter, pw_string, pw_letter, pw_max, pw_min))
```

Basically, all this is doing is making sure that only one of the two `pw_min` and `pw_max` variables have matching letters, and that they only appear at one of the two offsets.  
