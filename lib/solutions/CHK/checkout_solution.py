

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if len(skus) == 0:
        return 0
    items = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}
    price = 0
    basket_dict = {}

    for c in skus:
        if c not in items:
            return -1
        else:
            items[c] += 1

    if items['E'] // 2 > 0:
        items['B'] -= items['E'] // 2
        if items['B'] < 0:
            items['B'] = 0

    price_A = (items['A'] // 5) * 200 + ((items['A'] % 5) // 3) * 130 + ((items['A'] % 5) % 3) * 50
    price_B = (items['B'] // 2) * 45 + (items['B'] % 2) * 30
    price_C = items['C'] * 20
    price_D = items['D'] * 15
    price_E = items['E'] * 40

    return price_A + price_B + price_C + price_D + price_E


