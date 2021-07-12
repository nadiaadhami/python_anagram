# anagram.py
# Two strings are anagrams if they are written using the same exact letters, ignoring space, punctuation and capitalization. 
# Each letter should have the same count in both strings.
#  For example, ‘Eleven plus two’ and ‘Twelve plus one’ are meaningful anagrams of each other.

import numpy as np

s1 = "eleven plus two"
s2 = "twelve plus one"
s3 = "twelve plus two"

def splitWord(word):
    return [char for char in word]

def isAnagram(word1, word2):
    sorted1 = sorted(word1)
    sorted2 = sorted(word2)
    return np.array_equal(sorted1,sorted2)

if isAnagram(s1,s2):
    print("(",s1,") and (",s2, ") are Anagram!")
else:
    print("(",s1,") and (",s2, ") are not anagram.")

if isAnagram(s1,s3):
    print("(",s1,") and (",s3, ") are Anagram!")
else:
    print("(",s1,") and (",s3, ") are not anagram.")