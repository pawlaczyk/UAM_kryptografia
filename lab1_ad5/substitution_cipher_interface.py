#coding=utf-8

"""
Zadanie 2
Złam szfrogram powstały poprzez szyfrowanie metodą podstawieniową
(CrypTool: Szyfrowanie->Historyczne->Zamiana). Podaj również klucz szyfrujący, czyli tajny alfabet.
Tekst jawny został napisany w języku polskim, nie zawiera polskich liter oraz znaków interpunkcyjnych.
Przydatne narzędzia i informacje:

    CrypTool: Krytoanaliza->Narzędzia analizy->Histogram
    Arkusz kalkulacyjny
    Edytor tekstu z funkcją zastąp
    CrypTool: Kryptoanaliza->Alg. historyczne->Analiza manualna->Zamiana

"""


from zope.interface import Interface, Attribute

class ISubstitutionCipher(Interface):  # Interface
    """Interface for Substitution Cipher"""

    alphabet = Attribute("Używany alfabet")
    offset = Attribute("Przesuniecie dla szyfru Cezara")
    cipher_text = Attribute("Zaszforwany text")