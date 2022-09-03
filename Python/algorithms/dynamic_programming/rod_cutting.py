"""
Optimal rod-cutting is a classic dynamic programming problem. You are given a rod of length N and a price table that
maps rod lengths (i..N) to prices (i...N). The goal is to find the cut sequence that maximizes revenue.

Optimal substructure lemma:

Optimal Revenue (N) = max (i...N) { price[i] + Optimal Revenue (N - i) }

In other words, the optimal cut & revenue for a rod of length N is the initial cut + the optimal cut over the remainder of the
rod that maximizes optimal revenue for the entire rod.

We just have to find the initial cut that is the best in terms of maximizing revenue.

"""


class RodCutter:
    def __init__(self, price_table, rod_length):
        self.price_table = price_table
        self.rod_length = rod_length
        self.rev_table = [0] * rod_length
        self.cut_table = [0] * rod_length

    def __init_tables(self):
        self.rev_table[0] = self.price_table[str(1)]

    def find_optimal_rod_cut(self):
        for j in range(1, self.rod_length):
            rev = 0
            cut = 0
            for i in range(j + 1):
                this_rev = self.price_table[str(i + 1)] + self.rev_table[j - i - 1]
                if this_rev > rev:
                    rev = this_rev
                    cut = i

            self.rev_table[j] = rev
            self.cut_table[j] = cut

    def print_optimal_solution(self):
        cut_index = self.rod_length - 1
        cut_seq = []
        for i in range(self.rod_length - 1, -1, -1):
            current_cut = self.cut_table[cut_index]
            next_cut = cut_index - current_cut
            if next_cut == 0:
                break
            elif current_cut < next_cut:
                cut_seq.insert(0, current_cut + 1)
                break
            else:
                cut_seq.insert(0, current_cut + 1)
                cut_index = next_cut

        print(f"Optimal Revenue: {self.rev_table[-1]}")
        print(f"Optimal Cut Sequence: {cut_seq}")

    def run(self):
        if self.rod_length > 0:
            self.__init_tables()
            self.find_optimal_rod_cut()
            self.print_optimal_solution()
        else:
            print("There is no solution because rod has zero length.")


if __name__ == '__main__':
    # Declare price table & rod length
    price_table = {'1': 1, '2': 5, '3': 8, '4': 9, '5': 10, '6': 17, '7': 17, '8': 20, '9': 24, '10': 30}
    for i in range(11):
        rod_length = i
        print(f"Rod Length: {rod_length}")
        rod_cutter = RodCutter(price_table=price_table, rod_length=rod_length)
        rod_cutter.run()
        print("-----------------------------")