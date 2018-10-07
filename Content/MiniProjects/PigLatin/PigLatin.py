def convertToPigLatin(phrase):
    '''
    :param phrase: string
    :return: string
    '''
    newPhrase =  ""
    phrase = phrase.lower()
    phrase = phrase.split(" ")
    for word in phrase:
        newWord = convertWord(word)
        newPhrase += newWord + " "
    return newPhrase.strip()

def convertWord(word):
    '''
    :param word: string
    :return: string
    '''
    vowels = ['a', 'e', 'i', 'o', 'u']
    clusters = ['st', 'sm', 'gl', 'tr', 'bl', 'cl', 'pl', 'sl', 'br', 'cr', 'dr',
                'fr', 'gr', 'sc', 'sp', 'tw', 'kn', 'th']


    if word[0] in vowels:
        return pigLatinVowel(word)
    elif word[0:2] in clusters:
        return pigLatinCluster(word)
    else:
        return word[1:] + word[0] + "ay"


def pigLatinVowel(word):
    return word + "way"

def pigLatinCluster(word):
    return word[2:] + word[0:2] + "ay"