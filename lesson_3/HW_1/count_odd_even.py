# Count odd and even numbers.  Count odd and even digits of the whole number. E.g,
# if entered number 34560, then 3 digits will be even (4, 6, and 0)  and  2 odd digits (3 and 5).


number = int(input(f'Enter a number: '))


# def count_odd_and_even(n):
#     odd = 0
#     even = 0
#     for char in str(n):
#         if int(char) % 2 == 0:
#             odd += 1
#         else:
#             even += 1
#     return {
#         'odd': odd,
#         'even': even
#     }
#
#
# print(count_odd_and_even(number))

def count_odd_and_even(n):
    odd = 0
    even = 0
    while n > 0:
        remainder = n % 10
        if remainder % 2 == 0:
            even += 1
        else:
            odd += 1
        n //= 10
    return {
            'even': even,
            'odd': odd
        }


print(count_odd_and_even(number))


