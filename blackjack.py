import random
import os


def izracunaj_vsoto(roka):
    vsota = 0

    ne_as = [karta for karta in roka if karta[0] != 'A']
    As = [karta for karta in roka if karta[0] == 'A']

    for karta in ne_as:
        if karta[0] in 'JQK':
            vsota += 10
        elif int(karta[0]) == 1:
            vsota += 10
        else:
            vsota += int(karta[0])

# asov ne sešteva dobro

    for karta in As:
        if vsota <= 10:
            vsota += 11
        else:
            vsota += 1

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

standing = False
prva_roka = True

while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    igralceva_vsota = izracunaj_vsoto(igralec)
    dilerjeva_vsota = izracunaj_vsoto(diler)

    if standing:
        print('Dilerjeve karte: [{}] Dilerjeva vsota: ({})'.format(']['.join(diler), dilerjeva_vsota))
    else:
        print('Dilerjeve karte: [{}][?]'.format(diler[0]))

    print('Tvoje karte: [{}] Tvoja vsota: ({})'.format(']['.join(igralec), igralceva_vsota))
    print("")


    if standing:
        if dilerjeva_vsota > 21:
            print('Diler je BUSTED, zmagaš!')
        elif dilerjeva_vsota == igralceva_vsota:
            print('Izenačeno, vložek je povrnjen!')
        elif igralceva_vsota > dilerjeva_vsota:
            print('Zmagal si!')
        else:
            print('Zgubil si! :(')
        break 

    if prva_roka and igralceva_vsota == 21:
        print('BLACKJACK, Zmagaš!')
        break

    if igralceva_vsota > 21:
        print('Zgubil si! :(')
        break




# ne pozabi na split in double down

    print('Kaj boste naredili?')
    print('[1] hit')
    print('[2] stand')

    print("")
    izbira = input('Tvoja izbira: ')
    print("")

    if izbira == '1':
        igralec.append(karte.pop())
    elif izbira == '2':
        standing = True
        while izracunaj_vsoto(diler) <= 16:
            diler.append(karte.pop())

