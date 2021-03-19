# Recursion for digital root

def sum_of_digits(number):
    sum = 0
    for char in str(number):
        sum += int(char)
    return sum


def digital_root_rec(num):
    if num < 10:
        return num
    return digital_root_rec(sum_of_digits(num))


