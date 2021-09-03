"""This algorithm is used to compute the maximum size subarray in Theta(nlogn) time."""

class FindMaxSubArray:
    def __init__(self, items):
        self.items = items
        self.n = len(items)


    def find_max_crossing_subarray(self, A, low, mid, high):
        max_left = None
        left_sum = -10000000000
        sum = 0
        for i in range(mid, low-1, -1):
            sum += A[i]
            if sum > left_sum:
                left_sum = sum
                max_left = i

        """Find right subarray sum"""
        max_right = None
        right_sum = -10000000000
        sum = 0
        for j in range(mid+1, high):
            sum += A[j]
            if sum > right_sum:
                right_sum = sum
                max_right = j

        return max_left, max_right, left_sum + right_sum

    def find_max_subarray(self, A, low, high):
        print(A)
        print(f"This is low: {low} and this is high: {high}")
        if high == low:
            return low, high, A[low]
        else:
            mid = (low+high)//2
            left_low, left_high, left_sum = self.find_max_subarray(A, low, mid)
            right_low, right_high, right_sum = self.find_max_subarray(A, mid+1, high)
            cross_low, cross_high, cross_sum = self.find_max_crossing_subarray(A, low, mid, high)

            if left_sum >= right_sum and left_sum >= cross_sum:
                return left_low, left_high, left_sum
            elif right_sum >= left_sum and right_sum >= cross_sum:
                return right_low, right_high, right_sum
            else:
                return cross_low, cross_high, cross_sum


if __name__ == '__main__':
    num_list = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    algo = FindMaxSubArray(items=num_list)
    print(algo.find_max_subarray(A=algo.items, low=0, high=algo.n-1))