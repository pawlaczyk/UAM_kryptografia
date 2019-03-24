#coding=utf-8

"""
Złam szyfr RSA. Klucz publiczny prowadzącego to (n=462257, e=13). Udało Ci się przechwycić adresowany do niego
szyfrogram c=329549. Znajdź liczbę jaką jest wiadomość i wyślij do prowadzącego email o temacie:
ZKRR - RSA - <numerindeksu> <imię> <nazwisko> <znalezionaliczba>
(gdzie pod <imię>, <nazwisko>, <nr-indeksu> należy podstawić swoje odpowiednie dane osobowe, a pod
<znalezionaliczba> - znalezioną liczbę-wiadomość)
Treść wiadomości nie ma znaczenia. Możesz tam np. umieścić opis rozwiązywania, ale możesz też pozostawić ją pustą.
"""


def fme(a: int, k: int, n: int)->int: # bez tego mieli
    """Szybkie potegowanie modularne, wykorzsytuje operacje bitowe
    a ** k mod n
    :param a:
    :param k:
    :param n:

    """
    b = bin(k)[2:]  # list of bits
    m = len(b)
    r = 1  # result
    x = a % n

    for i in range(m - 1, -1, -1):
        if b[i] == '1':
            r = r * x % n

        x **= 2
        x %= n

    return r


def rozszerzonyEuklides(a, b): # nie dziala dla duzych liczb :<
    """ Obliczanie odwrotności dla liczby a mod b
    tzn. takiej liczby x dla której a*x mod b = 1;
    inaczej a*x przystaje do 1 mod b
    a - liczba, której odwrotność modulo obliczamy, a należy do N;
    b - moduł odwrotności, b należy do N
    u, w,x, z - współczynniki równań należą do Z (l.Całkowite)
    q - całkowity iloraz (floor) należy do Z (l.Całkowite)
    [!!!] w wersji 2.7 operacja / - dzielenie na l całkowitych daje
        liczbę naturalną np. 5/2 = 2  <- w wersji 3.x to DZIELENIE tak nie działa!
    """

    u = 1
    w = a # działamy aż w będzie == 0
    x = 0
    z = b

    while (w):
        if w < z:
            q = u
            u = x
            x = q
            q = w
            w = z
            z = q

        q = w/z
        u -=(q*x)
        w -= q*z

    if z == 1: # Bardzo wazny warunek!!!
        if x < 0:
            x += b
            return x

    return -1 # brak rozwiazania


# Took from SO
def egcd(a, b):  # nie moje
    """
    https://gist.github.com/ofaurax/6103869014c246f962ab30a513fb5b49
    :param a:
    :param b:
    :return:
    """
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b%a,a)
    return (g, x - (b//a) * y, y)

def modinv(a, m):  # nie moje
    """
    https://gist.github.com/ofaurax/6103869014c246f962ab30a513fb5b49
    :param a:
    :param m:
    :return:
    """
    g, x, y = egcd(a, m)
    if g != 1:
        raise ValueError('No modular inverse')
    return x%m

def prime_factorial(n: int)->tuple:
    """
    Rozkłada podaną liczbę `n` na dzwie liczby pierwsze
    Dla dużych liczb pierwszych

    :param n: liczba całkowita ktora rozkłada
    :return: krotka z dzielnika, w przypadku braku dzielników w postaci liczb pierwszych z plików z wikipedii
        zwraca (-1,-1)

    """
    with open('first.txt', 'r') as f:
        prime_numbers = [int(i) for i in f.readlines()]  # generator

    for prime in prime_numbers:
        if prime > (n**(1/2)):
            return -1, -1  # znaczy sie nie podzielna przez pierwsze z pliku

        if n % prime == 0:
            return prime, int((n/prime))

def gcd(a, b): # NWD (najwiekszy wspolny dzielnik)
    while b != 0:
        b, a = a % b, b
    return a

def f_euler(n:int)->int:
    """
    Funckja Eulera borzyszcze wszystkich grafofilów <3- zwraca moc zbioru podzielników liczny n

    :param n: liczba, dla której dzielników szukam
    :return divisors_number: ilość wszsytkich podzielników

    """
    # poprawione
    divisors_number = 0
    for i in range(1, n+1):
        if gcd(n, i) == 1:
            divisors_number += 1

    return divisors_number

def inverse_modulo(e:int, n:int)->int:
    """
    Odwrotnosc modulo, najbardziej paskudne liczenie
    :param e: 
    :param n: 
    :return: 
    """
    pass

def encrypt_RSA(m: int, e: int, n: int)->int:
    """
    Szyfrowanie za pomoca RSA (do sprawdzenia czy dobre rozszyfrowalo)
    m ** e (mod N) === c

    :param n:
    :param e:
    :param m:
    :return c: szyfrogram
    """
    c = fme(m, e, n)
    return int(c)

def decrypt_RSA(n: int, e: int, c: int)->tuple:
    """
    Deszyfrowanie wiadomosci zaszyfrowanej RSA znając klucz parę klucza publicznego

    :param n: n = (prime_numer1-1)*(prime_numer2-1)
    :param e: klucz publiczny ; losowe małe;  e należy (1; fi(n))
    :param c: szyfrgram int
    :returns (d:int,m:int): d- klucz prywatny, m - deszyfrowana wiadomosc
    """

    p1, p2 = prime_factorial(n)  # (503, 919); dla n = 462257
    if p1 == -1:
        raise ValueError("Podano nierozkładalne na liczby pierwsze `n`")

    fi = f_euler(p1)*f_euler(p2)  # korzystam z multiplikatywnosci
    print("FI: ", fi)
    d = modinv(e, fi)
    d = int(d)
    m = fme(c, d, n)  # Rozszerozny Euklides, bo inaczej mieli


    return d, m


def zad7(data:dict)->None:
    """
    Obliczenie wartosić dla zadania z https://renmich.faculty.wmi.amu.edu.pl/ZKRR/zajecia1.html

    :return: None

    # """
    n = data["n"]
    e = data["e"]
    c = data["c"]

    d, m = decrypt_RSA(n=n, e=e, c=c )
    print("KLUCZ PRYWATNY: ", d) #odwrotnosc modulo
    print("WIADOMOSC: ", m) # jest ok jest 20

    c = encrypt_RSA(m=m, e=e, n=n)
    print("SZYFROGRAM: ", c) # jest ok 41
    if c != data['c']:
        print("Coś się zesrało")

    print("________________________")


def main():
    data = {
        "n": 91,
        "e": 11,
        "c": 20
    }

    zad7(data)

    data = {
        "n": 35,
        "e": 23,
        "c": 20
    }

    zad7(data)

    data_old = {  # https://renmich.faculty.wmi.amu.edu.pl/EGO/zajecia1.html
        "n": 462257,
        "e": 13,
        "c": 54353
    }  # d = 35449

    zad7(data_old)

    data_old = { # https://renmich.faculty.wmi.amu.edu.pl/ZKRR/zajecia1.html
        "n": 462257,
        "e": 13,
        "c": 329549
    }  # d = 35449

    zad7(data_old)

    # Te co trzeba do końca marca
    data = {  # https://renmich.faculty.wmi.amu.edu.pl/ZEGO/zajecia1.html
        "n": 805787,
        "e": 13,
        "c": 57439
    }  # 61837

    print("Do końca marca")
    zad7(data)

if __name__ == "__main__":
    main()




