import random
import os

# vseh kart je 52
karte = [
    '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS', 'AS',
    '2K', '3K', '4K', '5K', '6K', '7K', '8K', '9K', '10K', 'JK', 'QK', 'KK', 'AK',
    '2P', '3P', '4P', '5P', '6P', '7P', '8P', '9P', '10P', 'JP', 'QP', 'KP', 'AP',
    '2Ka', '3Ka', '4Ka', '5Ka', '6Ka', '7Ka', '8Ka', '9Ka', '10Ka', 'JKa', 'QKa', 'KKa', 'AKa',

]

nove_karte = [
    '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS', 'AS',
    '2K', '3K', '4K', '5K', '6K', '7K', '8K', '9K', '10K', 'JK', 'QK', 'KK', 'AK',
    '2P', '3P', '4P', '5P', '6P', '7P', '8P', '9P', '10P', 'JP', 'QP', 'KP', 'AP',
    '2Ka', '3Ka', '4Ka', '5Ka', '6Ka', '7Ka', '8Ka', '9Ka', '10Ka', 'JKa', 'QKa', 'KKa', 'AKa',
]

random.shuffle(karte)


# vsak ima svojo vsoto denarja od katere se odšteva
a = 50
b = 50
c = 50

denarnica_igralec = a
denarnica_igralec_2 = b
denarnica_igralec_3 = c


diler = []
igralec = []
igralec_2 = []
igralec_3 = []
kos = []


# dokler je poln seznam prvih kart
# while len(karte) > 0:
igralec.append(karte.pop())
igralec_2.append(karte.pop())
igralec_3.append(karte.pop())
diler.append(karte.pop())
igralec.append(karte.pop())
igralec_2.append(karte.pop())
igralec_3.append(karte.pop())
diler.append(karte.pop())
# to še pogruntaj nekak
    # igralec.append(nove_karte.pop())
    # igralec_2.append(nove_karte.pop())
    # igralec_3.append(nove_karte.pop())
    # delilec.append(nove_karte.pop())
    # igralec.append(nove_karte.pop())
    # igralec_2.append(nove_karte.pop())
    # igralec_3.append(nove_karte.pop())
    # delilec.append(nove_karte.pop())

while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    print('Dilerjeve karte: [{}][?]'.format(diler[0]))
    print('Igralčeve karte: [{}] ({})'.format(']['.join(igralec), 000)
    print('Igralčeve karte: [{}] ({})'.format(']['.join(igralec_2), 000)
    print('Igralčeve karte: [{}] ({})'.format(']['.join(igralec_3), 000)
    
    break