
class Product:
    def __init__(self, name, price, quantity=0):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.__name = name
        self.price = price
        self.__quantity = quantity

    @property
    def name(self):
        return self.__name
    @property
    def quantity(self):
        return self.__quantity

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("price cannot be negative")
        self._price = value

    def add_stock(self, amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        self.__quantity += amount

    def sell(self, amount): 
        if amount < 0:
            raise ValueError("aamount cannot be negative")
        if amount > self.__quantity:
            raise ValueError("not enough stock")
        self.__quantity -= amount
    @property
    def total_value(self):
            return self.price * self.__quantity
    def __str__(self):
        return f"{self.name}: {self.price}, quantity : {self.quantity}, total {self.total_value}"

class Inventory:
    def __init__(self):
        self.__products = []
    @property
    def products(self):
        return self.__products
    
    def add(self, product):
        if any(p.name == product.name for p in self.products):
            raise ValueError("product already exists")
        self.products.append(product)

    def find(self, name):
        for product in self.products:
            if product.name == name:
                return product
        raise ValueError("product not found")

    def by_value(self):
        return sorted(self.products, key=lambda p: p.total_value, reverse=True)

    @property
    def total_value(self):
        return sum(product.total_value for product in self.products)




shop = Inventory()
shop.add(Product("Pen", 5, 10))
shop.add(Product("Bag", 60, 2))
shop.add(Product("Notebook", 12, 5))

shop.find("Pen").sell(4)
shop.find("Bag").add_stock(1)

try:
    shop.find("Notebook").sell(50)
except ValueError as error:
    print("error:", error)
 
try:
    shop.add(Product("Pen", 7))
except ValueError as error:
    print("error:", error)
 
try:
    shop.find("Bag").price = -3
except ValueError as error:
    print("error:", error)
 
for product in shop.by_value():
    print(product)
print("Total:", shop.total_value)
