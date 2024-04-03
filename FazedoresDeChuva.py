import networkx as nx
import matplotlib.pyplot as plt
import itertools

verticies = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'w', 'y', 'z'] 

G = nx.Graph()

for letra in verticies:
    if letra == 'f':
        break
    G.add_node(letra)


G.add_weighted_edges_from([('a', 'b', 2), ('a', 'c', 3), ('a', 'e', 4), ('b', 'c', 2), ('b', 'd', 5), ('b', 'e', 7), ('d', 'e', 3)])

# Definir o vértice inicial
start_vertex = input('De que verticie você deseja começar? ')

# Encontrar o caminho mais curto passando por todos os vértices
shortest_path = None
shortest_path_length = float('inf')

# Gerar permutações começando do vértice inicial
for permutation in itertools.permutations(G.nodes()):
    if permutation[0] == start_vertex:
        total_length = 0
        for i in range(len(permutation) - 1):
            # Verifica se a aresta existe no grafo
            if G.has_edge(permutation[i], permutation[i+1]):
                total_length += G[permutation[i]][permutation[i+1]]['weight']
            else:
                break  # Interrompe a iteração se encontrar uma sequência inválida de vértices
        else:  # Este bloco é executado se o loop interno terminar sem um break
            # Verifica a aresta entre o último e o primeiro vértice (volta ao começo)
            if G.has_edge(permutation[-1], permutation[0]):
                total_length += G[permutation[-1]][permutation[0]]['weight']
                # Atualiza o menor caminho encontrado até agora
                if total_length < shortest_path_length:
                    shortest_path_length = total_length
                    shortest_path = permutation

print("Caminho mais curto passando por todos os vértices começando de", start_vertex, ":", shortest_path)
print("Comprimento do caminho mais curto:", shortest_path_length)

# nx.draw(G, pos=nx.spring_layout(G), with_labels=True)
# plt.show()