def greedy(amount, denominations):
    coins_used = []

    for coin in reversed(denominations):
        while amount >= coin:
            coins_used.append(coin)
            amount -= coin

    return coins_used

amount = 5550
coin_denominations = [1, 2, 5, 10, 20, 50,100,200,500]
# if amount in coin_denominations:
#     coin_denominations.remove(amount)
result = greedy(amount, coin_denominations)
print("Coins Used:", result)
print("Total Coins:", len(result)) 