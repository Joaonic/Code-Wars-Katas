def duplicate_encode(word):
    word = word.lower()
    return "".join(["(" if word.count(w) == 1 else ")" for w in word])