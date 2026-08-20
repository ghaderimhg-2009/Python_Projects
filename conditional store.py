price = int(input("قیمت را وارد کنید:"))
final_price = 0

if price >50000 : 
    final_price = int(price - (price * 0.20))
    print (f"مبلغ نهایی: {final_price}")
elif price >=20000 and price <=50000:
    final_price = int(price - (price * 0.10))
    print (f"مبلغ نهایی: {final_price}")
elif price <20000:
     print (f"مبلغ نهایی: {price}")