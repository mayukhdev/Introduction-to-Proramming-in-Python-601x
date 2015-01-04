# 6.00x Problem Set 6
#
# Part 1 - HAIL CAESAR!

import string
import random

WORDLIST_FILENAME = "C:\Users\Mayukh\prog_python\Week 6\code_ProblemSet6\words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList

def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList

def randomWord(wordList):
    """
    Returns a random word.

    wordList: list of words  
    returns: a word from wordList at random
    """
    return random.choice(wordList)

def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList

    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([randomWord(wordList) for _ in range(n)])

def randomScrambled(wordList, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordList: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words

    NOTE:
    This function will ONLY work once you have completed your
    implementation of applyShifts!
    """
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' ']
    return applyShifts(s, shifts)[:-1]

def getStoryString():
    """
    Returns a story in encrypted text.
    """
    return open("C:\Users\Mayukh\prog_python\Week 6\code_ProblemSet6\table.txt", "r").read()


# (end of helper code)
# -----------------------------------


#
# Problem 1: Encryption
#
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    first = {}
    second = {}
    temp1 = string.ascii_lowercase
    temp2 = string.ascii_uppercase
    counter = 0
    
    if(shift==0):
        for char in temp1:
            first[char] = temp1[counter]              
            counter+=1
        counter = 0
        for char in temp2:
            first[char] = temp2[counter]              
            counter+=1
        final = first.copy()
        final.update(second)
        return final
    
    
    temp = []
    for letter in temp1[0:shift]:
         temp.append(letter)
    
    for char in temp1[:-shift]:
        value = ord(temp1[counter+shift])
        first[char] = chr(value)       
        counter+=1
    
    i = 0
    for char in temp1[counter:]:
        if temp:
            first[char] =  temp[i]
            i+=1
    counter = 0
    
    temp = []
    for letter in temp2[0:shift]:
         temp.append(letter)
    
    for char in temp2[:-shift]:
        value = ord(temp2[counter+shift])
        second[char] = chr(value)       
        counter+=1
    
    i = 0
    for char in temp2[counter:]:
        if temp:    
            second[char] =  temp[i]
            i+=1
        
    final = first.copy()
    final.update(second)
    return final
        
    
    ### TODO.
    #return "Not yet implemented." # Remove this comment when you code the function

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    answer = ''
    
    for letter in text:
        if letter.isalpha():
            answer += coder[letter]
        else:
            answer += letter    
    return answer        
    
    ### TODO.
    #return "Not yet implemented." # Remove this comment when you code the function

def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    return applyCoder(text , buildCoder(shift))
    
    ### TODO.
    ### HINT: This is a wrapper function.
    #return "Not yet implemented." # Remove this comment when you code the function

#
# Problem 2: Decryption
#
def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    temp = []
    temp = text.split(' ')
    countValid = 0
    
    
    for num in range(26):
        for word in temp:            
            if isWord(wordList, applyShift(word, num)):
                countValid+=1
            if countValid > len(temp)/3 or countValid == len(temp):
                return num
    return 0           
    
    ### TODO
    #return "Not yet implemented." # Remove this comment when you code the function

def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Use the functions getStoryString and loadWords to get the
    raw data you need.

    returns: string - story in plain text
    """
    wordList = loadWords()
    s = getStoryString()
    bestShift = findBestShift(wordList,getStoryString())
    
    return applyShift(s, bestShift)
    
    
    ### TODO.
    #return "Not yet implemented." # Remove this comment when you code the function

#
# Build data structures used for entire session and run encryption
#

if __name__ == '__main__':
    # To test findBestShift:
    #wordList = loadWords()
    #s = applyShift('Hello, world!', 8)
    #bestShift = findBestShift(wordList, s)
    #assert applyShift(s, bestShift) == 'Hello, world!'
    # To test decryptStory, comment the above four lines and uncomment this line:
        decryptStory()
