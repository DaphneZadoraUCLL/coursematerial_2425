def spellcheck(document, valid_words):
    valid_words = set(valid_words)
    invalid_words = set()

    for word in document.split():
        word_lower = word.lower()
        if word_lower not in valid_words:
            invalid_words.add(word_lower)
    return invalid_words
