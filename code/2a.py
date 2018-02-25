from nltk.corpus import words


def xor(input1, input2):
    assert len(input1) == len(input2)
    result = ""
    for index in range(len(input1)):
        if input1[index] == input2[index]:
            result += "0"
        else:
            result += "1"
    return result

def convert_binary_to_word(binary_string):
    result = ""
    for i in range(len(binary_string)//8):
        character = chr(int(binary_string[i*8: i*8 + 8], 2))
        result += character
    return result

def convert_word_to_binary(word):

    hex_result = ""
    for letter in word:
        hex_letter = format(ord(letter), "x")
        assert len(hex_letter) == 2
        hex_result += hex_letter
    return convert_hex_to_binary(hex_result)



def convert_hex_to_binary(hex_word):


    hex_to_binary = { "0":"0000", "1": "0001", "2": "0010", "3": "0011", "4":"0100", "5":"0101", "6":"0110",
                      "7":"0111", "8": "1000", "9": "1001", "a":"1010", "b":"1011", "c":"1100", "d": "1101",
                      "e":"1110", "f":"1111"}

    hex_word_without_space = hex_word.replace(" ", "")
    result = ""
    for letter in hex_word_without_space:
        result += hex_to_binary[letter]

    return result






if __name__ == '__main__':

    c1 = "a6 a5 6d f4 8c a0 fc 86 d6 1f 2f e9"
    c2 = "ac b9 60 e1 94 a3 f2 93 d2 01 24 f5"

    possible_words = set()
    for word in words.words():
        if len(word) == 12:
            possible_words.add(word)

    c1_binary = convert_hex_to_binary(c1)
    c2_binary = convert_hex_to_binary(c2)

    c_xor = xor(c1_binary, c2_binary)

    for word in possible_words:
        binary_word = convert_word_to_binary(word)

        second_binary_word = xor(binary_word, c_xor)
        second_possible_word = convert_binary_to_word(second_binary_word)

        if second_possible_word in possible_words:
            print("This is the first word: {}".format(word))
            print("This is the second word: {}".format(second_possible_word))
            break
