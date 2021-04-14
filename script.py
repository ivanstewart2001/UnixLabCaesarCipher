def caesarCipher(inp, shift):
    inp = inp.upper()
    answer = ""
    for i in range(len(inp)):
        letter = inp[i]
        if (letter.isupper()):
            answer += chr((ord(letter) + shift - 65) % 26 + 65)
    return answer.replace('o',"").upper()