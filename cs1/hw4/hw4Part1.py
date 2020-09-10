#This program reads a word and checks that there are 8 characters, starts with a vowel,
#alternates vowels and consonants, and consonants are in increasing alphabetical order
def is_alternating(word):
    word = word.lower()
    #checks length of word is 8
    if len(word) < 8:
        return False
    #check that word starts with a vowel
    if word[0] in vowels:
        pass
    else:
        return False
    #checks for alternating vowels and consonants
    for i in range(len(word)-1):
        if word[i] in consonants and word[i+1] in vowels:
            pass
        elif word[i] in vowels and word[i+1] in consonants:
            pass
        else:
            return False
    #checks consonants increase
    for i in range(len(word)-2):
        if (word[i] in consonants and word[i+2]>word[i]) or word[i] in vowels:
            pass
        else:
            return False
    return True
word = input("Enter a word => ")
print(word)
vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'
if is_alternating(word) == True:
    print("The word '"+word+"' is alternating")
else:
    print("The word '"+word+"' is not alternating")