class Product:
    """Takes the name and price of products."""

    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def __repr__(self) -> str:
        return f'Product "{self.name.capitalize()}" with price {self.price}'

    def __str__(self) -> str:
        return self.name

    def cost_calc(self, quantity: int | float) -> float:
        return round(self.price * quantity, 2)


class ShoppingCart:
    """Takes the quantity, adds, displays and counts the total price of product."""

    def __init__(self) -> None:
        self.list_of_products = []
        self.list_of_quantities = []

    def __repr__(self) -> str:
        return '<ShoppingCart>'

    def add_to_list(self, prod: Product, quantity: int | float) -> None:
        if prod in self.list_of_products:
            elem = self.list_of_products.index(prod)
            self.list_of_quantities[elem] += quantity
        else:
            self.list_of_products.append(prod)
            self.list_of_quantities.append(quantity)

    def total_price_cart(self) -> float:
        total = 0
        for prod, quantity in zip(self.list_of_products, self.list_of_quantities):
            total += prod.cost_calc(quantity)
        return round(total, 2)


apple = Product('apple', 10.59)
# apple.name = "apple"
# apple.price = 10.59
juice = Product('juice', 36.55)
# juice.name = "juice"
# juice.price = 36.55

obj = ShoppingCart()
obj.add_to_list(apple, 0.35)
obj.add_to_list(juice, 4)
obj.add_to_list(apple, 0.35)

assert obj.total_price_cart() == 153.61
