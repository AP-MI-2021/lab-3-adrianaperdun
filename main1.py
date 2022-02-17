import math


def get_longest_all_perfect_squares(lst: list):
    longest=0
    longest_poz=0
    lungime_actuala=0
    actual_poz=-1
    poz=-1
    for i in lst:
        poz=poz+1
        if math.sqrt(i)==math.isqrt(i) and i!=0:
            lungime_actuala=lungime_actuala+1
            if lungime_actuala==1:
                actual_poz=poz
        else:
            lungime_actuala=0
            actual_poz=0
        if lungime_actuala>longest:
            longest=lungime_actuala
            longest_poz=actual_poz
    lst2=[]
    if actual_poz != -1:
        for i in range(longest_poz, longest_poz + longest):
            lst2.append(lst[i])
    return lst2


def get_longest_average_below(lst, average):
    ceamailunga=0
    poz=-1
    for i in range (0,len(lst)):
        for j in range(i+1,len(lst)):
            suma=0
            for k in range (i,j+1):
                if k!=len(lst):
                    suma=suma+lst[k]
            if suma/(j-i+1)<average and ceamailunga<j-i+1:
                ceamailunga=j-i
                poz=i
    lst2=[]
    if poz!=-1:
        for i in range(poz,ceamailunga+poz+1):
            lst2.append(lst[i])
    return lst2


def get_longest_div_k(lst,k):
    longest = 0
    longest_poz = 0
    lungime_actuala = 0
    actual_poz = -1
    poz = -1
    for i in lst:
        poz = poz + 1
        if i%k==0:
            lungime_actuala = lungime_actuala + 1
            if lungime_actuala == 1:
                actual_poz = poz
        else:
            lungime_actuala = 0
            actual_poz = 0
        if lungime_actuala > longest:
            longest = lungime_actuala
            longest_poz = actual_poz
    lst2 = []
    if actual_poz != -1:
        for i in range(longest_poz, longest_poz + longest):
            lst2.append(lst[i])
    return lst2

def test_get_longest_all_perfect_squares():
    assert get_longest_all_perfect_squares([])==[]
    assert get_longest_all_perfect_squares([25])==[25]
    assert get_longest_all_perfect_squares([0])==[]
    assert get_longest_all_perfect_squares([10, 9, 25])==[9, 25]

def test_get_longest_div_k():
    assert get_longest_div_k([5,10,4,25],5)==[5,10]
    assert get_longest_div_k([0,1,2,3,4],2)==[0]
    assert get_longest_div_k([1,2,3,4,5],1)==[1,2,3,4,5]

def test_get_longest_average_below():
    assert get_longest_average_below([1,2,3],1.6)==[1,2]
    assert get_longest_average_below([9, 10, 1990],13)==[9,10]
    assert get_longest_average_below([1,2,3],1)==[]
def main():
    while True:
        print("1.Cea mai lunga secventa de patrate perfecte dintr-o lista data.")
        print("2.Cea mai lunga secventa cu proprietatea ca media numerelor din subsecventa este mai mica decat o valoare data .")
        print("3.Cea mai lunga secventa cu proprietatea ca toate numerele din subsecventa sunt divizibile cu un numar dat.")
        print("4.Iesire din program.")
        optiune = input("Alege optiunea:")
        if optiune == '1':
            test_get_longest_all_perfect_squares()
            lst = []
            n = int(input("Numarul de numere:"))
            for i in range(0, n):
                lst.append(int(input("Dati " + str(n) + " numere:")))
            print(get_longest_all_perfect_squares(lst))
        elif optiune == '2':
            test_get_longest_average_below()
            lst = []
            n = int(input("Numarul de numere:"))
            for i in range(0, n):
                lst.append(int(input("Dati " + str(n) + " numere:")))
            average=float(input("Valoarea data pentru medie:"))
            print( get_longest_average_below(lst,average))
        elif optiune == '3':
            test_get_longest_div_k()
            lst=[]
            n = int(input("Numarul de numere:"))
            for i in range(0, n):
                lst.append(int(input("Dati " + str(n) + " numere:")))
            k = int(input("Numarul cu care trebuie sa fie divizibile elementele secventei:"))
            print(get_longest_div_k(lst,k))
        elif optiune == '4':
            break
main()
