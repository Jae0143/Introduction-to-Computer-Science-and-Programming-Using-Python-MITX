#!/usr/bin/env python3
# -*- coding: utf-8 -*-
strings = 'azcbobobegghakl'

def checker(strings):
    test = strings[0]
    result = strings[0]
    
    for index in range(1, len(strings)):
        if strings[index] >= test[-1]:
            test += strings[index]
            if len(test) > len(result):
                result = test
                print(result)
        else:
            test = strings[index]
    print('The final value: ', result)

