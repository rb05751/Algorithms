"""
Problem: You are given N tasks {a1...aN}, with associated processing times {p1.....pN}.

Goal: Output an optimal ordering of the tasks such that the average sum of completion times is minimized.

Objective Function = sum(c1....cN) / N

where c(i) is the completion time of the task scheduled at the ith position.

Claim/Algo:

We can create an optimal schedule by first sorting the tasks in ascending order of processing times and
processing them in that order.

Proof:

- Assume we had created an optimal schedule (S) that is not in ascending order of processing times.
- This means that for some set of adjacent tasks, a(i) and a(j):
        - i < j
        - p(i) > p(j)
- Then I create another schedule by swapping the positions of a(i) and a(j), call it (S*).
- Since the Avg. completion time for the first half of the array does not change, we can stop focusing on that.
- For the second half of the array, its Avg. completion times increase/decrease by the same amount that the a(i),a(j)
  increase/decrease. So we can stop focusing on that as well, knowing this fact.
- Therefore we only need to analyze the relative increase/decrease in Avg. sum of completion times of a(i) & a(j).
- Note that for 2 tasks the average sum of completion times is:
    1/2 * (p_1 + (p_1 + p_2))
- We can drop the (1/2) since it's a constant.
- So the sum of average completion times for the a(i) --> a(j) ordering is:
    (p_i + (p_i + p_j))
- But if you notice, (p_i + p_j) == (p_j + p_i), so in order to compare the completion times between swapping and not,
  are comparison drops to:

    Not-swapped: p_i
    Swapped: p_j

- Since p_j < p_i, then we have decreased the Avg. sum of completion times across the entire schedule.
"""

if __name__ == '__main__':
    tasks = [{'idx': 1, 'process_time': 3},
             {'idx': 2, 'process_time': 1},
             {'idx': 3, 'process_time': 3},
             {'idx': 4, 'process_time': 6},
             {'idx': 5, 'process_time': 2}]

    # 1. Sort tasks
    sorted_tasks = list(sorted(tasks, key=lambda x: x['process_time']))

    # 2. Compute completion times
    completion_times = [sorted_tasks[0]['process_time']]
    for i, task in enumerate(sorted_tasks):
        c_time = completion_times[-1] + task['process_time']
        completion_times.append(c_time)

    # 3. Compute Average sum of completion times
    avg_sum_comp_times = sum(completion_times) / len(tasks)
    print(sorted_tasks)
    print(f"Avg sum of completion times: {avg_sum_comp_times}")



