from product import Product

p1 = Product('t-short', 50)
p1.discount(10)
print(p1.name, p1.price)

p2 = Product('Caneca', 15)
p2.discount(10)
print(p2.name, p2.price)
