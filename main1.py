#cerintele 4, 10 si 13
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

def numere_prime(l):
    '''
    Functie de arata daca toate elementele unui subliste sunt prime.
    :param l: sublista cu numere intregi
    :return: True daca toate elemntele sunt prime, False in caz contrar
    '''
    for a in l:
        while a != 0:
            c = a % 10
            if c == 0:
                return False
            for b in range(2,c // 2 + 1):
                if c % b == 0:
                    return False
            a = a//10
    return True

def numere_pare(l):
    """
    Functie ce returneaza True daca toate elementele unei subliste sunt pare.
    :param l: lista de numere
    :return: True daca toate sunt pare, False in caz contrar
    """
    for x in l:
        if x % 2 != 0:
            return False
    return True


def get_longest_all_even(l):
    """
    Determina cea mai lunga secventa care are toate numerele pare
    :param l: lista cu numerele
    :return: secventa cea mai lunga de numere
    """
    subsecmax=[]
    for i in range(len(l)):
        for j in range(i, len(l)):
            if numere_pare(l[i:j+1]) and len(subsecmax) < len(l[i:j+1]):
                subsecmax= l[i:j+1]
    return subsecmax


def test_get_longest_all_even(l):
    assert get_longest_all_even([2,4,6,8,9,]) == [2,4,6,8]
    assert get_longest_all_even([1,3,5]) == []
    assert get_longest_all_even([1,9,10,3]) == [10]


def ordonare(l):
    '''
    Functia returneaza True daca toate elementele unei subsecvente sunt ordonate crescator.
    :param l: Lista de numere
    :return: True daca sunt ordonate crescator, False in caz contrar
    '''
    for x in l:
        if x < x + 1:
            return False
    return True

def get_longest_sorted_asc(l):
    '''
    Gasim cea mai lunga subsecventa de elemente din lista, ordonate crescator
    :param lst: Lista elementelor
    :return: Subsecventa cea mai lunga de numere
    '''
    subsecmax = []
    for i in range(len(l)):
        for j in range(i, len(l)):
            if ordonare(l[i:j + 1]) and len(subsecmax) < len(l[i:j + 1]):
                subsecmax = l[i:j + 1]
    return subsecmax


def test_get_longest_sorted_asc(l):
    assert get_longest_sorted_asc([10,5]) == []
    assert get_longest_sorted_asc([1,9,10,3]) == [1,9,10]


def get_longest_prime_digits(l):
    '''
    Determina cea mai lunga secventa ce are doar numere prime.
    :param l: lista cu numere
    :return: secventa cea mai lunga
    '''
    submax= []
    for i in range(len(l)):
        for j in range(i, len(l)):
            if numere_prime(l[i:j+1]) and len(submax) < len(l[i:j+1]):
                submax= l[i:j+1]
    return submax


def test_get_longest_prime_digits(l):
    assert get_longest_prime_digits([2,13,5,8,9]) == [2,13,5]
    assert get_longest_prime_digits([6,8,9]) == []
    assert get_longest_prime_digits([6,2,3,8,9,10,11,13,17]) == [11,13,17]

def main():
    l=[]
    test_get_longest_all_even(l)
    test_get_longest_prime_digits(l)
    '''test_get_longest_sorted_asc(l)'''
    while True:
        print("1. Citire date.")
        print("2. Determina cea mai lungă subsecvență cu proprietatea ca numerele sa fie ordonate crescator.")
        print("3. Determina cea mai lungă subsecvență cu proprietatea ca numerele sa fie formate din cifre prime.")
        print("4. Determina cea mai lunga subsecventa cu proprietatea ca numerele sa fie pare.")
        print("5. Iesire")
        op=input("Dati optiunea: ")
        if op == "5":
            break
        elif op == "1":
            citire()
        elif op == "2":
            print(get_longest_sorted_asc(l))
        elif op == "3":
            print(get_longest_prime_digits(l))
        elif op == "4":
            print(get_longest_all_even(l))
        else:
            print("!!!Optiunea nu este buna!!!")

main()
