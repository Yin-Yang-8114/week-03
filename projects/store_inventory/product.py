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
