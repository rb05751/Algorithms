import random
import sys

def RandSearch(arr, x, checked):
    if len(checked) == len(arr):
        print(checked)
        return False
    else:
        i = random.randint(0, len(arr)-1)
        if arr[i] == x:
            print(arr[i])
            return True
        else:
            if arr[i] not in checked:
                checked.append(arr[i])
            return RandSearch(arr, x, checked)

if __name__ == '__main__':
    sys.setrecursionlimit(10**5)
    value = 7
    items = [3,2,1,5,6,9,8]
    print(RandSearch(arr=items, x=value, checked=[]))
