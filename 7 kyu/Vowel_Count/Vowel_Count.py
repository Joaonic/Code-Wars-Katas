def get_count(input_str):
    num_vowels = 0
    vowel = {'a', 'e', 'i', 'o', 'u'}
    for letter in list(input_str):
        if letter in vowel:
            num_vowels += 1
    return num_vowels