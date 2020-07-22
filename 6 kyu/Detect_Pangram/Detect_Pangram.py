import string

def is_pangram(s):
    return True if [True if letter in ''.join([n.lower() for n in s.split()]) else False for letter in list(string.ascii_lowercase[:26])].count(True) >= 26 else False
    