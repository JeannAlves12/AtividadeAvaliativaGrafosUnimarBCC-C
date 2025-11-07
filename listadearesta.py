def criar_grafo():
    """
    Cria e retorna uma estrutura de grafo com lista de arestas e lista de vértices.

    Passos:
    1. Criar uma lista vazia chamada 'vertices'.
    2. Criar uma lista vazia chamada 'arestas', onde cada elemento será uma lista de tamanho 2 (origem, destino)
    3. Retornar vertices e arestas
    """
    vertices = []
    arestas = []
    return vertices, arestas


def inserir_vertice(vertices, vertice):
    """
    Adiciona um novo vértice no grafo.

    Passos:
    1. Verificar se o vértice já existe em 'vertices'.
    2. Se não existir, adicionar à lista 'vertices'.
    """
    if vertice not in vertices:
        vertices.append(vertice)
        return True
    return False 


def inserir_aresta(vertices, arestas, origem, destino, nao_direcionado=False):
    """
    Adiciona uma aresta entre dois vértices.

    Passos:
    1. Garantir que 'origem' e 'destino' existam em 'vertices'.
       - Se não existirem, chamar 'inserir_vertice' para adicioná-los.
    2. Adicionar uma lista [origem, destino] na lista 'arestas'.
    3. Se nao_direcionado=True, adicionar também [destino, origem].
    """
    inserir_vertice(vertices, origem)
    inserir_vertice(vertices, destino)

    aresta_frente = [origem, destino]
    if aresta_frente not in arestas:
        arestas.append(aresta_frente)
    
    if nao_direcionado:
        aresta_inversa = [destino, origem]
        if aresta_inversa not in arestas:
            arestas.append(aresta_inversa)


def remover_aresta(arestas, origem, destino, nao_direcionado=False):
    """
    Remove uma aresta entre dois vértices.

    Passos:
    1. Percorrer a lista de Arestas procurando [origem, destino]
    2. Se encontrar, remover
    3. Se nao_direcionado=True, também procurar por [destino, origem]
    """
    aresta_frente = [origem, destino]
    try:
        arestas.remove(aresta_frente)
    except ValueError:
        pass

    if nao_direcionado:
        aresta_inversa = [destino, origem]
        try:
            arestas.remove(aresta_inversa)
        except ValueError:
            pass


def remover_vertice(vertices, arestas, vertice):
    """
    Remove um vértice e todas as arestas conectadas a ele.

    Passos:
    1. Verificar se o vértice existe na lista de vertices.
    2. Caso encontrado, remover o vértice da lista 'vertices'.
    3. Percorrer a lista de 'arestas' e remover todas onde o vértice aparece
       como origem ou destino.
    """
    if vertice not in vertices:
        print(f"Erro: Vértice '{vertice}' não encontrado.")
        return False
        
    vertices.remove(vertice)
    
    arestas_filtradas = [a for a in arestas if vertice not in a]
    
    arestas[:] = arestas_filtradas
    
    print(f"Vértice '{vertice}' e suas arestas foram removidos.")
    return True


def existe_aresta(arestas, origem, destino):
    """
    Verifica se existe uma aresta entre origem e destino.

    Passos:
    1. Percorrer a lista de aresta procurando [origem, destino]
    2. Retornar True se encontrar
    3. Caso não encontre na lista, retornar False no final.
    """
    return [origem, destino] in arestas


def vizinhos(vertices, arestas, vertice):
    """
    Retorna a lista de vizinhos (vértices alcançáveis a partir de 'vertice').

    Passos:
    1. Criar uma lista vazia chamada 'vizinhos'.
    2. Percorrer todas as arestas [origem, destino].
    3. Se origem == vertice, adicionar destino na lista de vizinhos.
    4. Retornar a lista final.
    """
    vizinhos_set = set()
    
    for o, d in arestas:
        if o == vertice:
            vizinhos_set.add(d)
            
    return list(vizinhos_set)


def grau_vertices(vertices, arestas, nao_direcionado=False):
    """
    Calcula o grau de entrada, saída e total de cada vértice.
    (Adaptado para receber o parâmetro 'nao_direcionado')
    """
    if nao_direcionado:
        graus = {v: 0 for v in vertices}
        for o, d in arestas:
            if o in graus:
                graus[o] += 1
    else:
        graus = {v: {'in': 0, 'out': 0, 'total': 0} for v in vertices}
        
        for o, d in arestas:
            if o in graus:
                graus[o]['out'] += 1
            if d in graus:
                graus[d]['in'] += 1
                
        for v in graus:
            graus[v]['total'] = graus[v]['in'] + graus[v]['out']

    return graus


