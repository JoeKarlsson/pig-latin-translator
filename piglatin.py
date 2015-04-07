phrase = 'This phrase will be converted into piglatin, please insert your phrase here.'
pigString= 'is-Thay ig-Pay atin-Lay ase-phray ill-way e-bay anslated-tray ack-bay o-intay e-thay ative-nay anguage-lay -asay -aay ing.-stray'

def unpigPhrase (phrase):
    sentence = phrase.split()
    unpiggedphrase = []
    for word in sentence:
        unpiggedphrase.append(unpigword(word))
    return ' '.join(unpiggedphrase)

def pigPhrase (phrase):
    sentence = phrase.split()
    piggedphrase = []
    for word in sentence:
        piggedphrase.append(pigword(word))
    return ' '.join(piggedphrase)

def unpigword (piggedword):
    return piggedword[(piggedword.find('-') +1):-2] + piggedword[0:piggedword.find('-')]

def findvowel (word):
    vowels = "aeiouAEIOU"
    for i in range (0,len(vowels)):
        vowelnumber = word.find(vowels[i])

        if vowelnumber > 0:
            return vowelnumber

        else:
            if i == len(vowels)-1:
                return len(word)

def pigword (word):
    return word[findvowel(word):] + "-" + word[:findvowel(word)] + "ay"

def join (List):
    if List == []:
        return ''
    else:
        sentence = List[0]
        for word in range (1, len(List)):
            sentence = sentence + ' ' + List[word]
        return sentence

print pigPhrase(phrase)

print unpigPhrase(pigString)