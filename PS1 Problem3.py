start = 0
x = 0
longest_substr = ''
start_substr = 0

for char in str_input:
    while x in range(x,(len(str_input)-1)):
        if str_input[x] <= s[x + 1]:
            substr = s[start_substr : x + 1]
            x += 1
        else:
            longest_substr = substr
            start_substr = x
if len(substr) > len(longest_substr):
    longest_substr = substr
            
print("Longest substring in alphabetical order is:",longest_substr)
