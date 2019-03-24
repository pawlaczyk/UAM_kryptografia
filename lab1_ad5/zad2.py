#coding=utf-8


from substitution import Subsitution

if __name__ == "__main__":

    replace_list = [
        #enigma
        ("t", "e"),
        ("f", "n"),
        ("o", "i"),
        ("u", "g"),
        ("d", "m"),
        ("q", "a"),

        #byla
        ("w", "b"),
        ("f", "y"),
        ("s", "l"),
        #a

        #uzywana
        ("x", "u"),
        ("m", "z"),
        ("n", "y"),
        ("v", "w"),
        #a
        #n
        #a

        # komercyjnie
        ("a", "k"),
        ("g", "o"),
        #m
        #e
        ("k", "r"),
        ("e", "c"),
        ("p", "j"),
        #n
        #i
        #e

        #od
        # o
        ("r", "d"),
        #
        #lat
        ("z", "t"),
        #
        # #dwudziestych
        ("l", "s"),
        ("i", "h"),
        ("h", "p"),

        #szyfrujacych
        ("y", "f"),

        ('8','8')
    ]

    cipher_text = Subsitution.get_cipher_text()
    output = Subsitution.replace_by_list(cipher_text, replace_list)



    print(cipher_text)
    print("--------------------")
    print(output)

    out = Subsitution.replace_via_static("lla ma kota")
    print("-----------------")
    print(out)

    out = Subsitution.replace_via_static(cipher_text)
    print("-----------------")
    print(out)
    print(output)