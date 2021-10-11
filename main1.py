#cerintele 4 si 13
def citire():
    '''
    Citim elementele listei
    :return: elementele listei
    '''
    l = []
    n = int(input("Dati numarul de elemente: "))
    for i in range(n):
        l.append(int(input(f"l[{i}]= ")))
    return l

def elemente_prime(l):
    '''
    Functie de arata daca toate elementele unui subliste sunt prime.
    :param l: sublista cu numere intregi
    :return: True daca toate elemntele sunt prime, False in caz contrar
    '''
    for a in l:
        while a!=0:
            c=a%10
            if c==0:
                return False
            for b in range(2,c//2+1):
                if c % b == 0:
                    return False
            a=a//10
    return True


def ordonare(l):
    '''
    Functia returneaza True daca toate elementele unei subsecvente sunt ordonate crescator.
    :param l: Lista de numere
    :return: True daca sunt ordonate crescator, False in caz contrar
    '''
    for x in l:
        if x > x + 1:
            return False
    return True

def get_longest_sorted_asc(l):
    '''
    Gasim cea mai lunga subsecventa de elemente din lista, ordonate crescator
    :param lst: Lista elementelor
    :return: Subsecventa cea mai lunga de numere
    '''
    subsecvmax = []
    for i in range(len(l)):
        for j in range(i, len(l)):
            if ordonare(l[i:j + 1]) and len(subsecvmax) < len(l[i:j + 1]):
                subsecvmax = l[i:j + 1]
    return subsecvmax

def test_get_longest_sorted_asc(l):
    assert get_longest_sorted_asc([12, 4, 7, 6, 5, 10]) == [7, 6, 5]
    assert get_longest_sorted_asc([2, 6, 9, 13]) == []


def get_longest_prime_digits(l):
    '''
    Determina cea mai lunga secventa ce are doar numere prime.
    :param l: lista cu numere
    :return: secventa cea mai lunga
    '''
    submax= []
    for i in range(len(l)):
        for j in range(i, len(l)):
            if elemente_prime(l[i:j+1]) and len(submax) < len(l[i:j+1]):
                submax= l[i:j+1]
    return submax


def test_get_longest_prime_digits(l):
    assert get_longest_prime_digits([2,13,5,8,9]) == [2,13,5]
    assert get_longest_prime_digits([6,8,9]) == []
    assert get_longest_prime_digits([6,2,3,8,9,10,11,13,17]) == [11,13,17]

def menu():
    l = []
    test_get_longest_sorted_asc(l)
    test_get_longest_prime_digits(l)
    while True:
        print("1. Citeste datele.")
        print("2. Determina cea mai lunga subsecventa cu numere ordonate descrescator.")
        print("3. Determina cea mai lunga subsecventa cu numere care au acelasi numar de divizori.")
        print("4. Iesire.")
        op = input("Dati optiunea: ")
        if op == '4':
            break
        elif op == 1:
            citire()
        elif op == 2:
            print(get_longest_sorted_asc(l))
        elif op == 3:
            print(get_longest_prime_digits(l))
        else:
            print("Eroare. Reincercati")

menu()
