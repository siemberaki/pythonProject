class item:
    def calculate_total_price(self, unit, price):
        return unit * price


item1 = item()
item1.unit = 2
item1.price = 3
print(item1.calculate_total_price(item1.unit, item1.price))





