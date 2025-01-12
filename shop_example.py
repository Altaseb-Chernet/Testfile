#shop program by using pytohn in file handling
with open('shop_file.txt','w') as file:
    file.write('1\t banana\t 20\t 50\t\n')
    file.write('2\t habhab\t 35\t 30\n')
    file.write('3\t Apple\t 75\t 150\n')
    file.write('4\t orange\t 16\t 8\n')

#add new product to the existing product
def add_product(id,name,price,stock):
    with open('shop_file.txt','a') as file:
        file.write(f'{id}\t {name}\t {price}\t {stock}')
        print(f'{id}\t {name}\t {price}\t {stock}\n')
        print(f'the product {name} added successfully')

add_product(5,'grapes',30,90)

print()
print()
#view all the product 
def view_all():
    with open('shop_file.txt','r') as file:
        products = file.readlines()
        print('id\t name\t price\t stock')
        for product in products:
            print(product,end = '')
            
view_all()

#purchase the product as you want
def purchese_product(product_id,quantity):
    products = []
    with open('shop_file.txt','r') as file:
        products = file.readlines()
    with open('shop_file.txt','w') as file:
        for product in products:
            id,name,price,stock = product.strip().split('\t')
            if int(id) == product_id:
                if int(stock) >= quantity:
                    stock = int(stock) - quantity
                    print(f'\npurchesed {quantity} {name}(s).')
                else:
                    print(f'the product {product_id} not stock')
            file.write(f'{id}\t {name}\t {price}\t {stock}\n')
purchese_product(4, 8)
purchese_product(3, 7)
purchese_product(1, 6)