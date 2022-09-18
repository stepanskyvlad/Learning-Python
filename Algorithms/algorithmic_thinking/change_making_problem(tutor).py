def make_change(target_amount):
    denominations = [200, 100, 50, 20, 10, 5, 2, 1]  # Order is important
    coin_count = 0  # Initialise count
    values = []  # Store values here
    for coin in denominations:
        while target_amount >= coin:  # Use the current coin until its value is too large
            target_amount -= coin  # Decrease the remaining amount
            values.append(coin)  # Make a note of which coin was used
            coin_count += 1  # Increase the coin count
    return coin_count, values


print(make_change(24))  # 3: 20 + 2 + 2
print(make_change(163))  # 5: 100 + 50 + 10 + 2 + 1
