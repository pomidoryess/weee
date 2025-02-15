class Product:
    def __init__(self, name, price, stock):
        self.name = name 
        self.price = price
        self.stock = stock

    def __str__(self):
        return f'{self.name} - ${self.price} (кількість: {self.stock})'


class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product, quantity):
        if product.stock >= quantity:
            self.items.append({'product': product, 'quantity': quantity})
            product.stock -= quantity
            print(f'додано {quantity} {product.name} до кішика')
        else:
            print(f'не хвата {product.name}. лише {product.stock} зісталось')

    def remove_product(self, product_name):
        for item in self.items:
            if item['product'].name == product_name:
                self.items.remove(item)
                item['product'].stock += item['quantity']
                print(f'прибрано {item["quantity"]} {product_name} з кішика')
                return
        print(f'{product_name} не знайдено')

    def total_price(self):
        total = sum(item['product'].price * item['quantity'] for item in self.items)
        return total

    def show_cart(self):
        if not self.items:
            print("кошик пустий лол")
        else:
            for item in self.items:
                print(f'{item["quantity"]} x {item["product"].name} - ${item["product"].price * item["quantity"]}')
            print(f'загалом: ${self.total_price()}')

# приклад оцього во
p1 = Product("нотбук", 1000, 10)
p2 = Product("мобілка", 500, 5)
cart = Cart()
cart.add_product(p1, 2)
cart.add_product(p2, 3)
cart.show_cart()
cart.remove_product("нотбук")
cart.show_cart()
