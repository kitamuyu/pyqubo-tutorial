import dwave
import dimod
import numpy as np

chains1 = [(0, 1, 2), (3, 4)]
samples1 = np.array([[1, 1, 0, 0, 0],
                     [1, 1, 1, 0, 0],
                     [1, 1, 1, 0, 1],
                     [1, 1, 1, 1, 1],
                     ], dtype=np.int8)

# ? unembedded, idx = dwave.embedding.chain_breaks.discard(samples, chains)
# ? unembedded, idx = dwave.embedding.chain_breaks.majority_vote(samples, chains)
# ? unembedded, idx = dwave.embedding.chain_breaks.weighted_random(samples, chains)
# print(idx)
# print(unembedded)

h = {'a': 0, 'b': 0, 'c': 0}
J = {('a', 'b'): 1, ('b', 'c'): 1, ('a', 'c'): 1}
bqm = dimod.BinaryQuadraticModel.from_ising(h, J)
embedding = {'a': [0], 'b': [1], 'c': [2, 3]}
# ? cbm = dwave.embedding.chain_breaks.MinimizeEnergy(bqm, embedding)
samples2 = np.array([[+1, -1, +1, +1],
                     [-1, -1, -1, -1],
                     [-1, -1, +1, -1],
                     [+1, +1, -1, +1]],
                    dtype=np.int8)
chains2 = [embedding['a'], embedding['b'], embedding['c']]
# unembedded, idx = cbm(samples2, chains2)
# print(unembedded)
