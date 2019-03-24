#coding=utf-8

"""
Zadanie 1
Odszyfruj szyfrogram powstały poprzez zastosowanie szyfru Cezara. Tekst jawny został napisany w języku polskim, nie zawiera polskich liter oraz znaków interpunkcyjnych.
Przydatne narzędzia:

    Edytor tekstu z funkcją zastąp
    CrypTool: Kryptoanaliza->Alg. historyczne->Analiza manualna->Zamiana

"""


from zope.interface import Interface, Attribute

class ICaesarCipher(Interface):  # Interface
    """Interface for Caesar Cipher"""

    alphabet = Attribute("Używany alfabet")
    offset = Attribute("Przesuniecie dla szyfru Cezara")
    cipher_text = Attribute("Zaszforwany text")



################################
# Abstrct method Interface
# Overriding


if __name__ == "__main__":
    print(type(ICaesarCipher))
    print(ICaesarCipher.__doc__)
    print(ICaesarCipher.__name__)
    print(ICaesarCipher.__module__)
    x = ICaesarCipher['offset']
    type(x)
    x.__name__
    x.__doc__
    ICaesarCipher.get('offset').__name__
    ICaesarCipher.get('cipher_text')
    print('x' in ICaesarCipher)
    names = list(ICaesarCipher)
    names.sort()
    print(names)
    bar = ICaesarCipher['alphabet']
    print(bar)
