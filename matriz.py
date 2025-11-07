def criar_grafo():
    """
    Cria e retorna uma matriz de adjacência vazia e uma lista de vértices.

    Passos:
    1. Criar uma lista vazia chamada matriz (para armazenar as conexões).
    2. Criar uma lista vazia chamada vertices (para armazenar os nomes dos vértices).
    3. Retornar (matriz, vertices).
    """
    matriz = []
    vertices = []
    return matriz, vertices


def inserir_vertice(matriz, vertices, vertice):
    """
    Adiciona um novo vértice ao grafo.

    Passos:
    1. Verificar se o vértice já existe em 'vertices'.
    2. Caso não exista:
          - Adicionar o vértice à lista 'vertices'.
          - Aumentar o tamanho da matriz:
                a) Para cada linha existente, adicionar um valor 0 no final (nova coluna).
                b) Adicionar uma nova linha com zeros do tamanho atualizado.
    """
    if vertice in vertices:
        return False

    vertices.append(vertice)
    n = len(vertices)

    for linha in matriz:
        linha.append(0)
    
    nova_linha = [0] * n
    matriz.append(nova_linha)
    
    return True


def inserir_aresta(matriz, vertices, origem, destino, nao_direcionado=False):
    """
    Adiciona uma aresta entre dois vértices.

    Passos:
    1. Garantir que 'origem' e 'destino' existam em 'vertices':
          - Se não existirem, chamar 'inserir_vertice' para adicioná-los.
    2. Localizar o índice da origem (i) e do destino (j).
    3. Marcar a conexão na matriz: matriz[i][j] = 1.
    4. Se nao_direcionado=True, também marcar a conexão inversa matriz[j][i] = 1.
    """
    inserir_vertice(matriz, vertices, origem)
    inserir_vertice(matriz, vertices, destino)

    i = vertices.index(origem)
    j = vertices.index(destino)

    matriz[i][j] = 1
    
    if nao_direcionado:
        matriz[j][i] = 1


def remover_vertice(matriz, vertices, vertice):
    """
    Remove um vértice e todas as arestas associadas.

    Passos:
    1. Verificar se o vértice existe em 'vertices'.
    2. Caso exista:
          - Descobrir o índice correspondente (usando vertices.index(vertice)).
          - Remover a linha da matriz na posição desse índice.
          - Remover a coluna (mesmo índice) de todas as outras linhas.
          - Remover o vértice da lista 'vertices'.
    """
    if vertice not in vertices:
        print(f"Erro: Vértice '{vertice}' não encontrado.")
        return False

    idx = vertices.index(vertice)

    matriz.pop(idx)

    for linha in matriz:
        linha.pop(idx)
        
    vertices.pop(idx)
    
    print(f"Vértice '{vertice}' removido com sucesso.")
    return True


def remover_aresta(matriz, vertices, origem, destino, nao_direcionado=False):
    """
    Remove uma aresta entre dois vértices.

    Passos:
    1. Verificar se ambos os vértices existem.
    2. Localizar os índices (i e j).
    3. Remover a aresta: matriz[i][j] = 0.
    4. Se nao_direcionado=True, também remover a inversa: matriz[j][i] = 0.
    """
    if origem not in vertices or destino not in vertices:
        print("Erro: Vértice de origem ou destino não encontrado.")
        return

    i = vertices.index(origem)
    j = vertices.index(destino)

    matriz[i][j] = 0
    
    if nao_direcionado:
        matriz[j][i] = 0
    
    print(f"Aresta entre '{origem}' e '{destino}' removida.")


def existe_aresta(matriz, vertices, origem, destino):
    """
    Verifica se existe uma aresta direta entre dois vértices.

    Passos:
    1. Verificar se ambos os vértices existem em 'vertices'.
    2. Obter os índices (i, j).
    3. Retornar True se matriz[i][j] == 1, caso contrário False.
    """
    if origem not in vertices or destino not in vertices:
        return False
        
    i = vertices.index(origem)
    j = vertices.index(destino)

    return matriz[i][j] == 1


