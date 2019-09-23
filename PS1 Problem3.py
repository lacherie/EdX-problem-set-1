s = 'abzcbobobegghakl'
previous = s[0] #assumes greater/equal comparison
substr = ''
longest_substr = ''
for char in s:
    if char >= previous:
        substr += char
    else:
        if len(substr) > len(longest_substr):
            longest_substr = substr
        substr = char
    previous = char
#does not work if last substring is the longest

print("Longest substring in alphabetical order is:",longest_substr)
