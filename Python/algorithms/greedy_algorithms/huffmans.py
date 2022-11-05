from data_structures.d_ary_heap import Heap
import json

if __name__ == '__main__':
    characters = [{45: 'a'}, {13: 'b'}, {12: 'c'}, {16: 'd'}, {9: 'e'}, {5: 'f'}]
    queue = Heap(items=characters, d=2, priority="min")
    queue.build_heap()

    for node in queue.items:
        if len(queue.items) > 1:
            min1 = queue.extract_top()
            min1_freq = list(min1.keys())[0]

            min2 = queue.extract_top()
            min2_freq = list(min2.keys())[0]

            freq = min1_freq + min2_freq
            z = {min1_freq: min1[min1_freq],
                 min2_freq: min2[min2_freq]}

            queue.insert(key=freq, value=z)

    print(json.dumps(queue.items, indent=4))