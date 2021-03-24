# Write a Python function, which will count how many times a character (substring)
# is included in a string. DON’T USE METHOD COUNT

string_1 = input(f'Enter a string ')
string_2 = input(f'Enter a substring ')


def count(given_string, given_substring):
    counter = 0
    if len(given_string) < len(given_substring):
        return counter
    index = given_string.find(given_substring)
    while index > -1:
        index = given_string.find(given_substring, index + 1)
        counter += 1
    return counter


print(count(string_1, string_2))
print(string_1.count(string_2))
