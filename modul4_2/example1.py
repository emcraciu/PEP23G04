shop1 = {'apple': 10, 'banana': 12, 'plum': 13}
shop2 = {'apple': 11, 'banana': 12, 'plum': 10}
shop3 = {'apple': 15, 'banana': 7, 'plum': 12}
shops = {'prof': shop1, 'lid': shop2, 'kauf': shop3}

shopping_cart = {'apple': 3, 'banana': 2, 'plum': 5}


# def best_buy():# variable number of arguments):
#     pass

def best_buy(shops: dict, cart: dict) -> str:  # variable number of arguments):
    result_per_shop = {}
    for name, shop_products in shops.items():
        print(name, shop_products)
        result_per_shop[name] = 0
        for product, price in shop_products.items():
            print(product, price)
            result_per_shop[name] += cart.get(product) * price
            print(result_per_shop)


    return ''

best_buy(shops, shopping_cart)
