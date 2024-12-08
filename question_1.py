def max_profit():
    input_data = input("Enter input (n, [prices]): ")
    n_part, prices_part = input_data.split(",", 1)
    n = int(n_part.strip())
    prices = list(map(int, prices_part.strip().strip("[]").split(",")))

    if n <= 1:
        return 0

    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        max_profit = max(max_profit, price - min_price)

    return max_profit

print("Maximum profit:", max_profit())
