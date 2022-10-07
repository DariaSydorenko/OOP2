class Product:
    def __init__(self, price, description, dimension):
        if price > 0:
            self.price = price
        else:
            raise ValueError
        self.description = description
        self.dimension = dimension

    def information(self):
        return f'Product:\n' \
               f'Price: {self.price}\n' \
               f'Description: {self.description}\n' \
               f'Dimension: {self.dimension}\n'


class Customer:
    def __init__(self, surname, name, patronymic, mobile_phone):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.mobile_phone = mobile_phone

    def information(self):
        return f' \nCustomer:\n' \
               f'Surname: {self.surname}\n' \
               f'Name: {self.name}\n' \
               f'Patronymic: {self.patronymic}\n' \
               f'Mobile phone: {self.mobile_phone}\n'


class Order:
    def __init__(self, product, customer, quantity):
        self.product = product
        self.customer = customer
        self.quantity = quantity

    def information(self):
        return f'\nOrder:\n{self.product.description} - {self.quantity} psc.\n'

    def total_cost(self):
        return f'\nTotal order value: {self.product.price * self.quantity}\n'


my_product = Product(30000, 'PlayStation 5', '120, 100')
my_customer = Customer('Sydorenko', 'Daria', 'Volodymyrivna', '+381234567890')
my_order = Order(my_product, my_customer, 3)
print(my_product.information(), my_customer.information(), my_order.information(), my_order.total_cost())
