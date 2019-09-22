# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 09:56:43 2019

@author: admin
"""


s = 'abzcbobobegghakl'
str_input = s
#s = 'abcdefg'
substr = ''
#x = 0
#y = x + 1
#for x in range(0,len(s)):
#    while s[x] <= s[x + 1]:
#        substr = s[x : y]
#        y += 1
#        print(s[x])
#
#for x in range(0,len(s)):
#    y = x
#    while s[y] <= s[y + 1]:
#        substr = s[start_substr : y + 1]
#        y += 1
#    else:
#        substr = ''
#        start_substr = y
        
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
        


        
    
print("Longest substring in alphabetical order is:",longest_substr)
