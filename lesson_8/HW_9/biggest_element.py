# Find the biggest number in the list (divide and rule)

from random import randint
length = int(input(f'Input number of items: '))
list_numbers = []

for _ in range(length):
    list_numbers.append(randint(1, 10))
print(list_numbers)


def biggest_element(numbers):
    # if len(list_numbers) > 2:
    #     split_list_numbers = 0
    #     first = max(split_list_numbers[0])
    #     second = max(split_list_numbers[1])
    # if first > second:
    #     return first
    # else:
    #     return second
    # if len(list_numbers) == 1:
    #     return 1
    # if len(list_numbers) == 2:
    #     if list_numbers[0] > list_numbers[1]:
    #         return list_numbers[0]
    # else:
    #     return list_numbers[1]

    temp = numbers[0]
    index = 1
    while index < len(numbers):
        if numbers[index] > temp:
            temp = numbers[index]
        index += 1
    return temp


print(biggest_element(list_numbers))


