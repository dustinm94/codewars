def removeVowel(S):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for letter in S:
        for vowel in vowels:
            if letter == vowel:
                S = S.replace(letter, '')


if __name__ == '__main__':
    removeVowel('test')