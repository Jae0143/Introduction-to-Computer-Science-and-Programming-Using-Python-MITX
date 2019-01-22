#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 13:03:12 2018

@author: seongjaegyeong
"""

class Dog:
    def __init__(self, name = "", owner = None):
        self.name = name
        self.owner = owner
    def speak(self):
       print("WOOF!")

class Owner:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("My name is:", self.name)