def text_to_morse(text):
    morse_code = {
        'A': '.-', 'B': '-...', 'C': '-.-. ', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
        ' ': '   '
    }

    morse_code_string = ""
    for char in text.upper():
        if char in morse_code:
            morse_code_string += morse_code[char] + " "
        else:
            morse_code_string += char

    return morse_code_string.strip()


text = input("Enter text to convert to Morse code: ")
morse_code_output = text_to_morse(text)
print(morse_code_output)
