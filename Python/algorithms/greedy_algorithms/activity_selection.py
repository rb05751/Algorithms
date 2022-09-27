"""
Problem: You are given a set of activities with a start & finishing time interval along with a single lecture hall
        to assign the activities to. Find the largest subset of your full set of activities such that no two activities
        time intervals overlap each other.

Solution: A greedy approach.

    1. Sort the activities in ascending order on finish times.
    2. Assign the first activity to the lecture hall.
    3. Find the next compatible activity with the lowest finishing time. Assign it to the lecture hall.
    4. Recurse #3 on the newly added activity.

Proof:

Claim: Consider a set of activities, and let a[i] be an activity with the earliest finishing time in the set. Then
        a[i] is apart of the optimal/maximum sized subset.

By contradiction:

    - Assume we have found an optimal subset A[k] of size k where a[j] has the earliest finishing time in the set.
    - Add a[i] in front of a[j], call this new set A'[k]
    - Note that since A'[k] is disjoint (since the finishing time of a[i] <= a[j]), then A'[k] is fully compatible.
    - Since |A'[k]| = 1 + |A[k]|, then A'[k] is a larger or more optimal subset of A, contradicting our original
        purported optimality.
"""


class ActivitySelector:
    def __init__(self, activities):
        self.activities = activities
        self.n = len(activities)
        self.max_subset = []
        if self.n != 0:
            self.max_subset = [activities[0]]

    def run(self):
        k = 1
        for i in range(2, self.n):
            if self.activities[i][0] >= self.activities[k][1]:
                self.max_subset.append(self.activities[i])
                k = i

        return self.max_subset


if __name__ == '__main__':
    activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]

    activity_selector = ActivitySelector(activities=activities)
    max_set = activity_selector.run()

    print(max_set)
