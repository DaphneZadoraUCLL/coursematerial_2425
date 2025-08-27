def decode1(word):
    return word.replace("A", "o")

def decode2(word):
    return word[::2]

def decode3(sentence):
    words = sentence.split()
    first_word = words[0][::-1]
    return " ".join([first_word] + words[1:])

def decode4(word):
    word_length = len(word)//2
    return word[2:2 + word_length]




def encode1(word):
    return word.replace("o", "A")


import random
import string

def encode2(word):
    return "".join([c + random.choice(string.ascii_lowercase) for c in word])


def encode3(sentence):
    words = sentence.split()
    words[0] = words[0][::-1]
    return " ".join(words)


def encode4(word):
    n = len(word)
    extra = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))
    return extra[:2] + word + extra[2:]