import networkx as nx
import itertools
import Levenshtein

def get_closest_node(city_name, node_list):
    closest_node = None
    min_distance = float('inf')
    for node in node_list:
        distance = Levenshtein.distance(city_name.lower(), node.lower())
        if distance < min_distance:
            min_distance = distance
            closest_node = node
    return closest_node

cidades = ['Afonso Cláudio', 'Água Doce do Norte', 'Águia Branca', 'Alegre', 'Alfredo Chaves', 'Alto Rio Novo', 'Anchieta', 'Apiacá', 'Aracruz', 'Atílio Vivácqua', 'Baixo Guandu', 
           'Barra de São Francisco', 'Boa Esperança', 'Bom Jesus do Norte', 'Brejetuba', 'Cachoeiro de Itapemirim', 'Cariacica', 'Castelo', 'Colatina', 'Conceição da Barra', 'Conceição do Castelo', 
           'Divino de São Lourenço', 'Domingos Martins', 'Dores do Rio Preto', 'Ecoporanga', 'Fundão', 'Governador Lindenberg', 'Guaçuí', 'Guarapari', 'Ibatiba', 'Ibiraçu', 'Ibitirama', 
           'Iconha', 'Irupi', 'Itaguaçu', 'Itapemirim', 'Itarana', 'Iúna', 'Jaguaré', 'Jerônimo Monteiro', 'João Neiva', 'Laranja da Terra', 'Linhares', 'Mantenópolis', 'Marataízes',
           'Marechal Floriano', 'Marilândia', 'Mimoso do Sul', 'Montanha', 'Mucurici', 'Muniz Freire', 'Muqui', 'Nova Venécia', 'Pancas', 'Pedro Canário', 'Pinheiros', 'Piúma', 'Ponto Belo',
           'Presidente Kennedy', 'Rio Bananal', 'Rio Novo do Sul', 'Santa Leopoldina', 'Santa Maria de Jetibá', 'Santa Teresa', 'São Domingos do Norte', 'São Gabriel da Palha', 'São José do Calçado',
           'São Mateus', 'São Roque do Canaã', 'Serra', 'Sooretama', 'Vargem Alta', 'Venda Nova do Imigrante', 'Viana', 'Vila Pavão', 'Vila Valério', 'Vila Velha', 'Vitória']

G = nx.Graph() 
G.add_nodes_from(cidades)

