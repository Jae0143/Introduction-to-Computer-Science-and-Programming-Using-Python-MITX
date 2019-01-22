#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s = 'azcbobobegghakl'

test = s[0]
result = s[0]

for index in range(1, len(s)):
    
    if s[index] >= test[-1]:
        test += s[index]
        print(test)
        if len(test) > len(result): # This part makes the longgest answer to the result
            result = test
    else:
        test = s[index]
        
        
print('The final result:', result)