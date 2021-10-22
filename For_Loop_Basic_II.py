# 1) Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
#   Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

def biggie_size(Input):
    for x in range(0, len(Input), 1):
        if Input[x] > 0:
            Input[x] = "big"
        elif Input[x] == 0:
            Input[x] = "Zero is neither positive or negative"
    return Input

a = [-1, 3, 5, -5, 0]
print(biggie_size(a))

# 2) Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
#   Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
#   Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

def count_positives(Input):
    count = 0
    for x in range(0, len(Input), 1):
        if Input[x] > 0:
            count += 1
    Input[len(Input)-1] = count
    return Input

a = [1,6,-4,-2,-7,-2]
print(count_positives(a))


# 3) Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
#   Example: sum_total([1,2,3,4]) should return 10
#   Example: sum_total([6,3,-2]) should return 7

def sum_total(input):
    sum = 0
    for x in range(0, len(input), 1):
        sum += input[x]
    return sum

a = [6,3,-2]
print(sum_total(a))


# 4) Average - Create a function that takes a list and returns the average of all the values.x
#   Example: average([1,2,3,4]) should return 2.5

def average(input):
    sum = 0
    for x in range(0, len(input), 1):
        sum += input[x]
    average = sum/len(input)
    return average

a = [1,2,3,4]
print(average(a))

# 5) Length - Create a function that takes a list and returns the length of the list.
#   Example: length([37,2,1,-9]) should return 4
#   Example: length([]) should return 0

def length(input):
    return len(input)

a = []
print(length(a))

# 6) Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
#   Example: minimum([37,2,1,-9]) should return -9
#   Example: minimum([]) should return False

def minimum(input):
    if len(input) == 0:
        return False
    min = input[0]
    for x in range(0, len(input), 1):
        if input[x] < min:
            min = input[x]
    return min

a = [37,2,1,-9]
print(minimum(a))

# 7) Maximum - Create a function that takes a list and returns the maximum value in the list. If the list is empty, have the function return False.
#   Example: maximum([37,2,1,-9]) should return 37
#   Example: maximum([]) should return False

def maximum(input):
    if len(input) == 0:
        return False
    max = input[0]
    for x in range(0, len(input), 1):
        if input[x] > max:
            max = input[x]
    return max

a = []
print(maximum(a))


# 8) Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
#   Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

def ultimate_analysis(list, dictionary):
    sum = 0
    for x in range(0, len(list), 1):
        sum += list[x]
    average = sum/len(list)

    min = list[0]
    for y in range(0, len(list), 1):
        if list[y] < min:
            min = list[y]

    max = list[0]
    for x in range(0, len(list), 1):
        if list[x] > max:
            max = list[x]

    analysis['sumTotal'] = sum
    analysis['average'] = average
    analysis['minimum'] = min
    analysis['maximum'] = max
    analysis['length'] = len(list)

    return dictionary

a = [37,2,1,-9]
analysis = {'sumTotal': 0, 'average': 0, 'minimum': 0, 'maximum': 0, 'length': 0}
print(ultimate_analysis(a, analysis))

# 9) Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
#   Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

def reverse_list(input):
    for x in range(0, len(input)//2, 1):
        temp = input[x]
        input[x] = input[len(input) - (x+1)]
        input[len(input) - (x+1)] = temp
    return input

a = [37,2,-3,1,-9]
print(reverse_list(a))
