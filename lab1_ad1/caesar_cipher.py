#coding=utf-8

from zope.interface import implementer

from caesar_interface import ICaesarCipher

@implementer(ICaesarCipher)
class CaesarCipher():
    """

    """

    @classmethod
    def get_cipher_text(cls, filepath='caesar_cipher_text.txt')-> str:
        """

        :param filepath: path to file with cipher text
        :return: string variable with cipher_text from file
        :rtype: str

        """
        with open(filepath, "r") as f:
            cipher_text = f.read()
        return cipher_text

    @classmethod
    def create_letter_table(cls,)->list:
        """

        :return: list with standard order of letters in English
        :rtype: list

        """
        alphabet = [chr(letter) for letter in range(97, 123)]
        return alphabet

    @classmethod
    def change_letter_offset(cls, elements: list, offset=3)->list:
        """

        :param elements: list of elements
        :param offset: offset for
        :return: alphabet letter with offset
        :rtype: list

        """
        return elements[offset:] + elements[:offset]

    @classmethod
    def change_letter_in_text(cls, cipher_text=None, alphabet=None , offset=None)->str:
        """

        :param cipher_text: cipher text str
        :param alphabet: list wit letters in alphabet order
        :param offset: offset for list alphabet
        :return: cipher_text with changed order of letter
        """
        alphabet = cls.create_letter_table() if not alphabet else alphabet
        offset = 3 if not offset else offset
        alphabet_with_offset = cls.change_letter_offset(alphabet, offset)
        cipher_text = cls.get_cipher_text() if not cipher_text else cipher_text

        output = ''
        for cipher_letter in cipher_text:
            if cipher_letter.isalpha():
                index_in_alphabet = alphabet.index(cipher_letter)
                output += alphabet_with_offset[index_in_alphabet]
            else:
                output += ' '

        return output

    @classmethod
    def show_all_caesar_permutation(cls, cipher_text=None, alphabet=None):
        alphabet = cls.create_letter_table() if not alphabet else alphabet
        for offset in range(len(alphabet)):
            output = cls.change_letter_in_text(cipher_text=cipher_text, alphabet=alphabet, offset=offset)
            print("OFFSET: ", offset)
            print(output)
            print("----------------------------\n")


if __name__ == "__main__":
    CaesarCipher().show_all_caesar_permutation()
