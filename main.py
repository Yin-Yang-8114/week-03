class Persom:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"hello  my name is {self.name} and I am {self.age} years old."


chaim = Persom("Chaim", 22)
michael = Persom("Michael", 25)

print(chaim.greet())
michael.greet()
