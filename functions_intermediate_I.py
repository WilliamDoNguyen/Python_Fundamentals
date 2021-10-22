import random
def randInt(min= None, max= None):
    if min is None and max is None:
        num = random.random() * 100
        print("line 1")
        return num
    elif min is None and max != None:
        num = random.random() * max
        print("line 2")
        return num
    elif max is None and min != None:
        num = random.random() + min
        print("line 3")
        return num
    else:
        if min > 0 and max > 0 and min > max:
            print("Error: minimum value is greater than maximum value")
            return -1
        num = random.random() * max + min
        print("line 4")
        return num

print(randInt()) # should print a random integer between 0 to 100
print(randInt(max=50)) # should print a random integer between 0 to 50
print(randInt(min=50)) # should print a random integer between 50 to 100
print(randInt(min=50, max=500)) # should print a random integer between 50 and 500
print(randInt(min=50, max=20))
print(randInt(min=0, max=-5))
