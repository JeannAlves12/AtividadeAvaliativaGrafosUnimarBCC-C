def criar_grafo():
    """
    Retorna um novo grafo vazio.
    Passos:
    1. Criar um dicionário vazio: {}
    2. Retornar o dicionário (representa o grafo)
    """
    return {}


def inserir_vertice(grafo, vertice):
    """
    Insere um vértice no grafo, sem arestas iniciais.
    Passos:
    1. Verificar se 'vertice' já é chave em grafo.
    2. Se não for, criar entrada grafo[vertice] = []
    3. Se já existir, não fazer nada (ou avisar)
    """
    if vertice not in grafo:
        grafo[vertice] = []
        return True
    return False


def inserir_aresta(grafo, origem, destino, nao_direcionado=False):
    """
    Adiciona aresta entre origem e destino.
    Passos:
    1. Garantir que 'origem' e 'destino' existam no grafo (inserir se necessário).
    2. adicionar destino como vizinho de origem (append).
    3. Se for Nâo Direcionado, também:
          - adicionar origem como vizinho de destino
    """
    inserir_vertice(grafo, origem)
    inserir_vertice(grafo, destino)

    if destino not in grafo[origem]:
        grafo[origem].append(destino)
    
    if nao_direcionado:
        if origem not in grafo[destino]:
            grafo[destino].append(origem)


def vizinhos(grafo, vertice):
    """
    Retorna a lista de vizinhos de 'vertice'.
    Passos:
    1. Se 'vertice' estiver em grafo, retornar grafo[vertice] (lista).
    2. Se não existir, retornar lista vazia ou sinalizar erro.
    """
    return grafo.get(vertice, [])


def listar_vizinhos(grafo, vertice):
    """
    Função semântica: imprimir/retornar os vizinhos de 'vertice'.
    Passos:
    1. Obter lista = vizinhos(grafo, vertice)
    2. Retornar/imprimir essa lista (ou informar que o vértice não existe)
    """
    if vertice not in grafo:
        print(f"Vértice '{vertice}' não encontrado no grafo.")
        return

    lista_v = vizinhos(grafo, vertice)
    
    if not lista_v:
        print(f"Vértice '{vertice}' não possui vizinhos.")
    else:
        print(f"Vizinhos de '{vertice}': {', '.join(map(str, lista_v))}")


def exibir_grafo(grafo):
    """
    Exibe o grafo em forma legível (lista de adjacência).
    Passos:
    1. Para cada vertice em ordem
          - imprimir: vertice -> vizinhos
    """
    if not grafo:
        print("O grafo está vazio.")
        return

    for vertice in sorted(grafo):
        lista_vizinhos_str = ", ".join(map(str, grafo[vertice]))
        print(f"  {vertice} -> [ {lista_vizinhos_str} ]")


def remover_aresta(grafo, origem, destino, nao_direcionado=False):
    """
    Remove a aresta entre origem e destino.
    Passos:
    1. Verificar se 'origem' existe; se não, terminar.
    2. Se destino estiver em grafo[origem], remover essa ocorrência.
    3. Se for não direcionado, também:
          - verificar se 'destino' existe e remover 'origem' de grafo[destino] se presente.
    """
    if origem in grafo:
        if destino in grafo[origem]:
            grafo[origem].remove(destino)

    if nao_direcionado:
        if destino in grafo:
            if origem in grafo[destino]:
                grafo[destino].remove(origem)


def remover_vertice(grafo, vertice, nao_direcionado=True):
    """
    Remove um vértice e todas as arestas que o tocam.
    Passos:
    1. Verificar se 'vertice' existe em grafo; se não, terminar.
    2. Para cada outro vertice no grafo:
          - se 'vertice' estiver na lista de vizinhos, remover essa aresta.
    3. Remover o vertice do grafo
    4. Opcional: retornar confirmação/erro.
    """
    if vertice not in grafo:
        print(f"Erro: Vértice '{vertice}' não encontrado.")
        return False

    for v_atual in list(grafo.keys()):
        if v_atual != vertice and vertice in grafo[v_atual]:
            grafo[v_atual].remove(vertice)
    
    del grafo[vertice]
    return True


def existe_aresta(grafo, origem, destino):
    """
    Verifica se existe aresta direta origem -> destino.
    Passos:
    1. Verificar se 'origem' é chave no grafo.
    2. Retornar True se 'destino' estiver em grafo[origem], caso contrário False.
    """
    return origem in grafo and destino in grafo[origem]