G.add_weighted_edges_from([
    (cidades[0], cidades[14], 38),
    (cidades[0], cidades[20], 46),
    (cidades[0], cidades[22], 99),
    (cidades[0], cidades[36], 46),
    (cidades[0], cidades[41], 34),
    (cidades[0], cidades[62], 83),
    (cidades[0], cidades[72], 53),
    (cidades[1], cidades[11], 33),
    (cidades[1], cidades[24], 37),
    (cidades[2], cidades[11], 42),
    (cidades[2], cidades[43], 55),
    (cidades[2], cidades[52], 70),
    (cidades[2], cidades[53], 52),
    (cidades[2], cidades[64], 28),
    (cidades[2], cidades[65], 44),
    (cidades[3], cidades[15], 62),
    (cidades[3], cidades[39], 20),
    (cidades[3], cidades[50], 47),
    (cidades[3], cidades[47], 59),
    (cidades[3], cidades[27], 23),
    (cidades[3], cidades[31], 44),
    (cidades[3], cidades[66], 40),
    (cidades[3], cidades[17], 65),
    (cidades[4], cidades[45], 47),
    (cidades[4], cidades[22], 53),
    (cidades[4], cidades[32], 32),
    (cidades[4], cidades[60], 50),
    (cidades[4], cidades[6], 33),
    (cidades[4], cidades[28], 47),
    (cidades[4], cidades[71], 43),
    (cidades[5], cidades[53], 35),
    (cidades[5], cidades[43], 34),
    (cidades[6], cidades[28], 26),
    (cidades[6], cidades[56], 11),
    (cidades[6], cidades[32], 25),
    (cidades[7], cidades[47], 43),
    (cidades[7], cidades[13], 13),
    (cidades[7], cidades[66], 27),
    (cidades[8], cidades[42], 60),
    (cidades[8], cidades[25], 30),
    (cidades[8], cidades[30], 13),
    (cidades[8], cidades[40], 23),
    (cidades[9], cidades[15], 20),
    (cidades[9], cidades[35], 66),
    (cidades[9], cidades[58], 40),
    (cidades[9], cidades[51], 23),
    (cidades[9], cidades[47], 49),
    (cidades[10], cidades[53], 60),
    (cidades[10], cidades[18], 50),
    (cidades[10], cidades[34], 53),
    (cidades[10], cidades[41], 87),
    (cidades[11], cidades[24], 58),
    (cidades[11], cidades[43], 41),
    (cidades[11], cidades[52], 80),
    (cidades[11], cidades[74], 47),
    (cidades[12], cidades[55], 18),
    (cidades[12], cidades[57], 84),
    (cidades[12], cidades[52], 28),
    (cidades[12], cidades[67], 60),
    (cidades[13], cidades[66], 13),
    (cidades[14], cidades[29], 39),
    (cidades[14], cidades[50], 50),
    (cidades[14], cidades[20], 36),
    (cidades[15], cidades[17], 38),
    (cidades[15], cidades[71], 31),
    (cidades[15], cidades[35], 44),
    (cidades[15], cidades[51], 35),
    (cidades[15], cidades[39], 42),
    (cidades[16], cidades[22], 47),
    (cidades[16], cidades[61], 30),
    (cidades[16], cidades[76], 38),
    (cidades[16], cidades[73], 15),
    (cidades[16], cidades[77], 15),
    (cidades[16], cidades[69], 29),
    (cidades[17], cidades[20], 37),
    (cidades[17], cidades[72], 39),
    (cidades[17], cidades[22], 99),
    (cidades[17], cidades[71], 37),
    (cidades[17], cidades[50], 36),
    (cidades[18], cidades[53], 59),
    (cidades[18], cidades[68], 29),
    (cidades[18], cidades[34], 58),
    (cidades[18], cidades[46], 27),
    (cidades[18], cidades[42], 73),
    (cidades[18], cidades[40], 55),
    (cidades[18], cidades[26], 74),
    (cidades[18], cidades[64], 59),
    (cidades[19], cidades[54], 52),
    (cidades[19], cidades[67], 38),
    (cidades[19], cidades[55], 70),
    (cidades[20], cidades[72], 18),
    (cidades[20], cidades[50], 39),
    (cidades[21], cidades[31], 15),
    (cidades[21], cidades[27], 24),
    (cidades[21], cidades[23], 31),
    (cidades[22], cidades[62], 60),
    (cidades[22], cidades[61], 83),
    (cidades[22], cidades[73], 33),
    (cidades[22], cidades[45], 10),
    (cidades[22], cidades[71], 101),
    (cidades[22], cidades[72], 68),
    (cidades[23], cidades[27], 33),
    (cidades[23], cidades[31], 39),
    (cidades[24], cidades[74], 65),
    (cidades[24], cidades[52], 81),
    (cidades[24], cidades[49], 68),
    (cidades[24], cidades[57], 64),
    (cidades[25], cidades[69], 28),
    (cidades[25], cidades[61], 30),
    (cidades[25], cidades[63], 28),
    (cidades[25], cidades[30], 16),
    (cidades[26], cidades[64], 38),
    (cidades[26], cidades[42], 64),
    (cidades[26], cidades[59], 19),
    (cidades[26], cidades[46], 49),
    (cidades[27], cidades[66], 39),
    (cidades[27], cidades[31], 44),
    (cidades[28], cidades[76], 51),
    (cidades[28], cidades[73], 42),
    (cidades[28], cidades[45], 69),
    (cidades[29], cidades[33], 30),
    (cidades[29], cidades[37], 23),
    (cidades[29], cidades[50], 52),
    (cidades[30], cidades[40], 10),
    (cidades[30], cidades[63], 44),
    (cidades[31], cidades[37], 38),
    (cidades[31], cidades[50], 47),
    (cidades[32], cidades[56], 17),
    (cidades[32], cidades[60], 18),
    (cidades[33], cidades[37], 15),
    (cidades[34], cidades[36], 10),
    (cidades[34], cidades[63], 52),
    (cidades[34], cidades[68], 35),
    (cidades[34], cidades[41], 32),
    (cidades[35], cidades[44], 17),
    (cidades[35], cidades[56], 12),
    (cidades[35], cidades[60], 21),
    (cidades[35], cidades[71], 69),
    (cidades[35], cidades[58], 59),
    (cidades[36], cidades[63], 42),
    (cidades[36], cidades[62], 32),
    (cidades[36], cidades[41], 39),
    (cidades[37], cidades[50], 25),
    (cidades[38], cidades[67], 40),
    (cidades[38], cidades[75], 208),
    (cidades[38], cidades[70], 44),
    (cidades[38], cidades[42], 68),
    (cidades[39], cidades[47], 39),
    (cidades[39], cidades[51], 22),
    (cidades[40], cidades[42], 56),
    (cidades[40], cidades[63], 53),
    (cidades[40], cidades[68], 67),
    (cidades[42], cidades[67], 83),
    (cidades[42], cidades[70], 25),
    (cidades[42], cidades[59], 46),
    (cidades[42], cidades[46], 71),
    (cidades[43], cidades[53], 68),
    (cidades[44], cidades[58], 42),
    (cidades[45], cidades[73], 36),
    (cidades[47], cidades[51], 17),
    (cidades[47], cidades[58], 62),
    (cidades[47], cidades[66], 71),
    (cidades[48], cidades[55], 44),
    (cidades[48], cidades[54], 64),
    (cidades[48], cidades[57], 22),
    (cidades[48], cidades[49], 18),
    (cidades[49], cidades[57], 4),
    (cidades[52], cidades[65], 44),
    (cidades[52], cidades[67], 67),
    (cidades[52], cidades[57], 112),
    (cidades[52], cidades[74], 32),
    (cidades[53], cidades[64], 48),
    (cidades[54], cidades[55], 35),
    (cidades[55], cidades[67], 71),
    (cidades[55], cidades[57], 67),
    (cidades[56], cidades[60], 36),
    (cidades[59], cidades[70], 69),
    (cidades[59], cidades[75], 39),
    (cidades[59], cidades[64], 57),
    (cidades[60], cidades[71], 48),
    (cidades[61], cidades[69], 50),
    (cidades[61], cidades[63], 29),
    (cidades[61], cidades[62], 34),
    (cidades[62], cidades[63], 27),
    (cidades[63], cidades[68], 32),
    (cidades[64], cidades[65], 21),
    (cidades[64], cidades[75], 48),
    (cidades[65], cidades[67], 110),
    (cidades[65], cidades[75], 27),
    (cidades[67], cidades[75], 100),
    (cidades[69], cidades[77], 30),
    (cidades[70], cidades[75], 55),
    (cidades[73], cidades[76], 22),
    (cidades[76], cidades[77], 13),
    ])

i = 1
for cidade in cidades:
    print(f'{i} - {cidade}')
    i += 1

start_vertex = cidades[int(input('Digite o número referente a cidade que deseja iniciar: ')) - 1]

# Implementação da busca gulosa
current_vertex = start_vertex
visited = set([start_vertex])
total_length = 0
shortest_path = [start_vertex]

while len(visited) < len(cidades):
    min_distance = float('inf')
    closest_vertex = None
    for neighbor in G.neighbors(current_vertex):
        if neighbor not in visited:
            distance = G[current_vertex][neighbor]['weight']
            if distance < min_distance:
                min_distance = distance
                closest_vertex = neighbor
    if closest_vertex is not None:
       total_length += G[current_vertex][closest_vertex]['weight']
       shortest_path.append(closest_vertex)
       visited.add(closest_vertex)
       current_vertex = closest_vertex

# Adiciona o último vértice para fechar o ciclo
if current_vertex is not None:
    # Usar os índices dos vértices em vez dos nomes das cidades para acessar a aresta
    total_length += G[current_vertex][closest_vertex]['weight']
    shortest_path.append(start_vertex)

print("Caminho mais curto passando por todos os vértices começando de", start_vertex, ":", shortest_path)
print("Comprimento do caminho mais curto:", total_length)