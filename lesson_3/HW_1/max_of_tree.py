# Find max number from 3 values, entered manually from a keyboard


num1 = int(input(f'First number '))
num2 = int(input(f'Secont number '))
num3 = int(input(f'Third number '))


def max_of_tree(number_1, number_2, number_3):
    max_item = number_1
    if max_item < number_2:
        max_item = number_2
    if max_item < number_3:
        max_item = number_3
    return max_item


print(max_of_tree(num1, num2, num3))
