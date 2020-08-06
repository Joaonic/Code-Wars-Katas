def alphabet_position(text):
    return ' '.join([str(ord(letter.lower()) - 96) for letter in list(text) if letter.isalpha()])