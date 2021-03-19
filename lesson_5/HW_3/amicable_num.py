# Check if two numbers are friendly to each other or not.
#
# Amicable number:
# n1 sum of divisors (except an n1) are equal to n2 and sum of divisors n2 are equal to n1.
# For example: 220 and 284
# 220: divisors [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110]
# 284: divisors [1, 2, 4, 71, 142]
def get_divisors(num, include_num: bool):
    result = []
    end = num
    if include_num:
        end = num + 1

    for item in range(1, end):
        if num % item == 0:
            result.append(item)
    return result


def is_amicable(num_1, num_2):
    div_num_1 = get_divisors(num_1, False)
    div_num_2 = get_divisors(num_2, False)
    return num_1 == sum(div_num_2) and num_2 == sum(div_num_1)


print(is_amicable(221, 284))

