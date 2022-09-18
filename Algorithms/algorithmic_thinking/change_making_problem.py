def make_change(target_amount):
    coin_list = [200, 100, 50, 20, 10, 5, 2, 1]
    new_list = []
    coin_sum = 0
    # I made mistake. In greedy algorithms we do not revisit choices once made
    while coin_sum != target_amount:
        for i in coin_list:
            if i + coin_sum <= target_amount:
                coin_sum += i
                new_list.append(i)
                break

    return len(new_list), new_list


print(make_change(24))  # 3: 20 + 2 + 2
print(make_change(163))  # 5: 100 + 50 + 10 + 2 + 1
