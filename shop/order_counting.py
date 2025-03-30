from shop.models import Product, Order


def getOrderData(cart):
    # cart example:  {'id': 3, 'user': 2, 'product': [13, 14, 15, 16]}
    price = 0
    for prod_id in cart.get('product'):
        product_from_id = Product.objects.get(id=prod_id)
        price += product_from_id.price

    return {
        "total_price": price,
        "status": "issued",
        "user": cart.get('user'),
        "product": cart.get('product')
    }


def getCart(user_id, carts):
    # Пример carts : [{'id': 7, 'user': 1, 'product': [2, 3, 4, 1]}]
    for cart in carts:
        if cart.get('user', None) is None:
            pass
        elif cart.get('user', None) == int(user_id):
            return cart
