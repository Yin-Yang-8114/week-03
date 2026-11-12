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
        return None

    def by_value(self):
        return sorted(self.products, key=lambda p: p.total_value, reverse=True)

    @property
    def total_value(self):
        return sum(product.total_value for product in self.products)