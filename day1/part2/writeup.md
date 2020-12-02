# Advent of Code 2020 Day 1 Part 2 Write-up

## Approach

Similar to the part 1 of this challenge, I re-used most of the same code and in fact only had to change some of the math involved.  

## Testing numbers  

The only changes made to the original part 1 script is the addition of the `third_num` variable and the multiplication sum. This was a particullary easy challenge, as I had already written most of the code neccessary, however, I underestimated how long the math operations would take, even on a MacBook Pro.  

```python
def getNum(): # chooses a random number from the numbers.txt file
    lines = open("numbers.txt").read().splitlines()
    return int(random.choice(lines))

first_num = getNum() # get first number
second_num = getNum() # get second number
third_num = getNum() # get third number
if (first_num + second_num + third_num) == 2020:
    # we found a valid number, print success output
    print("NUMBERS FOUND: {} {} {}".format(first_num, second_num, third_num))
    print("SOLUTION: {}".format((first_num * second_num * third_num)))
    print("TIME TAKEN: {}".format((start_time - time.time())))
            sys.exit()
```

This worked fine and all, but it took roughly 5 to 10 minutes to find the correct equation, so an improvement was going to be needed.  

## Optimisations  

Something I realised the first time I ran the program was how long it takes for the script to find the correct value, since normally it was only running in one thread, so what's the obvious solution here? Multithreading!  
Little did I know that this would be a bit more difficult than I anticipated.  
Turns out the Python `multithreading` library is a bit more involved than I was expecting (which is why I didn't implement it.)  
```python
import threading, time, sys, random
start_time = time.time() # get the start time

class multithreading(threading.Thread):
   def __init__(self, threadID, name):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name

   def run(self):
      print ("Starting " + self.name)
      solve(self.name) # begin the solve task

def getNum():
    lines = open("numbers.txt").read().splitlines()
    return int(random.choice(lines))

def solve(threadName):
    while True:
        first_num = getNum() # get first number
        second_num = getNum() # get second number
        third_num = getNum() # get third number
        if (first_num + second_num + third_num) == 2020: 
            # return the success output

thread1 = multithreading(1, "Thread-1", 1)
thread2 = multithreading(2, "Thread-2", 2)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
```  
Yeah, I'm not too bothered about multithreading just yet.  
