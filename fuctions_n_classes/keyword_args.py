def product_prices(**products):
    for k,v in products.items():
        print(f"{k} cost ${v}")
    print(f"total prices:${sum(products.vlues())}")    
    print(products)

product_prices(maggi= 50,mouse =2300)
product_prices(maggi= 67)    