def vizinhos(matriz, vertices, vertice):
    """
    Retorna a lista de vizinhos (vértices alcançáveis a partir de 'vertice').

    Passos:
    1. Verificar se 'vertice' existe em 'vertices'.
    2. Obter o índice 'i' correspondente.
    3. Criar uma lista de vizinhos vazia
    4. Para cada item da linha matriz[i], verificar se == 1
          - Adicionar o vértice correspondente na lista de vizinhos
    5. Retornar essa lista.
    """
    lista_vizinhos = []
    
    if vertice not in vertices:
        return lista_vizinhos

    i = vertices.index(vertice)
    
    for j, conexao in enumerate(matriz[i]):
        if conexao == 1:
            lista_vizinhos.append(vertices[j])
          
    return lista_vizinhos


def grau_vertices(matriz, vertices, nao_direcionado=False):
    """
    Calcula o grau de entrada, saída e total de cada vértice.

    Passos:
    1. Criar um dicionário vazio 'graus'.
    2. Para cada vértice i:
          - Se o grafo for direcionado:
                - Grau de saída: somar os valores da linha i.
                - Grau de entrada: somar os valores da coluna i.
                - Grau total = entrada + saída.
          - Se não:
                - calcular apenas o grau de saida ou entrada
    3. Armazenar no dicionário no formato:
          graus[vértice] = {"saida": x, "entrada": y, "total": z} ou graus[vértice] = x.
    4. Retornar 'graus'.
    """
    graus = {}
    n = len(vertices)

    for i in range(n):
        nome_vertice = vertices[i]
        
        if nao_direcionado:
            grau = sum(matriz[i])
            graus[nome_vertice] = grau
        else:
            grau_saida = sum(matriz[i])
            
            grau_entrada = 0
            for k in range(n):
                grau_entrada += matriz[k][i]
                
            graus[nome_vertice] = {
                "saida": grau_saida,
                "entrada": grau_entrada,
                "total": grau_saida + grau_entrada
            }
            
    return graus


def percurso_valido(matriz, vertices, caminho):
    """
    Verifica se um percurso (sequência de vértices) é possível no grafo.

    Passos:
    1. Percorrer a lista 'caminho' de forma sequencial (de 0 até len-2).
    2. Para cada par consecutivo (u, v):
          - Verificar se existe_aresta(matriz, vertices, u, v) é True.
          - Se alguma não existir, retornar False.
    3. Se todas existirem, retornar True.
    """
    if len(caminho) < 2:
        return True

    for i in range(len(caminho) - 1):
        u = caminho[i]
        v = caminho[i+1]
        
        if not existe_aresta(matriz, vertices, u, v):
            return False
            
    return True


def listar_vizinhos(matriz, vertices, vertice):
    """
    Exibe (ou retorna) os vizinhos de um vértice.

    Passos:
    1. Verificar se o vértice existe.
    2. Chamar a função vizinhos() para obter a lista.
    3. Exibir a lista formatada (ex: print(f"Vizinhos de {v}: {lista}")).
    """
    if vertice not in vertices:
        print(f"Vértice '{vertice}' não encontrado no grafo.")
        return

    lista_v = vizinhos(matriz, vertices, vertice)
    
    if not lista_v:
        print(f"Vértice '{vertice}' não possui vizinhos.")
    else:
        print(f"Vizinhos de '{vertice}': {', '.join(map(str, lista_v))}")


def exibir_grafo(matriz, vertices):
    """
    Exibe o grafo em formato de matriz de adjacência.

    Passos:
    1. Exibir cabeçalho com o nome dos vértices.
    2. Para cada linha i:
          - Mostrar o nome do vértice.
          - Mostrar os valores da linha (0 ou 1) separados por espaço.
    """
    if not vertices:
        print("O grafo está vazio.")
        return

    n = len(vertices)
    
    print("     ", end="")
    for v in vertices:
        print(f"{v:<3}", end="")
    print("\n" + "-" * (5 + n * 3))

    for i in range(n):
        print(f"{vertices[i]:<3} |", end=" ")
        
        for j in range(n):
            print(f"{matriz[i][j]:<3}", end="")
        print()


