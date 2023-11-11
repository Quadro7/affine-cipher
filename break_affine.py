from const import ALPHABET, WORDS
from math import gcd
from main import affineCiper


def breakAC(text: str):
    aList = []
    for x in range(26):
        if gcd(x, 26) == 1:
            aList.append(x)
    possibleAB = []
    for word in text.lower().split(' '):
        for b in range(27):
            for a in aList:
                proposition = ""
                for letter in word:
                    index = (pow(a, -1, len(ALPHABET)) * (ALPHABET.index(letter) - b)) % len(ALPHABET)
                    proposition += ALPHABET[index]
                if proposition in WORDS:
                    possibleAB.append((a, b))
    mostProbableAB = possibleAB[0]
    mostProbableCount = possibleAB.count(possibleAB[0])
    for pair in list(set(possibleAB)):
        if possibleAB.count(pair) > mostProbableCount:
            mostProbableAB = pair
            mostProbableCount = possibleAB.count(pair)
    return mostProbableAB

#print(breakAC("Cuzx zx l cfxc"))
if __name__ == "__main__":
    while True:
        answerCipher = input("Affine Cipher breaker\nEnter encoded text: ")
        if answerCipher.lower() == 'q' or answerCipher.lower() == 'quit':
            break
        ab = breakAC(answerCipher)
        print(f"A = {ab[0]}\nB = {ab[1]}")
        decipheredText = affineCiper(ab[0], ab[1], answerCipher, 'd')
        print(f"Here is deciphered text: {decipheredText}")
