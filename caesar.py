import string #string was not previously included

def alphabet_position(letter):
    letter = letter.lower()
    alphabet = string.ascii_letters
    digit = alphabet.find(letter)
    return digit

def rotate_character(char, rot):
    alphabet = string.ascii_letters
    position = alphabet_position(char)
    if not char.isalpha():
        return char
    elif char in string.ascii_lowercase:
        rotate = (position + rot) % 26
        return alphabet[rotate].lower()
    else:
        rotate = (position + rot) % 26
        return alphabet[rotate].upper()

def encrypt(text, rot):
    #rot = user_input_is_valid(argv)   These 3 lines were used when user was typing input with command
    #if rot == False:
        #return "useage: python3 caesar.py n"
    encrypted_message = ""
    for i in text:
        encrypted_character = rotate_character(i, rot)
        encrypted_message = encrypted_message + encrypted_character
    return encrypted_message
