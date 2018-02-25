import string
def decrypt(cipher_prev, cipher, pad, inverse_map):
    return inverse_map[cipher ^ pad] ^ cipher_prev



def create_map(filename):
    with open(filename, 'r') as f:
        g_map = {}
        g_inverse_map = {}
        index = 0
        for line in f:
            hex_array = line.split()
            for hex_char in hex_array:

                int_hex = int(hex_char, 16)
                g_map[index] = int_hex
                g_inverse_map[int_hex] = index
                index += 1
    return g_map, g_inverse_map

def get_ciphertext(filename):
    cipher_texts = []
    with open(filename, 'r') as f:
        for line in f:
            result_array = [0]
            hex_array = line.split()
            for hex_char in hex_array:
                int_hex = int(hex_char, 16)
                result_array.append(int_hex)
            cipher_texts.append(result_array)
    return cipher_texts


def find_pad(cipher_texts, inverse_map):
    possible_chars = set()

    for character in string.printable:
        char = int(hex(ord(character)), 16)
        possible_chars.add(char)

    correct_pad = []

    for index in range(1, len(cipher_texts[0])):
        for pad_value in range(256):
            valid = True
            for cipher_text in cipher_texts:
                if decrypt(cipher_text[index-1], cipher_text[index], pad_value, inverse_map) not in possible_chars:
                    valid = False
            if valid:
                correct_pad.append(pad_value)

    return correct_pad









if __name__ == '__main__':
    g_map, g_inverse_map = create_map('gbox.txt')
    cipher_texts = get_ciphertext('10ciphs.txt')
    pad = find_pad(cipher_texts, g_inverse_map)
    pad_hex = [hex(char)[2:] for char in pad]
    print("This is pad: {}".format(" ".join(pad_hex)))

    for cipher_text in cipher_texts:
        message = ""
        for index in range(1, len(cipher_text)):
            character = chr(decrypt(cipher_text[index-1], cipher_text[index], pad[index-1], g_inverse_map))
            message += character
        print(message)
