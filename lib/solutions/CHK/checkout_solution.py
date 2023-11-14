

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    basket_dict = {}
    for c in skus:
        if c in basket_dict.keys():
            basket_dict[c] += 1
        else:
            basket_dict[c] = 1

    
