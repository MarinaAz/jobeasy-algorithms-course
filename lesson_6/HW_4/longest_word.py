# Enter a string of words separated by spaces. Find the longest word.

string_3 = input(f'Enter a string: ')


def longest_word(string):
    substring = ''
    result = ''
    for char in string:
        if char == ' ':
            if len(substring) > len(result):
                result = substring
            substring = ''
        else:
            substring += char
    else:
        if len(substring) > len(result):
            result = substring
    return result


print(longest_word(string_3))