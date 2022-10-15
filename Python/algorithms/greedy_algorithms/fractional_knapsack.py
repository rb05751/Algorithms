"""
In fractional knapsack, you are given N items with some value (v) and weight (w) and your goal is to fill up a knapsack
of capacity (W). The difference between fractional & non-fractional knapsack, is that you are now able to store
fractional pieces of the items in the knapsack.

Algorithm:

1. Calculate value per weight (v/w) for each item.
2. Sort items in descending order of (v/w).
3. Starting with the first item take as much as possible until you run out of the first item.
4. If you still have capacity left in your knapsack, take as much of the next until you either run out of capacity
   or run out of item.
5. Repeat until you run out of capacity.

Proof:

- Assume we have constructed an optimal solution by following the above procedure except that when filling in the last
  (k) units of your knapsack, you chose a lower v/w density of the items.
- Now, imagine we remove the last (k) units of density from the knapsack & replace them with a same-size density from
  an earlier item in the ordering, that was not originally included.
- We have just constructed an even more optimal solution by doing so. Thus, contradicting our purported optimality.
  Thus, we should include any earlier densities before any further less v/w densities.
"""


class FractionalKnapsack:
    def __init__(self, items, max_capacity):
        self.items = items
        self.N = len(items)
        self.W = max_capacity

    def pre_process(self):
        # 1. Calculate value per weight for each item
        for item in self.items:
            item['v_per_w'] = item['v'] / item['w']

        # 2. Sort by value per weight
        self.items = list(sorted(self.items, key=lambda x: x['v_per_w'], reverse=True))

    def compute(self):
        self.pre_process()
        capacity_left = W
        total_value = 0
        knapsack = []
        for item in self.items:
            if capacity_left == 0: break
            if item['w'] < capacity_left:
                item['percent_taken'] = 1
                knapsack.append(item)
                capacity_left -= item['w']
                total_value += item['v']
            else:
                item['percent_taken'] = capacity_left / item['w']
                knapsack.append(item)
                capacity_left = 0
                total_value += item['percent_taken'] * item['v']
                break

        return total_value, knapsack


if __name__ == '__main__':
    items = [{'v': 6, 'w': 4}, {'v': 8, 'w': 2}, {'v': 3, 'w': 4}, {'v': 4, 'w': 4}, {'v': 10, 'w': 3}]
    N = len(items)
    W = 10

    fractional_knapsack = FractionalKnapsack(items=items, max_capacity=W)

    total_value, knapsack = fractional_knapsack.compute()

    print("Items In Knapsack")
    print(knapsack)
    print("-------------------")
    print(f"Total Value: {total_value}")
