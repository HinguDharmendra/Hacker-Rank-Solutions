#!/bin/python

import sys

n = int(raw_input().strip())
s = raw_input().strip()
k = int(raw_input().strip())

def getEncryptedText(string, k):
    encText = ''
    for i in string:
        if(i.isalpha()):
            asciiV = ord(i)+k
            if i.islower():
                if not (97 <= asciiV <= 122):
                    asciiV -= 26
            if i.isupper():
                if not (65 <= asciiV <= 90):
                    asciiV -= 26
            encText += chr(asciiV)
        else:
            encText += i
    return encText

print getEncryptedText(s, k%26)