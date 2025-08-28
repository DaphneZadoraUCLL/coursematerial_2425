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

def decode5(sentence):
    words = sentence.split()
    
    for i in range(len(words)):
        words[i] = decode1(words[i])
        words[i] = decode2(words[i])
        words[i] = decode4(words[i])
    
    sentence_decoded = " ".join(words)
    sentence_decoded = decode3(sentence_decoded)
    
    return sentence_decoded