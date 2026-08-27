raiz_clientes = None
raiz_estoque  = None

historicocliente = [] 
historicojogo    = []  

def criar_no(chave, dados):
    return {
        "chave":  chave,
        "dados":  dados,
        "esq":    None,
        "dir":    None,
        "altura": 1
    }

def altura(no):
    if no is None:
        return 0
    return no["altura"]

def fator(no):
    return altura(no["esq"]) - altura(no["dir"])

def atualizar_altura(no):
    no["altura"] = 1 + max(altura(no["esq"]), altura(no["dir"]))

def rotacao_direita(y):
    x  = y["esq"]
    T2 = x["dir"]
    x["dir"] = y
    y["esq"] = T2
    atualizar_altura(y)
    atualizar_altura(x)
    return x

def rotacao_esquerda(x):
    y  = x["dir"]
    T2 = y["esq"]
    y["esq"] = x
    x["dir"] = T2
    atualizar_altura(x)
    atualizar_altura(y)
    return y

def balancear(no):
    atualizar_altura(no)
    fe = fator(no)

    if fe > 1:
        if fator(no["esq"]) < 0:
            no["esq"] = rotacao_esquerda(no["esq"])
        return rotacao_direita(no)          

    if fe < -1:
        if fator(no["dir"]) > 0:
            no["dir"] = rotacao_direita(no["dir"])
        return rotacao_esquerda(no)

    return no

def avl_inserir(no, chave, dados):
    if no is None:
        return criar_no(chave, dados)
    if chave < no["chave"]:
        no["esq"] = avl_inserir(no["esq"], chave, dados)
    elif chave > no["chave"]:
        no["dir"] = avl_inserir(no["dir"], chave, dados)
    else:
        no["dados"] = dados
        return no
    return balancear(no)

def avl_buscar(no, chave):
    if no is None:
        return None
    if chave == no["chave"]:
        return no["dados"]
    if chave < no["chave"]:
        return avl_buscar(no["esq"], chave)
    return avl_buscar(no["dir"], chave)

def avl_minimo(no):
    while no["esq"] is not None:
        no = no["esq"]
    return no

def avl_remover(no, chave, removido):
    if no is None:
        return None
    if chave < no["chave"]:
        no["esq"] = avl_remover(no["esq"], chave, removido)
    elif chave > no["chave"]:
        no["dir"] = avl_remover(no["dir"], chave, removido)
    else:
        removido.append(no["dados"])
        if no["esq"] is None:
            return no["dir"]
        if no["dir"] is None:
            return no["esq"]

        sucessor = avl_minimo(no["dir"])
        no["chave"] = sucessor["chave"]
        no["dados"] = sucessor["dados"]
        no["dir"] = avl_remover(no["dir"], sucessor["chave"], [])
    return balancear(no)

def em_ordem(no, resultado):
    if no:
        em_ordem(no["esq"], resultado)
        resultado.append(no["dados"])
        em_ordem(no["dir"], resultado)

def pre_ordem(no, resultado):
    if no:
        resultado.append(no["dados"])
        pre_ordem(no["esq"], resultado)
        pre_ordem(no["dir"], resultado)

def pos_ordem(no, resultado):
    if no:
        pos_ordem(no["esq"], resultado)
        pos_ordem(no["dir"], resultado)
        resultado.append(no["dados"])

def cadastrar_cliente():
    global raiz_clientes
    nome = input("\nInforme o nome do cliente: ").strip()
    if not nome:
        print("Nome não pode ser vazio.")
        return
    plano = input("Plano (VIP ou NORMAL): ").strip()
    if plano.lower() not in ("vip", "normal"):
        print("Plano inválido.")
        return
    raiz_clientes = avl_inserir(raiz_clientes, nome.lower(), (nome, plano.upper()))
    print("Cliente cadastrado!")

def buscar_cliente():
    if raiz_clientes is None:
        print("Nenhum cliente cadastrado.")
        return
    nome = input("\nInforme o cliente que deseja buscar: ").strip()
    resultado = avl_buscar(raiz_clientes, nome.lower())
    if resultado:
        print(f"Cliente encontrado: {resultado[0]} | Plano: {resultado[1]}")
    else:
        print("Cliente não encontrado.")

