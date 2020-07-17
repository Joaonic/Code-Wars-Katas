def recoverSecret(triplets):
    secret = ''
    secret_dict = {}
    for x in triplets:
        for y in x:
            secret_dict.setdefault(y, set()).update(x[x.index(y) - 1]) if x.index(y) != 0 else secret_dict.setdefault(y, set())
    def removeChar(c) -> dict:
        {v.remove(c) for k, v in secret_dict.items() if c in v}
    def findChar() -> str:
        return next(k for k, v in secret_dict.items() if not v)
    while secret_dict:
        first_char = findChar()
        secret_dict = {k: v for k, v in secret_dict.items() if k != first_char}
        removeChar(first_char)
        secret = secret + first_char
    return secret