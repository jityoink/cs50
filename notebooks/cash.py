import math

while True:
    try:
        change = int(input("change owed(in cents)"))
        if change >= 0:
            coin_types = [25, 10, 5, 1]
            coin_count = 0
            a = 0
            while change >= 0 and a < len(coin_types):
                coins = 0
                if change >= coin_types[a]:
                    coins = math.floor(change / coin_types[a])
                coin_count = coins + coin_count
                change = change - (coins*coin_types[a])
                a = a + 1
            print(coin_count)
            break
        else:
            print("non-negative no. pls")
    except ValueError:
        print("invalid input, try again!")