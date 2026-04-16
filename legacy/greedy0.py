coin_list = [1, 100, 50, 500]

def min_coin_count(value, coin_list):
    coin_list.sort(reverse=True)
    total_coin_count = 0
    details = list()
    for coin in coin_list:
        coin_count = value // coin
        total_coin_count  += coin_count
        value = value % coin
        