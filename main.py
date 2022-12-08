class Product:
    """Takes the name and price of products."""

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f'Product "{self.name.capitalize()}" with price {self.price}'

    def cost_calc(self, quantity):
        return round(self.price * quantity, 2)


class ShoppingCart:
    """Takes the quantity, adds, displays and counts the total price of product."""

    def __init__(self):
        self.list_of_products = []
        self.list_of_quantities = []

    def add_to_list(self, prod, quantity):
        self.list_of_products.append(prod)
        self.list_of_quantities.append(quantity)

    def total_price_cart(self):
        total = 0
        for prod, quantity in zip(self.list_of_products, self.list_of_quantities):
            total += prod.cost_calc(quantity)
        return round(total, 2)


p1 = Product('beer', 35.2)
p2 = Product('cheese', 163.15)

cart = ShoppingCart()

cart.add_to_list(p1, 3)
cart.add_to_list(p2, 2)

cart.total_price_cart()
