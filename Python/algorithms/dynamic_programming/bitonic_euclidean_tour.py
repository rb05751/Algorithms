"""
https://metacpan.org/pod/Algorithm::TravelingSalesman::BitonicTour#THE-PROBLEM

"""

import math
import numpy as np


class OptimalBitonicTour:
    def __init__(self, points):
        self.points = points
        self.N = len(points)
        self.tour_matrix = np.full((self.N, self.N), np.inf)
        self.dist_matrix = np.full((self.N, self.N), np.inf)

    @staticmethod
    def __euclidean_distance(p1, p2):
        return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

    def initialize_tables(self):
        # 3a. Calculate distances
        for i in range(self.N):
            for j in range(i, self.N):
                self.dist_matrix[i, j] = self.__euclidean_distance(points[i], points[j])

        # 3b. Tour base cases
        self.tour_matrix[0, 0] = 0
        for i in range(1, self.N):
            self.tour_matrix[0, i] = self.tour_matrix[0, i - 1] + self.dist_matrix[i - 1, i]

    def find_optimal_tour(self):
        for i in range(1, self.N):
            for j in range(i, self.N):
                if i == j:
                    self.tour_matrix[i, j] = self.tour_matrix[i - 1, j] + self.dist_matrix[i - 1, j]
                elif i == j - 1:
                    for k in range(i):
                        tour_cost = self.tour_matrix[k, i] + self.dist_matrix[k, j]
                        if tour_cost < self.tour_matrix[i, j]:
                            self.tour_matrix[i, j] = tour_cost
                else:
                    self.tour_matrix[i, j] = self.tour_matrix[i, j - 1] + self.dist_matrix[j - 1, j]

    def run(self):
        self.initialize_tables()
        self.find_optimal_tour()
        print(f"Length of the shortest bitonic tour is: {self.tour_matrix[self.N - 1, self.N - 1]}")


if __name__ == '__main__':
    # 1. Define input points
    # points = [(1,1), (2,3), (2,2), (5,5), (7,3)]
    points = [(0, 6), (1, 0), (2, 3), (5, 4), (6, 1), (7, 5), (8, 2)]  # Example from CLRS Ch. 15 - Figure 15.11

    bitonic_tour = OptimalBitonicTour(points=points)
    bitonic_tour.run()
