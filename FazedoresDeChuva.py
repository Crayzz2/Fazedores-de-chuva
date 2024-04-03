import networkx as nx
import matplotlib.pyplot as plt
import itertools

cidades = ['Afonso Cláudio', 'Água Doce do Norte', 'Águia Branca', 'Alegre', 'Alfredo Chaves', 'Alto Rio Novo', 'Anchieta', 'Apiacá', 'Aracruz', 'Atílio Vivácqua', 'Baixo Guandu', 
           'Barra de São Francisco', 'Boa Esperança', 'Bom Jesus do Norte', 'Brejetuba', 'Cachoeiro de Itapemirim', 'Cariacica', 'Castelo', 'Colatina', 'Conceição da Barra', 'Conceição do Castelo', 
           'Divino de São Lourenço', 'Domingos Martins', 'Dores do Rio Preto', 'Ecoporanga', 'Fundão', 'Governador Lindenberg', 'Guaçuí', 'Guarapari', 'Ibatiba', 'Ibiraçu', 'Ibitirama', 
           'Iconha', 'Irupi', 'Itaguaçu', 'Itapemirim', 'Itarana', 'Iúna', 'Jaguaré', 'Jerônimo Monteiro', 'João Neiva', 'Laranja da Terra', 'Linhares', 'Mantenópolis', 'Marataízes',
           'Marechal Floriano', 'Marilândia', 'Mimoso do Sul', 'Montanha', 'Mucurici', 'Muniz Freire', 'Muqui', 'Nova Venécia', 'Pancas', 'Pedro Canário', 'Pinheiros', 'Piúma', 'Ponto Belo',
           'Presidente Kennedy', 'Rio Bananal', 'Rio Novo do Sul', 'Santa Leopoldina', 'Santa Maria de Jetibá', 'Santa Teresa', 'São Domingos do Norte', 'São Gabriel da Palha', 'São José do Calçado',
           'São Mateus', 'São Roque do Canaã', 'Serra', 'Sooretama', 'Vargem Alta', 'Venda Nova do Imigrante', 'Viana', 'Vila Pavão', 'Vila Valério', 'Vila Velha', 'Vitória']

G = nx.Graph() 

for letra in cidades:
    G.add_node(letra)


G.add_weighted_edges_from([('Afonso Cláudio', 'Água Doce do Norte', 2), ('Água Doce do Norte', 'Águia Branca', 3), (cidades[2], cidades[0], 5)])

i = 1
for cidade in cidades:
    print(f'{i} - {cidade}')
    i+=1


# Definir o vértice inicial
start_vertex = cidades[int(input('Digite o número referente a cidade que deseja iniciar: '))-1]

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