def disemvowel(string):
    vowels = {'a':'','e':'','i':'','o':'','u':'','A':'','E':'','I':'','O':'','U':''}
    for vowel in vowels:
        string = string.replace(vowel, vowels[vowel])
    return string