def grau_vertices(grafo):
    """
    Calcula e retorna o grau (out, in, total) de cada vértice.
    Passos:
    1. Inicializar um dict de graus vazia
    2. Para cada vertice, colocar no dict uma estrutura com in, out e total zerado
    3. Para cada u em grafo:
          - out_degree[u] = tamanho de vizinhos
          - para cada v em grafo:
             - verificar se u está na lista de vizinho de v,
             - caso esteja, adicionar +1 para o grau de entrada de u
    4. Calcular o grau total somando entrada + saida
    5. Retornar uma estrutura contendo out,in,total por vértice (ex: dict de dicts).
    """
    graus = {v: {'in': 0, 'out': 0, 'total': 0} for v in grafo}

    for u in grafo:
        graus[u]['out'] = len(grafo[u])
        for v in grafo:
            if u in grafo[v]:
                graus[u]['in'] += 1

    for v in graus:
        graus[v]['total'] = graus[v]['in'] + graus[v]['out']

    return graus


def percurso_valido(grafo, caminho):
    """
    Verifica se uma sequência específica de vértices (caminho) é válida:
    i.e., se existem arestas consecutivas entre os nós do caminho.
    Passos:
    1. Se caminho tiver tamanho < 2, retornar True (trivial).
    2. Para i de 0 até len(caminho)-2:
          - origem = caminho[i], destino = caminho[i+1]
          - se não existe_aresta(grafo, origem, destino): retornar False
    3. Se todas as arestas existirem, retornar True.
    """
    if len(caminho) < 2:
        return True
    
    for i in range(len(caminho) - 1):
        origem = caminho[i]
        destino = caminho[i+1]
        
        if not existe_aresta(grafo, origem, destino):
            return False
            
    return True


def main():
    """
    Crie um menu onde seja possível escolher qual ação deseja realizar
    ex:
        1 - Mostrar o Grafo
        2 - inserir vertice
        3 - inserir aresta
        4 - remover vértice.
        ....
    """
    g = criar_grafo()
    
    tipo_input = input("O grafo será Não-Direcionado? (s/n): ").strip().lower()
    NAO_DIRECIONADO = (tipo_input == 's')
    
    if NAO_DIRECIONADO:
        print("\n--- Grafo Não-Direcionado Criado ---")
    else:
        print("\n--- Grafo Direcionado Criado ---")

    while True:
        print("\n--- Menu de Opções ---")
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
            print("\n--- Grafo Atual ---")
            exibir_grafo(g)

        elif escolha == '2':
            v = input("Nome do vértice a inserir: ")
            if inserir_vertice(g, v):
                print(f"Vértice '{v}' inserido.")
            else:
                print(f"Vértice '{v}' já existe.")

        elif escolha == '3':
            o = input("Vértice de origem: ")
            d = input("Vértice de destino: ")
            inserir_aresta(g, o, d, nao_direcionado=NAO_DIRECIONADO)
            if NAO_DIRECIONADO:
                 print(f"Aresta {o} <-> {d} inserida.")
            else:
                 print(f"Aresta {o} -> {d} inserida.")

        elif escolha == '4':
            v = input("Nome do vértice a remover: ")
            if remover_vertice(g, v):
                print(f"Vértice '{v}' e todas as suas arestas foram removidos.")

        elif escolha == '5':
            o = input("Vértice de origem da aresta: ")
            d = input("Vértice de destino da aresta: ")
            remover_aresta(g, o, d, nao_direcionado=NAO_DIRECIONADO)
            print(f"Aresta entre {o} e {d} removida (se existia).")

        elif escolha == '6':
            v = input("Listar vizinhos de qual vértice: ")
            listar_vizinhos(g, v)

        elif escolha == '7':
            o = input("Verificar origem: ")
            d = input("Verificar destino: ")
            if existe_aresta(g, o, d):
                print(f"SIM, existe aresta {o} -> {d}.")
            else:
                print(f"NÃO, não existe aresta {o} -> {d}.")

        elif escolha == '8':
            graus = grau_vertices(g)
            print("\n--- Graus dos Vértices ---")
            if not graus:
                print("Grafo vazio.")
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
                if percurso_valido(g, caminho_lista):
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