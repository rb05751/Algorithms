"""
Problem Statement: Given the following inputs

S = {a1...aN} of N unit-time tasks (time to complete = 1)
D = {d1...dN} of N deadlines for each task between 1 - N
W = {w1...wN} of N penalties/weights for each task between 1 - N

Find a schedule for S that minimizes the total penalty incurred for missed deadlines.

Solution:
    - Since S can be represented as a Matroid, it can be solved using a Greedy algorithm
    - The greedy algorithm finds the maximum weight independent set of tasks in S, where a set of tasks
      are independent if they are all "early" or meet the deadline. The remaining tasks not selected to be
      in the independent set are considered "late" and we incur a penalty on them.
    - The following implementation is of the greedy algorithm that solves this problem.
"""

import copy
import json


class UnitTaskScheduler:
    def __init__(self, tasks):
        self.tasks = tasks

    @staticmethod
    def check_independence(A, x) -> bool:
        local_A = copy.deepcopy(A)

        local_A.append(x)

        max_deadline = max(list(map(lambda x: x['d'], local_A)))  # O(N)

        num_each_deadline = [0] * (max_deadline + 1)  # O(max(d))

        for i, a in enumerate(local_A):  # O(N)
            a_deadline = a['d']
            num_each_deadline[a_deadline] += 1

        for i in range(1, len(num_each_deadline)):
            num_each_deadline[i] += num_each_deadline[i - 1]
            if num_each_deadline[i] > i:
                return False

        return True

    def find_optimal_schedule(self) -> list[dict]:
        # 1. Sort in descending order of weight
        tasks = list(sorted(self.tasks, key=lambda x: x['w'], reverse=True))

        # 2. Run Greedy
        Late = []
        A = []
        A_length = 0
        for task in tasks:
            if A_length == 0:
                A.append(task)
                A_length += 1
            else:
                is_independent = self.check_independence(A, x=task)
                if is_independent:
                    A.append(task)
                else:
                    Late.append(task)

        # 3. Sort A in monotonically increasing deadlines
        A.sort(key=lambda x: x['d'])
        A.extend(Late)

        return A


if __name__ == '__main__':
    tasks = [{'a': 1, 'd': 4, 'w': 70}, {'a': 2, 'd': 2, 'w': 60}, {'a': 3, 'd': 4, 'w': 50},
             {'a': 4, 'd': 3, 'w': 40}, {'a': 5, 'd': 1, 'w': 30}, {'a': 6, 'd': 4, 'w': 20},
             {'a': 7, 'd': 6, 'w': 10}]

    task_scheduler = UnitTaskScheduler(tasks=tasks)

    optimal_schedule = task_scheduler.find_optimal_schedule()

    print(json.dumps(optimal_schedule, indent=4))
