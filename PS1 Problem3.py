s = 'abzcbobobegghakl'
s1 = s + '_'
previous = s[0] #assumes greater/equal comparison
substr = ''
longest_substr = ''
for char in s1:
    if char >= previous:
        substr += char
    else:
        if len(substr) > len(longest_substr):
            longest_substr = substr
        substr = char
    previous = char


print("Longest substring in alphabetical order is:",longest_substr)
