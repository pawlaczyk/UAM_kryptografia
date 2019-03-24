#coding=utf-8

import csv
from collections import Counter
import re

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class Subsitution(object):
    """Szyfr monoalfabetyczny

tfoudq wnsq xmnvqfq agdtkenpfot gr sqz rvxrmotlznei rvxrmotlztug votax q hgmfotp mglzqsq mqqrqhzgvqfq hkmtm oflznzxept
 hqflzvgvt votsx akqpgv hgremql rkxuotp vgpfn lvoqzgvtp dqlmnfq zq wnłq vnagkmnlznvqfq usgvfot hkmtm losn mwkgpft gkqm
  offt lsxmwn hqflzvgvt o vnvoqrgvemt fotdote qst zqamt offnei hqflzv tfoudq fqstmqsq rg kgrmofn tstazkgdteiqfoemfnei
   vokfoagvnei dqlmnf lmnykxpqenei o wnłq hkgrxagvqfq v votsx kgmfnei grdoqfqei hg kqm hotkvlmn lmnykgukqdn mqagrgvqft
    hkmn hgdgen tfoudn xrqsg lot kgmlmnykgvqe hgslaod aknhzgsgugd v zkmnrmotlznd rkxuod kgax hkqet hgsqagv usgvfot
     dqkoqfq ktptvlaotug ptkmtug kgmneaotug o itfknaq mnuqslaotug hgmvgsosn fq rqslmt hkqet fqr rtagrgvqfotd lmnykgv
      lzqst xfgvgemtlfoqfnei dqlmnf tfoudq fqphotkv v hgslet q hg vnwxeix vgpfn vt ykqfepo o votsaotp wknzqfoo

    ENIGMA BYLA UZYWANA KOMERCYJNIE OD LAT DWUDZIESTYCH DWUDZIESTEGO WIEKU A POZNIEJ ZOSTALA ZAADAPTOWANA PRZEZ
    INSTYTUCJE PANSTWOWE WIELU KRAJOW PODCZAS DRUGIEJ WOJNY SWIATOWEJ MASZYNA TA BYłA WYKORZYSTYWANA GLOWNIE PRZEZ
    SILY ZBROJNE ORAZ INNE SLUZBY PANSTWOWE I WYWIADOWCZE NIEMIEC ALE TAKZE INNYCH PANSTW ENIGMA NALEZALA DO RODZINY
    ELEKTROMECHANICZNYCH WIRNIKOWYCH MASZYN SZYFRUJACYCH I BYłA PRODUKOWANA W WIELU ROZNYCH ODMIANACH PO RAZ PIERWSZY
    SZYFROGRAMY ZAKODOWANE PRZY POMOCY ENIGMY UDALO SIE ROZSZYFROWAC POLSKIM KRYPTOLOGOM  W TRZYDZIESTYM DRUGIM ROKU
    PRACE POLAKOW GLOWNIE MARIANA REJEWSKIEGO JERZEGO ROZYCKIEGO I HENRYKA ZYGALSKIEGO POZWOLILY NA DALSZE PRACE NAD
    DEKODOWANIEM SZYFROW STALE UNOWOCZESNIANYCH MASZYN ENIGMA NAJPIERW W POLSCE A PO WYBUCHU WOJNY WE FRANCJI I
    WIELKIEJ BRYTANII

    """


    @classmethod
    def get_cipher_text(cls, filepath='substitution_cipher_text.txt')->str:
        with open(filepath, "r", encoding="utf-8") as f:
            cipher_text = f.read()
        return cipher_text

    @classmethod
    def _row_to_float(cls, row):
        row = row[:-1] # bez procenta
        row = row.replace(',', '.')
        return float(row)

    @classmethod
    def _two_letter_i(cls, cipher_text):
        """
        W języku polskim słowa często są zakończone a dwie litery ii
        :param cipher_text:
        :return:
        """
        pass

    @classmethod
    def _one_letter_words(cls, cipher_text):
        """
        Słowa będące pojedynczymi literami
        :param cipher_text:
        :return:
        """
        list_words = ["a", "w", "z", "i", "u", "o" ]

    @classmethod
    def _two_letter_words(cls, cipher_text):
        """
        Słowa będące słowami z dwóch liter
        :param cipher_text:
        :return:
        """
        list_words = ["do", "za", "az", "bo", "by", "iz", "ni", "ze", "do", 'ku', 'na', 'od', 'po', 'we',
                      'za', "ze", "he", "no", "ot",  "ow", "ta", "te", "ta", "to", "go"]
        return list(set(list_words))

    @classmethod
    def _three_letter_words(cls, cipher_text):
        """
        Słowa będące słowami z trzech liter
        :param cipher_text:
        :return:
        """
        list_words = ["przy", "nad", "pod"]

    @classmethod
    def _four_letter_words(cls, cipher_text):
        """
        Słowa będące słowami z trzech liter
        :param cipher_text:
        :return:
        """
        list_words = ["oraz", "nad", "pod"]

    @classmethod
    def _sort_statistics(cls, statistics:dict)->list:
        return sorted(statistics.items(), key=lambda x: x[1], reverse=True)

    @classmethod
    def get_language_statistics(cls, filepath='polish_letters_statistics.csv')->list:
        """

        :param filepath:
        :return:
        """
        statistics = {}
        with open(filepath, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                statistics[row[0]] = cls._row_to_float(row[1])

        sorted_statistics = cls._sort_statistics(statistics)
        # # print(sorted_statistics)
        return sorted_statistics

    @classmethod
    def calculate_text_statistics(cls, cipher_text=None, is_char=True)->list:
        cipher_len = len(cipher_text)
        cipher_text = cls.get_cipher_text() if not cipher_text else cipher_text
        statistics = dict(Counter(cipher_text))
        if is_char:
            statistics = {k: round(v/cipher_len*100,2) for k,v in statistics.items() if k.isalpha()}
        else:
            statistics = {k: round(v/cipher_len*100,2)  for k,v in statistics.items()}

        sorted_cipher_letter_statisctics = cls._sort_statistics(statistics)
        # # print(sorted_cipher_letter_statisctics)
        return sorted_cipher_letter_statisctics

    @classmethod
    def draw_text_histogram(cls, statiscics=None, filename="cipher.png"):
        statiscics = cls.calculate_text_statistics() if not statiscics else statiscics
        cls._draw_histogram(statiscics, filename= filename)

    @classmethod
    def draw_polish_histogram(cls, statiscics=None, filename="polish.png"):
        statiscics = cls.get_language_statistics() if not statiscics else statiscics
        cls._draw_histogram(statiscics, filename=filename)

    @classmethod
    def _draw_histogram(cls, statiscics, filename="histogram.png"):
        # print(statiscics)
        x = [i[0] for i in statiscics]
        plt.bar(x, height=[i[1] for i in statiscics])
        plt.xticks(x,[i[0] for i in statiscics])  # no need to add .5 anymore
        plt.savefig(filename)
        # plt.show()


    @classmethod
    def map_text(cls, cipher_text, language_statistics=None, is_char=True)->str:
        language_stat = cls.get_language_statistics() if not language_statistics else language_statistics
        cipher_stat = cls.calculate_text_statistics(cipher_text, is_char=is_char)

        order_list_language = [i[0] for i in language_stat]
        order_list_cipher = [i[0] for i in cipher_stat]

        output = ''
        for letter in cipher_text:
            if letter.isalpha():
                cipher_index = order_list_cipher.index(letter)
                output+= order_list_language[cipher_index]
            else:
                output += ' '
        return output

    @classmethod
    def replace_by_list(cls, cipher_text:str, letter_dict:list)->str:
        output = cipher_text # str jest prosty - bez referencji

        for k, v in letter_dict:
            output = cls.replace_one_letter(output, k,v)

        return  output

    @classmethod
    def replace_one_letter(cls, cipher_text:str, first:str, second:str)->str:
        output = cipher_text # str jest prosty - bez referencji
        output = output.replace(second.upper(), '!')
        output = output.replace(first, second.upper())
        output = output.replace('!', first.upper())

        return  output

    @classmethod
    def replace_via_static(cls, cipher_text):
        cipher_stat = [ i[0] for i in cls.calculate_text_statistics(cipher_text)]
        lang_stat = [ i[0] for i in cls.get_language_statistics()]

        # # print(cipher_stat)
        # print(lang_stat)
        # print(cipher_text)

        # print("-----------------------------------")
        output = ''
        for cipher_char in cipher_text:
            try:
                # # print("cipher_char: ", cipher_char)
                index = cipher_stat.index(cipher_char)
                # # print("index: ", index)
                # # print("cipher_stat: ", cipher_stat)
        #
                stat_char = lang_stat[index]
                # # print("stat_char: ", stat_char)

            except ValueError:
                stat_char = ' '

            output += stat_char
        # # print("lang_stat: ", lang_stat)
        return output

    @classmethod
    def _ii(cls, cipher_text:str)->list:
        """Znajdowanie dwóch liter obok siebie i strzelanie że sa to dwa `ii` zgodnie z językiem polskim"""
        alphabet = [chr(letter) for letter in range(97, 123)]

        posible_letter_i = []

        for letter in alphabet + [' ']:
            pattern = letter + letter
            result = re.search(pattern, cipher_text)

            if result:
                posible_letter_i.append(letter)
        return posible_letter_i