def editar_cliente():
    global raiz_clientes
    if raiz_clientes is None:
        print("Nenhum cliente cadastrado.")
        return
    nome = input("\nInforme o cliente que deseja editar: ").strip()
    dados = avl_buscar(raiz_clientes, nome.lower())
    if not dados:
        print("Cliente não encontrado.")
        return
    novo_nome  = input("Novo nome: ").strip()
    novo_plano = input("Novo plano (VIP ou NORMAL): ").strip()
    if novo_plano.lower() not in ("vip", "normal"):
        print("Plano inválido.")
        return
    removido = []
    raiz_clientes = avl_remover(raiz_clientes, nome.lower(), removido)
    raiz_clientes = avl_inserir(raiz_clientes, novo_nome.lower(), (novo_nome, novo_plano.upper()))
    print("Cliente atualizado!")

def remover_cliente():
    global raiz_clientes
    if raiz_clientes is None:
        print("Nenhum cliente cadastrado.")
        return
    nome = input("\nInforme o cliente que deseja remover: ").strip()
    removido = []
    raiz_clientes = avl_remover(raiz_clientes, nome.lower(), removido)
    if removido:
        historicocliente.append(removido[0])
        print(f"Cliente '{removido[0][0]}' removido.")
    else:
        print("Cliente não encontrado.")

def cadastrar_jogo():
    global raiz_estoque
    jogo = input("\nInforme o nome do jogo: ").strip()
    if not jogo:
        print("Nome não pode ser vazio.")
        return
    status = input("Status (alugado ou disponivel): ").strip()
    if status.lower() not in ("alugado", "disponivel", "disponível"):
        print("Status inválido.")
        return
    raiz_estoque = avl_inserir(raiz_estoque, jogo.lower(), (jogo, status.lower()))
    print("Jogo cadastrado!")

def buscar_jogo():
    if raiz_estoque is None:
        print("Nenhum jogo cadastrado.")
        return
    nome = input("\nInforme o jogo que deseja buscar: ").strip()
    resultado = avl_buscar(raiz_estoque, nome.lower())
    if resultado:
        print(f"Jogo encontrado: {resultado[0]} | Status: {resultado[1]}")
    else:
        print("Jogo não encontrado.")

def editar_jogo():
    global raiz_estoque
    if raiz_estoque is None:
        print("Nenhum jogo cadastrado.")
        return
    nome = input("\nInforme o jogo que deseja editar: ").strip()
    dados = avl_buscar(raiz_estoque, nome.lower())
    if not dados:
        print("Jogo não encontrado.")
        return
    novo_nome   = input("Novo nome: ").strip()
    novo_status = input("Novo status (alugado ou disponivel): ").strip()
    if novo_status.lower() not in ("alugado", "disponivel", "disponível"):
        print("Status inválido.")
        return
    removido = []
    raiz_estoque = avl_remover(raiz_estoque, nome.lower(), removido)
    raiz_estoque = avl_inserir(raiz_estoque, novo_nome.lower(), (novo_nome, novo_status.lower()))
    print("Jogo atualizado!")

def remover_jogo():
    global raiz_estoque
    if raiz_estoque is None:
        print("Nenhum jogo cadastrado.")
        return
    nome = input("\nInforme o jogo que deseja remover: ").strip()
    removido = []
    raiz_estoque = avl_remover(raiz_estoque, nome.lower(), removido)
    if removido:
        historicojogo.append(removido[0])
        print(f"Jogo '{removido[0][0]}' removido.")
    else:
        print("Jogo não encontrado.")

def mostrar_historico_clientes():
    if not historicocliente:
        print("Nenhum histórico disponível.")
        return
    print("\n==== HISTÓRICO DE CLIENTES REMOVIDOS (topo → base) ====")
    for i in range(len(historicocliente) - 1, -1, -1):
        print(f"  {i+1}. {historicocliente[i][0]} | Plano: {historicocliente[i][1]}")

