import random
import sys
from sorting import bubble_sort, heap_sort, insertion_sort, merge_sort, quick_sort, selection_sort
import time

if __name__ == '__main__':
    num_list = [5, 2, 4, 6, 1, 3, 3, 8, 9, 11, 7, 0, 1, 4, 10, 12]
    num_list = list(range(0, 10000))
    random.shuffle(num_list)
    quick_sorter = quick_sort.QuickSort(items=num_list, is_random=False)
    merge_sorter = merge_sort.MergeSort(items=num_list)
    insertion_sorter = insertion_sort.InsertionSort(items=num_list, ascending=True)
    heap_sorter = heap_sort.HeapSort(items=num_list)
    bubble_sorter = bubble_sort.BubbleSort(items=num_list)
    select_sorter = selection_sort.SelectionSort(items=num_list)
    if quick_sorter.check(A=num_list):
        """Test"""

        """QuickSort"""
        start = time.time()
        q_result = quick_sorter.sort(A=num_list)
        print(f"QuickSort: {q_result}...")
        print(f"Time: {time.time() - start} seconds")

        """MergeSort"""
        start = time.time()
        m_result = merge_sorter.run()
        print(f"MergeSort: {m_result}...")
        print(f"Time: {time.time() - start} seconds")

        """Insertion Sort"""
        start = time.time()
        i_result = insertion_sorter.sort()
        print(f"InsertionSort: {i_result}...")
        print(f"Time: {time.time() - start} seconds")

        """Heap Sort"""
        start = time.time()
        h_result = heap_sorter.sort()
        print(f"Heap Sort: {h_result}...")
        print(f"Time: {time.time() - start} seconds")

        """Bubble Sort"""
        start = time.time()
        b_result = bubble_sorter.run()
        print(f"Bubble Sort: {b_result}...")
        print(f"Time: {time.time() - start} seconds")

        """Selection Sort"""
        start = time.time()
        s_result = select_sorter.sort()
        print(f"Selection Sort: {s_result}...")
        print(f"Time: {time.time() - start} seconds")

    else:
        print(num_list)
