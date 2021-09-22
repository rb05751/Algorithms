import random


class RandomSearch:
    def __init__(self, a, b):
        self.items = list(range(a, b + 1))

    def __floor_or_ceil(self):
        return random.randint(0, 1)

    def __choose_side(self):
        return random.randint(0, 1)

    def run(self, arr):
        if len(arr) == 1:
            return arr[0]
        elif len(arr) == 2:
            return arr[self.__choose_side()]
        else:
            side, fc = self.__choose_side(), self.__floor_or_ceil()
            n = len(arr)
            if not fc:
                if not side:
                    return self.run(arr[:n // 2])
                else:
                    return self.run(arr[n // 2:])
            else:
                if not side:
                    return self.run(arr[:n // 2 + 1])
                else:
                    return self.run(arr[n // 2 + 1:])


if __name__ == '__main__':
    """Algorithm has a slight bias towards the edge values (1 and 5) in this case"""
    freq_dict = {
        '1': 0,
        '2': 0,
        '3': 0,
        '4': 0,
        '5': 0
    }
    random_search = RandomSearch(a=1, b=5)
    for i in range(100000):
        value = random_search.run(random_search.items)
        freq_dict[str(value)] += 1
