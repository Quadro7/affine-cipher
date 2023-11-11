from const import LOGO, ALPHABET


def affineCiper(a: int, b: int, text: str, mode: str):
    res = ""
    for i, symbol in enumerate(text):
        if symbol.lower() in ALPHABET:
            if mode == 'e' or mode == 'encode':
                index = (a*ALPHABET.index(symbol.lower()) + b) % len(ALPHABET)
            else:
                index = (pow(a, -1, len(ALPHABET)) * (ALPHABET.index(symbol.lower()) - b)) % len(ALPHABET)
            if symbol.islower():
                res += ALPHABET[index]
            else:
                res += ALPHABET[index].upper()
        else:
            res += symbol
    return res


if __name__ == "__main__":
    while True:
        print(LOGO)
        answerMode = input('[e]ncode or [d]ecode? ').lower()
        if answerMode == 'q' or answerMode == 'quit':
            break
        elif answerMode not in 'ed' or answerMode not in 'encode decode':
            continue
        keyB = int(input("Key (between 1 and 26): "))
        answerText = input(f"Enter text to {'encode' if answerMode == 'e' or answerMode == 'encode' else 'decode'}: ")
        cipherText = affineCiper(a=27, b=keyB, text=answerText, mode=answerMode)
        print(f"Here is ciphered text: {cipherText}")
        runAgain = input("Run again? [y]es / [n]o: ").lower()
        if runAgain == 'n' or runAgain == 'no':
            break