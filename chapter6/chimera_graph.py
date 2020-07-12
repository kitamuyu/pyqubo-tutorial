import networkx as nx
import dwave_networkx as dnx
import matplotlib.pyplot as plt

G = dnx.chimera_graph(3, 2, 4)

plt.figure(figsize=(5, 5))
dnx.draw_chimera(G, width=1)
plt.show()