def mostrar_historico_jogos():
    if not historicojogo:
        print("Nenhum histórico disponível.")
        return
    print("\n==== HISTÓRICO DE JOGOS REMOVIDOS (topo → base) ====")
    for i in range(len(historicojogo) - 1, -1, -1):
        print(f"  {i+1}. {historicojogo[i][0]} | Status: {historicojogo[i][1]}")

def restaurar_cliente():
    global raiz_clientes
    if not historicocliente:
        print("Nenhum histórico disponível.")
        return
    ultimo = historicocliente.pop()
    raiz_clientes = avl_inserir(raiz_clientes, ultimo[0].lower(), ultimo)
    print(f"Cliente '{ultimo[0]}' restaurado!")

def restaurar_jogo():
    global raiz_estoque
    if not historicojogo:
        print("Nenhum histórico disponível.")
        return
    ultimo = historicojogo.pop()
    raiz_estoque = avl_inserir(raiz_estoque, ultimo[0].lower(), ultimo)
    print(f"Jogo '{ultimo[0]}' restaurado!")

def fila_prioridade():
    todos = []
    em_ordem(raiz_clientes, todos)
    if not todos:
        print("Nenhum cliente na fila.")
        return
    print("\n==== ORDEM DE ATENDIMENTO ====")
    print("--- VIP (prioridade) ---")
    for c in todos:
        if c[1] == "VIP":
            print(f"  [VIP] {c[0]}")
    print("--- NORMAL ---")
    for c in todos:
        if c[1] == "NORMAL":
            print(f"  [NORMAL] {c[0]}")

def quicksort(arr, esquerda, direita, campo=0):
    if esquerda < direita:
        pi = particao(arr, esquerda, direita, campo)
        quicksort(arr, esquerda, pi - 1, campo)
        quicksort(arr, pi + 1, direita, campo)

def particao(arr, esquerda, direita, campo):
    pivo = arr[direita][campo]
    i = esquerda - 1
    for j in range(esquerda, direita):
        if arr[j][campo] <= pivo:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[direita] = arr[direita], arr[i + 1]
    return i + 1

def relatorio_clientes_em_ordem():
    dados = []
    em_ordem(raiz_clientes, dados)
    if not dados:
        print("Nenhum cliente cadastrado.")
        return
    print("\n==== CLIENTES — IN-ORDER ====")
    for c in dados:
        print(f"  {c[0]} | Plano: {c[1]}")

def relatorio_clientes_pre_ordem():
    dados = []
    pre_ordem(raiz_clientes, dados)
    if not dados:
        print("Nenhum cliente cadastrado.")
        return
    print("\n==== CLIENTES — PRÉ-ORDER ====")
    for c in dados:
        print(f"  {c[0]} | Plano: {c[1]}")

def relatorio_clientes_pos_ordem():
    dados = []
    pos_ordem(raiz_clientes, dados)
    if not dados:
        print("Nenhum cliente cadastrado.")
        return
    print("\n==== CLIENTES — PÓS-ORDER ====")
    for c in dados:
        print(f"  {c[0]} | Plano: {c[1]}")

def relatorio_jogos_em_ordem():
    dados = []
    em_ordem(raiz_estoque, dados)
    if not dados:
        print("Nenhum jogo cadastrado.")
        return
    print("\n==== JOGOS — IN-ORDER ====")
    for j in dados:
        print(f"  {j[0]} | Status: {j[1]}")

def relatorio_jogos_pre_ordem():
    dados = []
    pre_ordem(raiz_estoque, dados)
    if not dados:
        print("Nenhum jogo cadastrado.")
        return
    print("\n==== JOGOS — PRÉ-ORDER ====")
    for j in dados:
        print(f"  {j[0]} | Status: {j[1]}")

def relatorio_jogos_pos_ordem():
    dados = []
    pos_ordem(raiz_estoque, dados)
    if not dados:
        print("Nenhum jogo cadastrado.")
        return
    print("\n==== JOGOS — PÓS-ORDER ====")
    for j in dados:
        print(f"  {j[0]} | Status: {j[1]}")

