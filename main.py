alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


def cypher(text, shift, direction):
    shift = shift % 26

    if direction == -1:
        shift *= -1

    modified_text = ""
    shifted_alphabet = shift_alphabet(shift)
    for i in range(len(text)):
        current_letter = text[i]
        if current_letter not in alphabet:
            modified_text += current_letter
        else:
            position_in_alphabet = alphabet.index(current_letter)
            modified_text += shifted_alphabet[position_in_alphabet]
    print(f"Here is your message: {modified_text}")


def shift_alphabet(shift):
    # return shifted_alphabet
    return alphabet[shift:] + alphabet[:shift]


def main():
    repeat = "yes"
    while repeat == "yes":
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        if direction == "encode" or direction == "decode":
            text = input("Type your message:\n").lower()
            shift = int(input("Type the shift number:\n"))
            if direction == "encode":
                cypher(text, shift, 1)
            else:
                cypher(text, shift, -1)
        else:
            print("Invalid Option")

        repeat = input("Type 'yes' if you want to go again. Otherwise type 'no'\n")


main()
