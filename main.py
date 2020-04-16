class Beer:

 #Constructor
  def __init__ (self, company, quantity, unit, price, description, on_sale):
        self.company = company
        self.quantity = quantity
        self.unit = unit
        self.price = price
        self.description = description
        self.on_sale = on_sale

    # Getters
  def get_company(self):
        return self.company

  def get_quantity(self):
        return self.quantity

  def get_unit(self):
        return self.unit

  def get_price(self):
        return self.price

  def get_description(self):
        return self.description

  def get_on_sale(self):
        return self.on_sale

    # Setters
  def set_company(self, company):
        self.company = company

  def set_quantity(self, quantity):
        self.quantity = quantity

  def set_unit(self, unit):
        self.unit = unit

  def set_price(self, price):
        self.price = price

  def set_description(self, description):
        self.description = description

  def set_on_sale(self, on_sale):
        self.on_sale = on_sale

    # Methods
  def print_oxxo_ad(self):
        print(f'Cerveza {self.company} de {self.quantity} {self.unit} a tan sólo ${self.price}')

  def calculate_amount(self, quantity):
        return quantity * self.price

  def print_amount_to_pay(self, quantity):
        print(f'El total a pagar por {quantity} cervezas es de: {self.calculate_amount(quantity)}')

  def is_on_sale(self):
        print('A LA VENTA') if self.is_on_sale else print('EXISTENCIAS AGOTADAS')


def main():
    company = input('¿Qué marca es la cerveza?: ')
    unit = input('¿Qué unidad de volumen utiliza (ml, l, gal, etc): ')
    quantity = input(f'Cantidad de {unit} que contiene el envase: ')
    price = input('¿Cuánto cuesta la pieza?: ')
    description = input('¿Alguna descripción de la chela?: ')
    on_sale = True if input('¿Está actualmente a la venta? (S/N): ') == 'S' or input('¿Está actualmente a la venta?: ') == 's' else False

    # Creating new instance of out Beer class:
    beer = Beer(company, unit, quantity, price, description, on_sale)

    beer.print_oxxo_ad()
    beer.is_on_sale()
main()