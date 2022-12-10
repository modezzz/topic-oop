class Product:

    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def __repr__(self) -> str:
        return f'Product "{self.name.capitalize()}" with price {self.price}'

    def __str__(self) -> str:
        return self.name

    def cost_calc(self, quantity: int | float) -> float:
        return round(self.price * quantity, 2)

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price

    def __float__(self):
        return float(self.price)


class ShoppingCart:

    def __init__(self, products=None) -> None:
        self.list_of_products = []
        self.list_of_quantities = []

        if products is not None:
            if type(products) == list:
                for prod in products:
                    self.add_to_list(prod, 1)
            elif type(products) == Product:
                self.add_to_list(products, 1)

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

    def __float__(self):
        return self.total_price_cart()

    def __add__(self, other):
        if type(other) == Product:
            self.add_to_list(other, 1)
        elif type(other) == ShoppingCart:
            new_cart = ShoppingCart()
            for prod, quantity in zip(self.list_of_products, self.list_of_quantities):
                new_cart.add_to_list(prod, quantity)
            for prod, quantity in zip(other.list_of_products, other.list_of_quantities):
                new_cart.add_to_list(prod, quantity)
            return new_cart


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

same_apple = Product('apple', 10.59)
assert apple == same_apple

obj2 = ShoppingCart()
obj2.add_to_list(apple, 0.35)
obj2.add_to_list(juice, 4)
obj2.add_to_list(apple, 0.35)

print(float(obj2))

obj3 = obj + obj2

print(float(obj3))

