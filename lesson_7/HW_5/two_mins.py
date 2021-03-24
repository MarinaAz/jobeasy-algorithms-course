# When given a list of elements find the two lowest elements.
# They can be equal to each other or different.

from random import randint

length = int(input(f'Enter a number of items: '))
list_numbers = []

for _ in range(length):
    list_numbers.append(randint(1, 10))
print(list_numbers)


def two_mins(array):
    result = []
    min_element = min(array)
    result.append(min_element)
    array.remove(min_element)
    min_element = min(array)
    result.append(min_element)
    return result


print(two_mins(list_numbers))
