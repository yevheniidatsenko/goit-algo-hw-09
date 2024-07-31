import timeit

# Available coin denominations
denominations = [50, 25, 10, 5, 2, 1]


def calculate_change_greedy(amount):
    """Calculate change using a greedy algorithm."""
    change = {}
    for denomination in denominations:
        count = amount // denomination
        if count > 0:
            change[denomination] = count
            amount %= denomination
    return change


def calculate_min_change(amount):
    """Calculate minimum change using dynamic programming."""
    min_coins = [0] + [float("inf")] * amount
    coin_counts = [{} for _ in range(amount + 1)]

    for denomination in denominations:
        for x in range(denomination, amount + 1):
            if min_coins[x - denomination] + 1 < min_coins[x]:
                min_coins[x] = min_coins[x - denomination] + 1
                coin_counts[x] = coin_counts[x - denomination].copy()
                coin_counts[x][denomination] = coin_counts[x].get(denomination, 0) + 1

    return coin_counts[amount]


def benchmark_functions(amounts):
    """Benchmark the greedy and dynamic programming functions."""
    results = []
    for amount in amounts:
        time_greedy = timeit.timeit(lambda: calculate_change_greedy(amount), number=1000)
        time_dp = timeit.timeit(lambda: calculate_min_change(amount), number=1000)
        results.append([amount, time_greedy, time_dp])
    return results


def print_benchmark_results(results):
    """Print the benchmark results."""
    print("Amount | Greedy Time (s) | DP Time (s)")
    for result in results:
        print(f"{result[0]:>6} | {result[1]:>14.8f} | {result[2]:>12.8f}")


def main():
    amounts = [10, 55, 113, 207, 505, 1001]
    results = benchmark_functions(amounts)
    print_benchmark_results(results)


if __name__ == "__main__":
    main()