#coding=utf-8

import re
import numpy as np
import matplotlib.pyplot as plt

from substitution import Subsitution

def trying(cipher_text, replace_list, length=20):
    output = Subsitution.replace_by_list(cipher_text, replace_list)
    output = output.lower()
    print(output[:length])


if __name__ == "__main__":
    s_obj  = Subsitution()
    cipher_text = s_obj.get_cipher_text('313.txt')
    #
    cipher_stat =s_obj.calculate_text_statistics(cipher_text, is_char=False)
    print(cipher_stat)
    hist = np.histogram([1,2,3,4,5], [1,2,3,4,5])
    print(hist)
    plt.hist(hist)
    plt.show()

    pl_stat = s_obj.get_language_statistics()

    s_obj.draw_text_histogram(statiscics=cipher_stat)
    s_obj.draw_polish_histogram()
    # output = s_obj.map_text(cipher_text, is_char=False)
    # print(output)

    # out = Subsitution.replace_via_static(cipher_text)
    # print(out[:20])
    # alphabet = [chr(letter) for letter in range(97, 123)] + [' ']
    #
    # compare = []
    # for cipher, lang in zip(cipher_stat, pl_stat):
    #     compare.append((cipher[0], lang[0]))

    # print(compare)
    # with open("compare.txt", "w") as f:
    #     for i in compare:
    #         f.write(i[0] + " : " + i[1] + "\n")

    # output = Subsitution.replace_by_list(cipher_text, compare).lower()
    # print(output[:20])
    # print("______________")


    # replace_list = [
    #     #enigma
    #     ("w", "e"),  # w -> a
    #     ('z', 'e'),
    #     ('s', 'o'),
    #     ('y', 'i'),
    #     ('o', 'z'),
    #     ('h', 'n'),
    #     ('k', 's'),
    #     ('i', 'w'),
    #     ('t', 'r'),
    #     ('b', 'c'),
    #     ('q', 't'),
    #     ('l', 'y'),
    #     ('d', 'l'),
    #     ('e', 'k'),
    #     ('g', 'd'),
    #     ('j', 'p'),
    #     ('p', 'm'),
    #     ('a', 'j'),
    #     ('m', 'u'),
    #     ('r', 'b'),
    #     ('x', 'g'),
    #     ('f', 'h'),
    #     ('c', 'f'),
    #     ('v', 'x'),
    #     (' ', 'v'),
    #     ('u', 'q')
    # ]
    #
    # trying(cipher_text, replace_list, length=20)

    #
    # replace_list = [
    #     #enigma
    #     ("w", "a"),  # w -> a
    #     ('z', 'e'),
    #     ('s', 'o'),
    #     ('y', 'i'),
    #     ('o', 'z'),
    #     ('h', 'n'),
    #     ('k', 's'),
    #     ('i', 'w'),
    #     ('t', 'r'),
    #     ('b', 'c'),
    #     ('q', 't'),
    #     ('l', 'y'),
    #     ('d', 'l'),
    #     ('e', 'k'),
    #     ('g', 'd'),
    #     ('j', 'p'),
    #     ('p', 'm'),
    #     ('a', 'j'),
    #     ('m', 'u'),
    #     ('r', 'b'),
    #     ('x', 'g'),
    #     ('f', 'h'),
    #     ('c', 'f'),
    #     ('v', 'x'),
    #     (' ', 'v'),
    #     ('u', 'q')
    # ]