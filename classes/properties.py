class Product:
    def __init__(self, price):
        self.__price = price
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value
        
        
product = Product(100)
print(product.price)  # Accessing the price property
product.price = 150  # Setting a new price

print(product.price)  # Accessing the updated price

try:
    product.price = -50  # Attempting to set a negative price       
except ValueError as e:
    print(e)
    