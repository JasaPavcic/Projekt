import random
import os


def izracunaj_vsoto(roka):
    vsota = 0

    ne_as = [karta for karta in roka if karta != 'As' or 'Ak' or 'Ap' or 'Aka']
    As = [karta for karta in roka if karta == 'As' or 'Ak' or 'Ap' or 'Aka']

    for karta in ne_as:
        if karta in 'JQK':
            vsota += 10
        else:
            vsota += int(karta)

    for karta in As:
        if vsota <= 10:
            vsota += 11
        else:
            sum +=1

    return vsota



# vseh kart je 52
karte = [
    '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', '10s', 'Js', 'Qs', 'Ks', 'As',
    '2k', '3k', '4k', '5k', '6k', '7k', '8k', '9k', '10k', 'Jk', 'Qk', 'Kk', 'Ak',
    '2p', '3p', '4p', '5p', '6p', '7p', '8p', '9p', '10p', 'Jp', 'Qp', 'Kp', 'Ap',
    '2ka', '3ka', '4ka', '5ka', '6ka', '7ka', '8ka', '9ka', '10ka', 'Jka', 'Qka', 'Kka', 'Aka',

]

nove_karte = [
    '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', '10s', 'Js', 'Qs', 'Ks', 'As',
    '2k', '3k', '4k', '5k', '6k', '7k', '8k', '9k', '10k', 'Jk', 'Qk', 'Kk', 'Ak',
    '2p', '3p', '4p', '5p', '6p', '7p', '8p', '9p', '10p', 'Jp', 'Qp', 'Kp', 'Ap',
    '2ka', '3ka', '4ka', '5ka', '6ka', '7ka', '8ka', '9ka', '10ka', 'Jka', 'Qka', 'Kka', 'Aka',
]

random.shuffle(karte)


# vsak ima svojo vsoto denarja od katere se odšteva


diler = []
igralec = []



# dokler je poln seznam prvih kart
# while len(karte) > 0:

igralec.append(karte.pop())
diler.append(karte.pop())
igralec.append(karte.pop())
diler.append(karte.pop())


# TUKAJ SE MORAS UPOSTEVATI DRUGE IGRALCE

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print('Dilerjeve karte: [{}][?]'.format(diler[0]))
    print('Igralceve karte' + str(igralec))

    break