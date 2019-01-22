#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 15:24:25 2018

@author: seongjaegyeong
"""
import string
# Do not modify Message
class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

        
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        key = dict()
        every_letter = string.ascii_lowercase
        copy_of_letter = self.message_text[:]
        for letter in copy_of_letter:
            if letter.isalpha():
                key[letter.lower()] = every_letter[(every_letter.index(letter.lower()) + shift) % len(every_letter)]
        return key

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        returning_string = str()
        keys = self.build_shift_dict(shift)
        copy_message = self.message_text[:]
        for letter in copy_message:
            if letter.isalpha():
                if letter.isupper():
                    returning_string += keys[letter.lower()].upper()
                else:
                    returning_string += keys[letter]
            else:
                returning_string += letter
        return returning_string
            
            
        
# Encrypting message
class PlaintextMessage(Message):
    def __init__(self, text, shift):

        Message.__init__(self, text)
        self.shift = shift
        self.encrypting_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)
        



    def get_message_text_encrypted(self):


        return self.message_text_encrypted 

    def change_shift(self, shift):

        self.shift = shift
        self.message_text_encrypted = self.apply_shift(shift)
    
    

class ceaser_cipher(Message):
    def __init__(self, text):
        Message.__init__(self, text)
        self.message_text = text
        
    
        
    def decrypt(self):
        copy_word = self.message_text[:]
        seperation = copy_word.split()
        total = str()
        for cipher in range(26):
            total = str()
            for word in seperation:
                setting = PlaintextMessage(word, 26 - cipher)
                new_word = setting.get_message_text_encrypted()
                total += new_word + ' '
            print()
            print()
            print('Key used to decrypt: ',26 - cipher, ' Key used to encrypt this message:', cipher , '\n', total)
            print()
            print()
            
            

print('Welcome to cipher - Made by Jae')
while True:
    user_input = int(input('Enter 1 if you want to decrypt, 2 to encrypt, 3 to exit: '))
    if user_input in [1, 2]:
        user_input_2 = str(input('Enter the message: '))
        setting = ceaser_cipher(user_input_2)
        if user_input == 1:
            setting.decrypt()
        elif user_input == 2:
            user_input_3 = int(input('Enter shift: '))
            setting2 = PlaintextMessage(user_input_2, user_input_3)
            print(setting2.get_message_text_encrypted())
    if user_input == 3:
        print('Thank you for using')
        break
        