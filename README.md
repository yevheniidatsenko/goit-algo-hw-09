### Greedy Algorithms and Dynamic Programming

Welcome to the assignment on "Greedy Algorithms and Dynamic Programming"!

Studying greedy algorithms and dynamic programming along with practical problem-solving will enhance your skills in optimization and algorithm analysis.

By completing this assignment:

- You will deepen your knowledge and understanding of implementing greedy algorithms and dynamic programming algorithms.
- You will have the opportunity to apply theoretical knowledge in practice: developing functions for a greedy algorithm and a dynamic programming algorithm will help you better understand their real nature and application.
- By comparing the efficiency of two different methods for solving the same problem, you will learn to conduct objective analysis and understand which method may be more effective under specific conditions.

### Task Description

In the lecture notes, we discussed an example of breaking down a sum into coins. We have a set of coins [50, 25, 10, 5, 2, 1]. Imagine you are developing a system for a cash register that needs to determine the optimal way to give change to a customer.

You need to write two functions for the cash register system that gives change to the customer:

1. **Greedy Algorithm Function `calculate_change_greedy`**: This function should take the amount to be given as change and return a dictionary with the number of coins of each denomination used to make up that amount. For example, for the amount of 113, it would return the dictionary {50: 2, 10: 1, 2: 1, 1: 1}. The algorithm should be greedy, meaning it selects the largest available coin denominations first.

2. **Dynamic Programming Function `calculate_min_change`**: This function should also take the amount to be given as change but use the dynamic programming method to find the minimum number of coins needed to make up that amount. The function should return a dictionary with the denominations of coins and their quantities to achieve the given amount in the most efficient way. For example, for the amount of 113, it would return the dictionary {1: 1, 2: 1, 10: 1, 50: 2}.

Compare the efficiency of the greedy algorithm and the dynamic programming algorithm based on their execution time or Big-O notation, paying attention to their performance with large amounts. Highlight how they handle large amounts and why one algorithm may be more effective than the other in certain situations. Add your conclusions to the readme.md file of the assignment.

### Results

The execution times for different amounts are as follows:

| Amount | Greedy Time (s) | DP Time (s) |
| ------ | --------------- | ----------- |
| 10     | 0.00031229      | 0.00544050  |
| 55     | 0.00033304      | 0.03168008  |
| 113    | 0.00041787      | 0.06787208  |
| 207    | 0.00038887      | 0.12788504  |
| 505    | 0.00033187      | 0.34832750  |
| 1001   | 0.00033771      | 0.71953683  |

### Comparison:

**Greedy Algorithm**:

- **Time Complexity**: O(n), where n is the number of different coin denominations. This is because the algorithm iterates through the list of denominations.
- **Advantages**:
  - Very fast and simple to implement.
  - Execution time remains almost constant even for large amounts.
- **Disadvantages**:
  - Does not always ensure the minimum number of coins for certain sets of coin denominations.
  - Less flexible for varying sets of coin denominations.

**Dynamic Programming Algorithm**:

- **Time Complexity**: O(n \* m), where n is the amount of change and m is the number of different coin denominations. This is because the algorithm iterates through the list of denominations for each value up to the given amount.
- **Advantages**:
  - Always finds the minimum number of coins for any amount.
  - More adaptable to different sets of coin denominations.
- **Disadvantages**:
  - Significantly slower, especially for large amounts.
  - Execution time increases with the amount.

### Conclusion:

The greedy algorithm is efficient and quick for scenarios where it is not critical to minimize the number of coins. However, the dynamic programming algorithm is more suitable for scenarios where minimizing the number of coins is essential, despite its slower performance. The choice between the two algorithms depends on the specific requirements of the cash register system.