def percurso_valido(arestas, caminho):
    """
    Verifica se um percurso é possível (seguindo as arestas na ordem dada).

    Passos:
    1. Percorrer o caminho de 0 até len(caminho) - 2.
    2. Para cada par consecutivo (u, v):
          - Verificar se (u, v) existe na lista de 'arestas' (funcao existe_aresta).
          - Se alguma não existir, retornar False.
    3. Se todas existirem, retornar True.
    """
    if len(caminho) < 2:
        return True

    for i in range(len(caminho) - 1):
        u = caminho[i]
        v = caminho[i+1]
        
        if not existe_aresta(arestas, u, v):
            return False
            
    return True


def listar_vizinhos(vertices, arestas, vertice):
    """
    Exibe os vizinhos de um vértice.

    Passos:
    1. Chamar a função vizinhos() para obter a lista.
    2. Exibir a lista formatada.
    """
    if vertice not in vertices:
        print(f"Vértice '{vertice}' não encontrado no grafo.")
        return

    lista_v = vizinhos(vertices, arestas, vertice)
    
    if not lista_v:
        print(f"Vértice '{vertice}' não possui vizinhos (arestas de saída).")
    else:
        print(f"Vizinhos de '{vertice}': {', '.join(map(str, lista_v))}")


def exibir_grafo(vertices, arestas):
    """
    Exibe todas as arestas do grafo.

    Passos:
    1. Exibir a lista de vértices.
    2. Exibir todas as arestas no formato (origem -> destino).
    """
    if not vertices:
        print("O grafo está vazio.")
        return
        
    print(f"Vértices: {', '.join(map(str, sorted(vertices)))}")
    
    print("Arestas:")
    if not arestas:
        print("  (Nenhuma)")
    else:
        for o, d in sorted(arestas):
            print(f"  {o} -> {d}")


def main():
    """
    Menu interativo para manipular o grafo (lista de arestas).
    """
    vertices, arestas = criar_grafo()
    
    tipo_input = input("O grafo será Não-Direcionado? (s/n): ").strip().lower()
    NAO_DIRECIONADO = (tipo_input == 's')
    
    if NAO_DIRECIONADO:
        print("\n--- Grafo Não-Direcionado (Lista de Arestas) Criado ---")
    else:
        print("\n--- Grafo Direcionado (Lista de Arestas) Criado ---")

    while True:
        print("\n--- Menu de Opções (Lista de Arestas) ---")
        print(" 1. Exibir Grafo")
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
            print("\n--- Grafo Atual (Lista de Arestas) ---")
            exibir_grafo(vertices, arestas)

        elif escolha == '2':
            v = input("Nome do vértice a inserir: ")
            if inserir_vertice(vertices, v):
                print(f"Vértice '{v}' inserido.")
            else:
                print(f"Vértice '{v}' já existe.")

        elif escolha == '3':
            o = input("Vértice de origem: ")
            d = input("Vértice de destino: ")
            inserir_aresta(vertices, arestas, o, d, nao_direcionado=NAO_DIRECIONADO)
            if NAO_DIRECIONADO:
                 print(f"Aresta {o} <-> {d} inserida.")
            else:
                 print(f"Aresta {o} -> {d} inserida.")

        elif escolha == '4':
            v = input("Nome do vértice a remover: ")
            remover_vertice(vertices, arestas, v)

        elif escolha == '5':
            o = input("Vértice de origem da aresta: ")
            d = input("Vértice de destino da aresta: ")
            remover_aresta(arestas, o, d, nao_direcionado=NAO_DIRECIONADO)
            print(f"Aresta entre {o} e {d} removida (se existia).")

        elif escolha == '6':
            v = input("Listar vizinhos de qual vértice: ")
            listar_vizinhos(vertices, arestas, v)

        elif escolha == '7':
            o = input("Verificar origem: ")
            d = input("Verificar destino: ")
            if existe_aresta(arestas, o, d):
                print(f"SIM, existe aresta {o} -> {d}.")
            else:
                print(f"NÃO, não existe aresta {o} -> {d}.")

        elif escolha == '8':
            graus = grau_vertices(vertices, arestas, nao_direcionado=NAO_DIRECIONADO)
            print("\n--- Graus dos Vértices ---")
            if not graus:
                print("Grafo vazio.")
            elif NAO_DIRECIONADO:
                 for v, grau in sorted(graus.items()):
                     print(f"  {v}: Grau = {grau}")
            else:
                for v, d in sorted(graus.items()):
                    print(f"  {v}: Saída={d['out']}, Entrada={d['in']}, Total={d['total']}")

        elif escolha == '9':
            caminho_str = input("Digite o caminho (vértices separados por vírgula): ")
            caminho_lista = [v.strip() for v in caminho_str.split(',') if v.strip()]
            
            if not caminho_lista:
                print("Caminho vazio.")
            else:
                caminho_formatado = " -> ".join(caminho_lista)
                if percurso_valido(arestas, caminho_lista):
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
    