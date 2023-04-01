alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(letter, num):
    array = []
    for i in letter:
        for n in range(0, len(alphabet)):
            if i == alphabet[n]:
                if n + num > 26:
                    array.append(alphabet[int((n + num) - 26)])
                else:
                    array.append(alphabet[n + num])
    print(''.join(array))


def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        if new_position < 0:
            plain_text += alphabet[new_position + 26]
        else:
            plain_text += alphabet[new_position]
    print(plain_text)


if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