def relatorio_jogos_quicksort():
    dados = []
    em_ordem(raiz_estoque, dados)
    if not dados:
        print("Nenhum jogo cadastrado.")
        return
    quicksort(dados, 0, len(dados) - 1, campo=1)
    print("\n==== JOGOS ORDENADOS POR STATUS ====")
    for j in dados:
        print(f"  {j[0]} | Status: {j[1]}")

while True:
    print("\n==== MENU PRINCIPAL ====")
    print("1 - Cadastrar")
    print("2 - Buscar")
    print("3 - Editar")
    print("4 - Remover")
    print("5 - Relatórios")
    print("6 - Desfazer remoção")
    print("7 - Sair")
    print("========================")
    escolha = input("\nEscolha uma opção: ").strip()

    match escolha:
        case "1":
            tipo = input("Cadastrar (cliente ou jogo): ").strip().lower()
            if tipo == "cliente":
                vezes = int(input("Quantos clientes: "))
                for _ in range(vezes):
                    cadastrar_cliente()
                    
            elif tipo == "jogo":
                vezes = int(input("Quantos jogos: "))
                for _ in range(vezes):
                    cadastrar_jogo()
                    
            else:
                print("Opção inválida.")

        case "2":
            tipo = input("Buscar (cliente ou jogo): ").strip().lower()
            if tipo == "cliente":
                buscar_cliente()
                
            elif tipo == "jogo":
                buscar_jogo()
                
            else:
                print("Opção inválida.")

        case "3":
            tipo = input("Editar (cliente ou jogo): ").strip().lower()
            if tipo == "cliente":  
                editar_cliente()
            
            elif tipo == "jogo":   
                editar_jogo()
            
            else:
                print("Opção inválida.")

        case "4":
            tipo = input("Remover (cliente ou jogo): ").strip().lower()
            if tipo == "cliente":  
                remover_cliente()
            
            elif tipo == "jogo":   
                remover_jogo()
            
            else:  
                print("Opção inválida.")

        case "5":
            while True:
                print("\n==== RELATÓRIOS ====")
                print("1  - Clientes (em ordem)")
                print("2  - Clientes (pré-ordem)")
                print("3  - Clientes (pós-ordem)")
                print("4  - Jogos (em ordem)")
                print("5  - Jogos (pré-ordem)")
                print("6  - Jogos (pós-ordem)")
                print("7  - Jogos ordenados por status (Quicksort)")
                print("8  - Fila de prioridade")
                print("9  - Histórico de clientes removidos")
                print("10 - Histórico de jogos removidos")
                print("0  - Voltar")
                print("====================")
                escolha_relatorios = input("\nEscolha: ").strip()
                
                match escolha_relatorios:
                    case "1":  
                        relatorio_clientes_em_ordem()
                        
                    case "2":  
                        relatorio_clientes_pre_ordem()
                    
                    case "3":  
                        relatorio_clientes_pos_ordem()
                    
                    case "4":  
                        relatorio_jogos_em_ordem()
                    
                    case "5":  
                        relatorio_jogos_pre_ordem()
                    
                    case "6":  
                        relatorio_jogos_pos_ordem()
                    
                    case "7":  
                        relatorio_jogos_quicksort()
                    
                    case "8":  
                        fila_prioridade()
                    
                    case "9":  
                        mostrar_historico_clientes()
                    
                    case "10": 
                        mostrar_historico_jogos()
                    
                    case "0":
                        print("Saindo do menu relatorios.")
                        break
                    
                    case _:    print("Opção inválida.")

        case "6":
            tipo = input("Desfazer remoção de (cliente ou jogo): ").strip().lower()
            if tipo == "cliente":  
                restaurar_cliente()
                
            elif tipo == "jogo":   
                restaurar_jogo()
                
            else:                 
                print("Opção inválida.")

        case "7":
            print("Saindo...")
            break

        case _:
            print("Opção inválida.")