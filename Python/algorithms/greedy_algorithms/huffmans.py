from data_structures.d_ary_heap import Heap
import json


class Huffman:
    def __init__(self, characters):
        self.characters = characters
        self.queue = None

    def __init__queue(self):
        self.queue = Heap(items=characters, d=2, priority="min")
        self.queue.build_heap()

    def compute(self):
        self.__init__queue()
        for _ in self.queue.items:
            if len(self.queue.items) > 1:
                min1 = self.queue.extract_top()
                min1_freq = list(min1.keys())[0]

                min2 = self.queue.extract_top()
                min2_freq = list(min2.keys())[0]

                freq = min1_freq + min2_freq
                z = {min1_freq: min1[min1_freq],
                     min2_freq: min2[min2_freq]}

                self.queue.insert(key=freq, value=z)

        return self.queue.items


if __name__ == '__main__':
    characters = [{45: 'a'}, {13: 'b'}, {12: 'c'}, {16: 'd'}, {9: 'e'}, {5: 'f'}]
    huffman = Huffman(characters=characters)
    items = huffman.compute()
    print(json.dumps(items, indent=4))
