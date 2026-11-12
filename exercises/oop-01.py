# question 01 


"""
student1 = {"name": "Dana", "grades": [90, 85]}
student2 = {"name": "Avi", "grades": [70]}
student3 = {"nmae": "Noa", "grades": []}

def average(student):
    return sum(student["grades"]) / len(student["grades"])
"""


"""
1) no rols or validations 
2) line 7 problem with "nmae"
3) the calcolation of ave with empty list 
"""



# question 02

class Product:
    def __init__(self, name, price, quantity=0):
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.name = name
        self.price = price
        self.quantity = quantity


pen = Product("Pen", 5)
print(pen.name, pen.price, pen.quantity)
try:
    Product("Bad", -10)
except ValueError as error:
    print("error:", error)

