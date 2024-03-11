def coinChange(coins, amount):
    # Create a list to store the minimum number of coins needed for each amount
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Base case: 0 coins needed to make amount 0

    # Iterate through each coin denomination
    for coin in coins:
        # Update dp[i] if using coin reduces the number of coins needed to make amount i
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[amount] is still float('inf'), it means no combination of coins can make up the amount
    return dp[amount] if dp[amount] != float('inf') else -1

# Example usage:
coins = [1, 2, 5]
amount = 11
print(coinChange(coins, amount))
