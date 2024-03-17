def josephus(n, k):
    if n == 1:
        return 0
    else:
        return (josephus(n - 1, k) + k) % n

# Example usage:
n = 7  # Number of people
k = 3  # Every k-th person will be executed
survivor_position = josephus(n, k)
print("The position of the survivor:", survivor_position + 1)
