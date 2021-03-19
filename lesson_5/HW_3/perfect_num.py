# Write a function to check if a number a Perfect or not


def get_divisors(num, include_num: bool):
    result = []
    end = num
    if include_num:
        end = num + 1

    for item in range(1, end):
        if num % item == 0:
            result.append(item)
    return result


def is_perfect(num):
    return num == sum(get_divisors(num, True))


print(is_perfect(6))