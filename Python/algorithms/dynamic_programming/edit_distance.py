import numpy as np


class EditDistance:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        self.M = len(X)
        self.N = len(Y)
        self.EDIT = np.zeros((self.M + 1, self.N + 1))

    def init_table(self):
        for i in range(1, self.N + 1):
            self.EDIT[0, i] = self.EDIT[0, i - 1] + 1

        for j in range(1, self.M + 1):
            self.EDIT[j, 0] = self.EDIT[j - 1, 0] + 1

    def find_edit_distance(self):
        for i in range(1, self.M + 1):
            for j in range(1, self.N + 1):
                if self.X[i - 1] == self.Y[j - 1]:
                    self.EDIT[i, j] = self.EDIT[i - 1, j - 1] + 0  # COPY has not cost
                else:
                    replace_cost = self.EDIT[i - 1, j - 1] + 1  # REPLACE
                    insert_cost = self.EDIT[i, j - 1] + 1  # INSERT
                    delete_cost = self.EDIT[i - 1, j] + 1  # DELETE
                    self.EDIT[i, j] = min([replace_cost, insert_cost, delete_cost])

        return self.EDIT[self.M, self.N]

    def compute(self):
        self.init_table()
        num_edits = self.find_edit_distance()
        return num_edits


if __name__ == '__main__':
    X = 'INTENTION'
    Y = 'EXECUTION'
    edit_distance = EditDistance(X, Y)
    result = edit_distance.compute()

    print("\n")
    print("-------------------------")
    print(f"Edit Distance: {result}")
    print("------------------------")
    print(edit_distance.EDIT)
