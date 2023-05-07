price = int(input("Enter the price of yours purchase: "))
discount = 0
if price < 100:
    discount = 0.05
elif 100 <= price < 200:
    discount = 0.1
elif price >= 200:
    discount = 0.15
print(f"Your disThe price of your purchase with the discount is {price - (price*discount)}")
