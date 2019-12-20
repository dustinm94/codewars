def count_vowels(string):
    num_vowels = 0
    vowels = ['a','e','i','o', 'u']
    for s in string:
        if s in vowels:
            num_vowels += 1
        else:
            pass
    return num_vowels
