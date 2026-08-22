products = { 
    "laptap":85000000,
    "phone":35000000,
    "mouse":800000,
    "keyboard":1200000
}
print(f"list1: {products} \n")

products["mouse"] = "1000000"
print(f"lisst2: {products} \n")

products["charger"] = "500000"
print(f"lisst3: {products} \n")

del products["phone"]
print(f"lisst4: {products} \n")

print(f"lisst5: {products.keys()} \n")

print(f"lisst6: {products.values()} \n")

print(f"lisst7: {products.items()} \n")