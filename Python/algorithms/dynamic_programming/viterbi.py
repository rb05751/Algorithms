"""
Resources:
- https://www.youtube.com/watch?v=6JVqutwtzmo
- https://en.wikipedia.org/wiki/Viterbi_algorithm
- CLRS Ch.15

Problem (Speech Recognition):
    - Given a directed graph G = (V,E), each edge (u,v) is labeled with a sound sigma(u,v) from a finite set of sounds (S=[sigma1...sigmak]).
    - Each edge also has a non-negative probability p(u,v) of traversing the edge (u,v) from vertex u and producing the
        corresponding sound (sigma(u,v)).
    - Each path in the graph starting from a distinguished vertex v0 corresponds to a possible sequence of sounds produced by the model.
    - We define the label of a directed path to be the concatenation of the labels of the edges on that path.
    - The probability of a path is equal to the product of the probabilities of the path (e.g. Random Walk)
    - GOAL: Find the most probable path that has S as its label.

Optimal Substructure:

OPT(X[1...j]) = min(k) { OPT(X[1...k] + dist(k, j) }

Proof:

CLAIM: The optimal path from X[1...j] is the minimum path k such that The optimal path X[1..k] + dist(k, j) is better than
        all other qualifying paths to j.

- Assume that we constructed an optimal path to j using the method above.
- Imagine that we had another k' such that the path X[1...k'] + dist(k', j) is more optimal that our original with k.
- We could just replace the old one with this one and construct an even more optimal one. Contradicting our purported optimality.
"""




