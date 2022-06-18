"""This algorithm is used to compute the maximum size subarray in Theta(nlogn) time."""
import copy


class FindMaxSubArray:
    def __init__(self, items):
        self.items = items
        self.n = len(items)

    def find_max_subarray_3(self, num_list):
        """This is a brute force implementation that runs in O(n^2)"""
        low, high, amt = 0, 0, -100000
        for i in range(len(num_list)):
            for j in range(i + 1, len(num_list)):
                if sum(num_list[i:j]) > amt:
                    low, high, amt = i, j, sum(num_list[i:j])
        return low, high, amt

    def find_max_crossing_subarray(self, A, low, mid, high):
        # print(f"Finding the max subarray for this array: {A} with these indices: {low}, {mid}, {high}")
        max_left = None
        left_sum = -10000000000
        sum = 0
        for i in range(mid, low - 1, -1):
            sum += A[i]
            if sum > left_sum:
                left_sum = sum
                max_left = i

        """Find right subarray sum"""
        max_right = None
        right_sum = -10000000000
        sum = 0
        for j in range(mid + 1, high):
            sum += A[j]
            if sum > right_sum:
                right_sum = sum
                max_right = j

        return max_left, max_right, left_sum + right_sum

    def find_max_subarray_2(self, A, low, high):
        """Recursive implementation that runs in O(nlogn)"""
        if high == low:
            return low, high, A[low]
        else:
            mid = (low + high) // 2
            left_low, left_high, left_sum = self.find_max_subarray(A, low, mid)
            right_low, right_high, right_sum = self.find_max_subarray(A, mid + 1, high)
            cross_low, cross_high, cross_sum = self.find_max_crossing_subarray(A, low, mid, high)

            if left_sum >= right_sum and left_sum >= cross_sum:
                return left_low, left_high, left_sum
            elif right_sum >= left_sum and right_sum >= cross_sum:
                return right_low, right_high, right_sum
            else:
                return cross_low, cross_high, cross_sum

    def find_max_subarray(self, A):
        """Linear time, iterative implementation courtesy of Michelle Bodnar, Andrew Lohr in their CLRS solutions:
        https://sites.math.rutgers.edu/~ajl213/CLRS/Ch4.pdf"""

        M = -float('inf')
        low_m, high_m = None, None
        M_r = 0
        low_r = 0

        for i in range(len(A)):
            M_r += A[i]
            if M_r > M:
                low_m = low_r
                high_m = i
                M = M_r

            if M_r < 0:
                M_r = 0
                low_r = i + 1

        return low_m, high_m, M

    def run(self):
        A = copy.deepcopy(self.items)
        return self.find_max_subarray(A)


if __name__ == '__main__':
    A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    A = [-3, -2, -1]
    algo = FindMaxSubArray(items=A)
    print(algo.run())
