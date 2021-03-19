# TODO: Homework: Rewrite a program with any number of digits.
#  Instead of  3 digits, you should sum digits up from n digits number,
#  Where User enter n manually. n > 0


from random import randint

n = int(input('Enter a number of digits: '))


def sum_of_digits(digits):
    down = 10 ** (digits - 1)
    up = (10 ** digits) - 1
    random_number = randint(down, up)
    print(random_number)
    sum = 0
    for char in str(random_number):
        sum += int(char)
    return sum


print(sum_of_digits(n))

