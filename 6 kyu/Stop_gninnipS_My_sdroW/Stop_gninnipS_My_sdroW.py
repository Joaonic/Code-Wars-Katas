def spin_words(sentence):
    return ' '.join([s[::-1] if len(list(s)) >= 5 else s for s in sentence.split(' ')])