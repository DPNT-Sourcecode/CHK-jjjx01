

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    legal_inputs = {'A', 'B', 'C', 'D'}
    price = 0
    basket_dict = {}

    for c in skus:
        if c not in legal_inputs:
            return -1
        if c in basket_dict.keys():
            basket_dict[c] += 1
        else:
            basket_dict[c] = 1

    if basket_dict['A'] // 3 >= 1:
        price += (basket_dict['A'] // 3) * 130
        price += (basket_dict['A'] % 3) * 50
    else:
        price += basket_dict['A'] * 50

    if basket_dict['B'] // 2 >= 1:
        price += (basket_dict['B'] // 2) * 45
        price += (basket_dict['B'] % 2) * 30
    else:
        price += basket_dict['B'] * 30

    if 'C' in basket_dict.keys():
        price += basket_dict['C'] * 20
    if 'D' in basket_dict.keys():
        price += basket_dict['D'] * 15

    return price

