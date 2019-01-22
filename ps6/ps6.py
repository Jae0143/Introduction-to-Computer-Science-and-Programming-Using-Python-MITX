import string

### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    #print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    
    #print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list

### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'words.txt'


# Bunch of essential functions
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
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
        
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
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less 
        code is repeated
        '''
        Message.__init__(self, text)
        self.shift = shift
        self.encrypting_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)
        
    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        '''
        return self.encrypting_dict.copy()

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted 

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift
        self.encrypting_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)
        
#Decrypting message
class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)
        
    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        copy_word = self.message_text[:]
        copy_valid_word = self.valid_words[:]
        best_result = tuple()
        best_key = 0
        best_num = 0
        all_word_seperate = dict()
        seperation = copy_word.split()
        total = str()
        for cipher in range(27):
            total = str()
            for word in seperation:
                setting = PlaintextMessage(word, 26 - cipher)
                new_word = setting.get_message_text_encrypted()
                total += new_word + ' '
            all_word_seperate[cipher] = [total.split()]

        
        for key in all_word_seperate.keys():
            maxim = 0
            check = all_word_seperate[key][0]
            for word in check:
                if is_word(copy_valid_word, word.lower()):
                    maxim += 1
            all_word_seperate[key].append(maxim)
            
            check = all_word_seperate[key][1]
            if check > best_num:
                best_num = check
                best_key = key
                
        all_word_seperate[best_key][0] = ' '.join(all_word_seperate[best_key][0])
        print()
        print('How to read result: (key used to decrypt, key used to encrypt, decrypted message)')
        print()
        best_result += (26 - best_key, )
        best_result += (best_key, )
        best_result += (all_word_seperate[best_key][0], )

        return best_result
    
            
    def way_2(self):
        copy_word = self.message_text[:]
        seperation = copy_word.split()
        total = str()
        for cipher in range(27):
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
        
        
    
def decrypt_story(story):
    setting = CiphertextMessage(story)
    story_decrypt = setting.way_2()
    return story_decrypt
            
                
      

#Example test case (PlaintextMessage)
plaintext = PlaintextMessage('hello', 2)
print('Expected Output: jgnnq')
print('Actual Output:', plaintext.get_message_text_encrypted())
    
#Example test case (CiphertextMessage)
ciphertext = CiphertextMessage('jgnnq')
print('Expected Output:', (24, 'hello'))
print('Actual Output:', ciphertext.decrypt_message())


get_story = get_story_string()
print(decrypt_story(get_story))
"""
inputs = str(input('Enter the story: '))

setting = CiphertextMessage(inputs)
setting.way_2()
"""