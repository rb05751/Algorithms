"""
Problem: Given a string (S) and pattern (P), output whether the pattern matches the full string
"""


class RegExMatch:
    def __init__(self, s, p):
        self.s = s
        self.p = p
        self.M = len(s)
        self.N = len(p)
        self.T = [[False for _ in range(self.N + 1)] for _ in range(self.M + 1)]  # Truth table for matching

    def __init__table(self):
        self.T[0][0] = True  # empty string matches an empty pattern
        for i in range(1, self.N + 1):  # consider the case where we have empty string & non-empty pattern
            if i < self.N:
                if self.p[i] == '*':  # then previous character is repeating
                    continue
                elif self.p[i - 1] == '*':
                    self.T[0][i] = True
                else:
                    break  # just break if we hit a non-repeating character
            else:
                if self.p[i - 1] == '*':
                    self.T[0][i] = True

    def run(self):
        M, N = self.M, self.N
        self.__init__table()
        for i in range(1, M + 1):
            for j in range(1, N + 1):
                # 1. Case 1: if s[i] == p[j]
                if self.s[i - 1] == self.p[j - 1] or self.p[j - 1] == '.':
                    self.T[i][j] = self.T[i - 1][j - 1]
                # 2. Case 2: if p[j] == '*'
                elif self.p[j - 1] == '*':
                    if self.s[i - 1] == self.p[j - 2] or self.p[j - 2] == '.':
                        self.T[i][j] = any([self.T[i - 1][j], self.T[i][j - 2]])
                    else:
                        self.T[i][j] = self.T[i][j - 2]
                else:
                    continue

        return self.T[M][N]


if __name__ == '__main__':
    reg_exp_match = RegExMatch(s='aaa', p='aaaa')
    is_match = reg_exp_match.run()
    print(is_match)
