from minorminer import find_embedding
import dwave_networkx as dnx
import matplotlib.pyplot as plt

S = [('C', 'B'), ('B', 'A'), ('C', 'A'), ('C', 'D'), ('D', 'A')]

ChimeraG = dnx.chimera_graph(1, 1, 4)

mapping = find_embedding(S, ChimeraG.edges)

mapping_inv = {}
for s, chain in mapping.items():
    for c in chain:
        mapping_inv[c] = s


def edge_color(u, v):
    if u in mapping_inv and v in mapping_inv:
        us, vs = mapping_inv[u], mapping_inv[v]
        if (us, vs) in S or (vs, us) in S:
            return 'red'
        elif mapping_inv[u] == mapping_inv[v]:
            return 'blue'
        else:
            return 'black'
    else:
        return 'black'


def node_color(u):
    if u in mapping_inv:
        return 'red'
    else:
        return 'black'


plt.figure(figsize=(3, 3))
G = dnx.chimera_graph(1, 1, 4)
dnx.draw_chimera(G, width=2,
                 edge_color=[edge_color(u, v) for u, v in G.edges],
                 node_color=[node_color(u)for u in G.nodes],
                 labels={u: mapping_inv[u]for u in G.nodes if u in mapping_inv})

plt.show()
