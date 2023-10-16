class Product:
    
    def __init__(self, name, price, description) -> None:
        self.name = name
        self.price = price
        self.description = description
        self.available = True
    

class Shop:
    
    def __init__(self, name) -> None:
        self.name = name
        self.products = []
        
        
    def add_product(self, product):
        self.products.append(product)
    
    
    def list(self):
        for product in self.products:
            if product.available == True:
                print(product.name, product.price,'$')
            
    def buy_product(self, name):
        for pro in self.products:
            if pro.name == name:
                print('successfully done')
                pro.available = False
                return
            else:
                print('we do not have product', name)
                return



product1 = Product( 'anwars', 12, 'low of the case')
product2 = Product( 'anwarsdas', 12, 'low of the case')
product3 = Product( 'anwarsasd', 12, 'low of the case')



my_shop = Shop('anwar home')

my_shop.add_product(product1)
my_shop.add_product(product2)
my_shop.add_product(product3)


my_shop.buy_product('anwars')
my_shop.buy_product('and')

my_shop.list()
    
    