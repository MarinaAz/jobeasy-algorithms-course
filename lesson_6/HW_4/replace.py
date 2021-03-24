# Find and replace a substring in a string for another substring.
# User enter from a keyboard a string and both substrings. DON’T USE METHOD REPLACE

string = input(f'Enter a string: ')
old_substring = input(f'Enter a substring what you want to change: ')
new_substring = input(f'Enter a substring what you want instead: ')


def replace_string(string_1, old_substr, new_substr):
    if old_substr not in string_1:
        return string_1
    len_old_string = len(old_substr)
    index = string_1.find(old_substr)
    while index > -1:
        string_1 = string_1[:index] + new_substr + string_1[index + len_old_string:]
        index = string_1.find(old_substr, index + len(new_substr))
    return string_1


print(replace_string(string, old_substring, new_substring))
