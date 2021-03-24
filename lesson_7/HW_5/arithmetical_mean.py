# When given a list, the program should return a list of all the elements
# that are below the arithmetical mean of the original list.
# The arithmetical mean is the sum of all elements divided by the number of elements.

from random import randint

length = int(input(f'Enter a number of items: '))
list_numbers = []

for _ in range(length):
    list_numbers.append(randint(1, 10))
print(list_numbers)


def arithmetical_mean(arr):
    result = []
    arith = sum(arr) / len(arr)
    for item in arr:
        if item < arith:
            result.append(item)
    return result


print(arithmetical_mean(list_numbers))
