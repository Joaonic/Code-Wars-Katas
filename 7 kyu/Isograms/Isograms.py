def is_isogram(string):
    string = string.lower()
    if len(string) == len(set(string)):
        return True
    return False