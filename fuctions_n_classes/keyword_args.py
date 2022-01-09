def product_prices(**products):
    for k,v in products.items():
        print(f"{k} cost ${v}")
    print(f"total prices:${sum(products.vlues())}")    
    print(products)

product_prices(maggi= 50,mouse =2300, coffe = 399)
product_prices(maggi= 50 , coffee =399)    

print(range(300))