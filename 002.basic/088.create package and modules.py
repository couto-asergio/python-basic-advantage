"""
Create Package and Modules
"""

from sales.sale.calc_price import reduction, increase
from sales.format import price as price_2

price = 49.90
price_with_increase = increase(price, 15, format=True)
print(price_with_increase)

reduced_price = reduction(value=price, percentage=15, format=True)
print(reduced_price)

print(price_2.real(59.95))

