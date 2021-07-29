products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}
def get_product(product):
    return products[product]

def get_property(code, property):
    return products[code][property]

def main():
    orders=[]
    end=[]
    total=0
    while True:
        order=input("order please {product_code},{quantity}")
        if order=="/":
            break
        orders.append(order.split(","))
        show_once=list(set([x[0] for x in orders]))
        for i in show_once:
            amount=[i,0]
            for each in orders:
                if each[0]==i:
                    amount[1]+=int(each[1])
            end.append(amount)
        for product in end:
            name=get_property(product[0],"name")
            subtotal=int(product[1])*(get_property(product[0],"price"))
            total+=subtotal
            with open("receipt.txt","w") as receipt:
                receipt.write('''
    ==
    CODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL

            ''')
                with open("receipt.txt","a") as receipt:
                    receipt.write('\n'+f'{product[0]}\t\t{name}\t\t{product[1]}\t\t\t\t{subtotal}')

            with open('receipt.txt','a+') as receipt:
                receipt.write(f'''

    Total:\t\t\t\t\t\t\t\t\t\t{total})
    ==
            ''')
                receipt.seek(0)
                print(receipt.read())
