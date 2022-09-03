import numpy as np

if __name__ == '__main__':
    # 1. Create examples
    X = ['A', 'B', 'C', 'B', 'D', 'A', 'B']
    Y = ['B', 'D', 'C', 'A', 'B', 'A']

    # 2. Build tables
    length_table = np.zeros(shape=(len(X) + 1, len(Y) + 1))
    seq_table = np.zeros(shape=(len(X), len(Y)))

    # 3. Add sentinels
    X, Y = ['<START>'] + X, ['<START>'] + Y

    # 3. Run algo
    for i in range(1, length_table.shape[0]):
        for j in range(1, length_table.shape[1]):
            if X[i] == Y[j]:
                length_table[i, j] = length_table[i - 1, j - 1] + 1
                seq_table[i-1, j-1] = 3
            elif length_table[i, j - 1] > length_table[i - 1, j]:
                length_table[i, j] = length_table[i, j - 1]
                seq_table[i-1, j-1] = 2
            else:
                length_table[i, j] = length_table[i - 1, j]
                seq_table[i-1, j-1] = 1

    # 4. Print optimal solution
    # Notes: 1 = i-1, 2 = j-1, 3 = [i-1, j-1]

    X, Y = X[1:], Y[1:]
    subsequence = []
    i, j = seq_table.shape[0] - 1, seq_table.shape[1] - 1

    while True:
        if i == -1 or j == -1:
            break
        elif seq_table[i, j] == 1:
            i -= 1
        elif seq_table[i, j] == 2:
            j -= 1
        else:
            subsequence.insert(0, X[i])
            i -= 1
            j -= 1

    print(subsequence)