from collections import defaultdict

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if len(skus) == 0:
        return 0

    items = {c: 0 for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
    price = 0

    for c in skus:
        if c not in items:
            return -1
        else:
            items[c] += 1

    if items['E'] // 2 > 0:
        items['B'] -= items['E'] // 2
        if items['B'] < 0:
            items['B'] = 0

    if items['F'] // 3 > 0:
        items['F'] -= items['F'] // 3

    if items['R'] // 3 > 0:
        items['Q'] -= items['R'] // 3
        if items['Q'] < 0:
            items['Q'] = 0

    if items['N'] // 3 > 0:
        items['M'] -= items['N'] // 3
        if items['M'] < 0:
            items['M'] = 0

    if items['U'] // 4 > 0:
        items['U'] -= items['U'] // 4

    {S: 2, T: 1, X: 3, Y: 2, Z: 0}

    if sum([val for val in items['S', 'T', 'X', 'Y', 'Z']])

    price += (items['A'] // 5) * 200 + ((items['A'] % 5) // 3) * 130 + ((items['A'] % 5) % 3) * 50
    price += (items['B'] // 2) * 45 + (items['B'] % 2) * 30
    price += items['C'] * 20
    price += items['D'] * 15
    price += items['E'] * 40
    price += items['F'] * 10
    price += items['G'] * 20
    price += (items['H'] // 10) * 80 + ((items['H'] % 10) // 5) * 45 + ((items['H'] % 10) % 5) * 10
    price += items['I'] * 35
    price += items['J'] * 60
    price += (items['K'] // 2) * 120 + (items['K'] % 2) * 70
    price += items['L'] * 90
    price += items['M'] * 15
    price += items['N'] * 40
    price += items['O'] * 10
    price += (items['P'] // 5) * 200 + (items['P'] % 5) * 50
    price += (items['Q'] // 3) * 80 + (items['Q'] % 3) * 30
    price += items['R'] * 50
    price += items['S'] * 20
    price += items['T'] * 20
    price += items['U'] * 40
    price += (items['V'] // 3) * 130 + ((items['V'] % 3) // 2) * 90 + ((items['V'] % 3) % 2) * 50
    price += items['W'] * 20
    price += items['X'] * 17
    price += items['Y'] * 20
    price += items['Z'] * 21

    return price


