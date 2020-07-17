def order(sentence):
    words = [(int(l), w) for w in sentence.split() for l in w if l.isdigit()]
    words.sort(key=lambda t: t[0])
    return " ".join(t[1] for t in words)