def main():
    """
    Menu interativo para manipular o grafo (matriz de adjacência).
    """
    matriz, vertices = criar_grafo()
    
    tipo_input = input("O grafo será Não-Direcionado? (s/n): ").strip().lower()
    NAO_DIRECIONADO = (tipo_input == 's')
    
    if NAO_DIRECIONADO:
        print("\n--- Grafo Não-Direcionado (Matriz) Criado ---")
    else:
        print("\n--- Grafo Direcionado (Matriz) Criado ---")

    while True:
        print("\n--- Menu de Opções (Matriz de Adjacência) ---")
        print(" 1. Exibir Grafo (Matriz)")
        print(" 2. Inserir Vértice")
        print(" 3. Inserir Aresta")
        print(" 4. Remover Vértice")
        print(" 5. Remover Aresta")
        print(" 6. Listar Vizinhos de um Vértice")
        print(" 7. Verificar existência de Aresta")
        print(" 8. Exibir Graus dos Vértices")
        print(" 9. Verificar Percurso Válido")
        print(" 0. Sair")
        
        escolha = input("Escolha uma opção: ").strip()

        if escolha == '1':
            print("\n--- Grafo Atual (Matriz de Adjacência) ---")
            exibir_grafo(matriz, vertices)

        elif escolha == '2':
            v = input("Nome do vértice a inserir: ")
            if inserir_vertice(matriz, vertices, v):
                print(f"Vértice '{v}' inserido.")
            else:
                print(f"Vértice '{v}' já existe.")

        elif escolha == '3':
            o = input("Vértice de origem: ")
            d = input("Vértice de destino: ")
            inserir_aresta(matriz, vertices, o, d, nao_direcionado=NAO_DIRECIONADO)
            if NAO_DIRECIONADO:
                 print(f"Aresta {o} <-> {d} inserida.")
            else:
                 print(f"Aresta {o} -> {d} inserida.")

        elif escolha == '4':
            v = input("Nome do vértice a remover: ")
            remover_vertice(matriz, vertices, v)

        elif escolha == '5':
            o = input("Vértice de origem da aresta: ")
            d = input("Vértice de destino da aresta: ")
            remover_aresta(matriz, vertices, o, d, nao_direcionado=NAO_DIRECIONADO)

        elif escolha == '6':
            v = input("Listar vizinhos de qual vértice: ")
            listar_vizinhos(matriz, vertices, v)

        elif escolha == '7':
            o = input("Verificar origem: ")
            d = input("Verificar destino: ")
            if existe_aresta(matriz, vertices, o, d):
                print(f"SIM, existe aresta {o} -> {d}.")
            else:
                print(f"NÃO, não existe aresta {o} -> {d}.")

        elif escolha == '8':
            graus = grau_vertices(matriz, vertices, nao_direcionado=NAO_DIRECIONADO)
            print("\n--- Graus dos Vértices ---")
            if not graus:
                print("Grafo vazio.")
            elif NAO_DIRECIONADO:
                 for v, grau in sorted(graus.items()):
                     print(f"  {v}: Grau = {grau}")
            else:
                for v, d in sorted(graus.items()):
                    print(f"  {v}: Saída={d['saida']}, Entrada={d['entrada']}, Total={d['total']}")

        elif escolha == '9':
            caminho_str = input("Digite o caminho (vértices separados por vírgula): ")
            caminho_lista = [v.strip() for v in caminho_str.split(',') if v.strip()]
            
            if not caminho_lista:
                print("Caminho vazio.")
            else:
                caminho_formatado = " -> ".join(caminho_lista)
                if percurso_valido(matriz, vertices, caminho_lista):
                    print(f"O caminho '{caminho_formatado}' é VÁLIDO.")
                else:
                    print(f"O caminho '{caminho_formatado}' é INVÁLIDO.")

        elif escolha == '0':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
