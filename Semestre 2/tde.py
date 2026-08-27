# CRIANDO AS LISTAS
estoque = []
clientes = []
historicocliente = []
historicojogo = []

# FUNÇÃO PARA CADASTRAR CLIENTE
def cadastrar_cliente():
    cliente = input("\nInforme o cliente que deseja cadastrar: ")
    plano = input("Informe o tipo de plano (VIP ou NORMAL): ")
    if plano.lower() != "vip" and plano.lower() != "normal":
        print("Plano inválido.")
    
    else:
        clientes.append((cliente, plano))

# FUNÇÃO PARA CADASTRAR JOGO
def cadastrar_jogo():
    jogo = input("\nInforme o jogo que deseja cadastrar: ")
    statusjogo = input("Informe o status do jogo (alugado ou disponivel): ")
    if statusjogo.lower() != "alugado" and statusjogo.lower() != "disponivel" and statusjogo.lower() != "disponível":
        print("Status do jogo inválido.")
    
    else:
        estoque.append((jogo, statusjogo))

# FUNÇÃO PARA BUSCAR CLIENTE
def buscar_cliente():
    if len(clientes) == 0:
        print("Nenhum cliente cadstrado.")
        return

    else:
        clientepesquisado = input("\nInforme qual cliente deseja buscar: ")

        achou = False
        indice = 0
        while indice < len(clientes):
            if clientes[indice][0] == clientepesquisado:
                clienteencontrado = clientes[indice]
                print(f"Cliente: {clienteencontrado}")
                achou = True
                break
            
            indice += 1
            
        if achou == False:
            print("Cliente não existe.")

# FUNÇÃO PARA BUSCAR JOGO
def buscar_jogo():
    if len(estoque) == 0:
        print("Nenhum jogo cadstrado.")
        return

    else:
        jogopesquisado = input("\nInforme qual jogo deseja buscar: ")
        
        achou = False
        indice = 0
        while indice < len(estoque):
            if estoque[indice][0] == jogopesquisado:
                jogoencontrado = estoque[indice]
                print(f"Jogo: {jogoencontrado}")
                achou = True
                break
            
            indice += 1
                
        if achou == False:
            print("Jogo não existe.")

# FUNÇÃO PARA EDITAR AS INFORMAÇÕES DO CLIENTE
def editar_cliente():
    if len(clientes) == 0:
        print("Nenhum cliente cadastrado.")
        return
        
    else:
        clienteeditado = input("\nInforme qual cliente deseja editar: ")
        
        achou = False
        indice = 0
        while indice < len(clientes):
            if clientes[indice][0] == clienteeditado:
                novonome = input("Novo nome: ")
                novoplano = input("Novo plano (VIP ou NORMAL): ")
                if novoplano.lower() != "vip" and novoplano.lower() != "normal":
                    print("Novo plano inválido.")
                    
                else:
                    clientes[indice] = (novonome, novoplano)
                    print("Cliente atualizado!")
                achou = True
                break
            
            indice += 1    
            
        if achou == False:
            print("Cliente não existe.")

# FUNÇÃO PARA EDITAR AS INFORMAÇÕES DO JOGO
def editar_jogo():
    if len(estoque) == 0:
        print("Nenhum jogo cadastrado.")
        return
    
    else:
        jogoeditado = input("\nInforme qual jogo deseja editar: ")

        achou = False
        indice = 0
        while indice < len(estoque):
            if estoque[indice][0] == jogoeditado:
                novonome = input("Novo nome: ")
                novostatus = input("Novo status do jogo: ")
                if novostatus.lower() != "alugado" and novostatus.lower() != "disponivel" and novostatus.lower() != "disponível":
                    print("Novo status do jogo inválido.")
                
                else:
                    estoque[indice] = (novonome, novostatus)
                print("Jogo atualizado!")
                achou = True
                break
                
            indice += 1
                
        if achou == False:
            print("Jogo não existe.")

# FUNÇÃO PARA REMOVER CLIENTE
def remover_cliente():
    if len(clientes) == 0:
        print("Nenhum cliente cadstrado.")
        return

    else:
        clienteremovido = input("\nInforme o cliente que deseja remover: ")
        
        achou = False
        indice = 0
        while indice < len(clientes):
            if clientes[indice][0] == clienteremovido:
                removido = clientes.pop(indice)
                historicocliente.append(removido)
                achou = True
                break
                
            indice += 1
                
        if achou == False:
            print("Cliente não existe.")

# FUNÇÃO PARA REMOVER JOGO
def remover_jogo():
    if len(estoque) == 0:
        print("Nenhum jogo cadstrado.")
        return

    else:
        remocaojogo = input("\nInforme o jogo que deseja remover: ")
        
        achou = False
        indice = 0
        while indice < len(estoque):
            if estoque[indice][0] == remocaojogo:
                removido = estoque.pop(indice)
                historicojogo.append(removido)
                achou = True
                break
            
            indice += 1
                
        if achou == False:
            print("Jogo não existe.")

# FUNÇÃO PARA MOSTRAR O HISTORICO DE CLIENTES           
def mostrarhistoricoclientes():
    if len(historicocliente) == 0:
        print("Nenhum historico disponivel.")
        return
    
    for i in range(len(historicocliente)):
        print(f"\nCliente {i + 1}: {historicocliente[i]}")

# FUNÇÃO PARA MOSTRAR O HISTORICO DE JOGOS
def mostrarhistoricoestoque():
    if len(historicojogo) == 0:
        print("Nenhum historico disponivel.")
        return
    
    for i in range(len(historicojogo)):
        print(f"\nJogo {i + 1}: {historicojogo[i]}")

# FUNÇÃO PARA MOSTRAR A FILA DE PRIORIDADES         
def filaprioridade():
    if len(clientes) == 0:
        print("Nenhum cliente na fila.")
        return
    
    print("\n==== ORDEM DE ATENDIMENTO ====")
    for c in clientes:
        if c[1].lower() == "vip":
            print(f"[PRIORIDADE] Cliente: {c[0]}")
            
    for c in clientes:
        if c[1].lower() == "normal":
            print(f"[COMUM] Cliente: {c[0]}")

# FUNÇÃO PARA MOSTRAR A LISTA DE JOGOS ORDENADOS           
def quicksort(arr, esquerda, direita):
    if esquerda < direita:
        pi = particao(arr, esquerda, direita)
        quicksort(arr, esquerda, pi-1)
        quicksort(arr, pi+1, direita)
        
def particao(arr, esquerda, direita):
    pivo = arr[direita]
    i = esquerda -1
    
    for j in range(esquerda, direita):
        if arr[j] <= pivo:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
            
    arr[i+1], arr[direita] = arr[direita], arr[i+1]
    return i+1

# FUNÇÃO PARA RESTAURAR UM CLIENTE DO HISTORICO          
def restaurarcliente():
    if len(historicocliente) == 0:
        print("Nenhum historico disponivel.")
        return
    
    else:
        ultimo = historicocliente.pop()
        clientes.append(ultimo)
        print("Cliente restaurado.")

# FUNÇÃO PARA RESTAURAR UM JOGO DO HISTORICO           
def restaurarjogo():
    if len(historicojogo) == 0:
        print("Nenhum historico disponivel.")
        return
    
    else:
        ultimo = historicojogo.pop()
        estoque.append(ultimo)
        print("Jogo restaurado.")

# MENU DE OPÇÕES
while True:
    print("\n==== MENU ====")
    print("1- CADASTRO")
    print("2- BUSCAR")
    print("3- EDITAR")
    print("4- REMOVER")
    print("5- RELATORIOS")
    print("6- DESFAZER")
    print("7- SAIR")
    print("================")
    escolha = int(input("\nEscolha uma opção: "))

    match escolha:
        # OPÇÃO PARA CADASTRAR (JOGO OU CLIENTE)
        case 1:
            tipocadastro = input("Informe o que deseja cadastrar (jogo ou cliente): ")

            if tipocadastro.lower() == "cliente":
                vezes = int(input("Informe quantos clientes quer cadastrar: "))
                for i in range(vezes):
                    cadastrar_cliente()

            elif tipocadastro.lower() == "jogo":
                vezes = int(input("Informe quantos jogos quer cadastrar: "))
                for i in range(vezes):
                    cadastrar_jogo()

            else:
                print("Opção inválida.")

        # OPÇÃO PARA BUSCAR (JOGO OU CLIENTE)
        case 2:
            tipobusca = input("Informe o que deseja buscar (jogo ou cliente): ")

            if tipobusca.lower() == "cliente":
                buscar_cliente()

            elif tipobusca.lower() == "jogo":                
                 buscar_jogo()

            else:
                print("Opção inválida.")

        # OPÇÃO PARA EDITAR (JOGO OU CLIENTE)
        case 3:
            tipoeditar = input("Editar (jogo ou cliente): ")

            if tipoeditar.lower() == "cliente":
                editar_cliente()

            elif tipoeditar.lower() == "jogo":
                editar_jogo()

            else:
                print("Opção inválida.")

        # OPÇÃO PARA REMOVER (JOGO OU CLIENTE)
        case 4:
            nomecliente = [cliente[0] for cliente in clientes]
            nomejogo = [jogo[0] for jogo in estoque]

            tiporemocao = input("Informe o que deseja excluir (jogo ou cliente): ")
            if tiporemocao.lower() == "cliente":
                remover_cliente()

            elif tiporemocao.lower() == "jogo":
                remover_jogo()

            else:
                print("Opção inválida.")
        
        # OPÇÃO PARA VER RELATORIOS (HISTORICOS, FILA E ORDENAÇÃO)                
        case 5:
            # MENU RELATORIOS
            while True:
                print("\n==== MENU ====")
                print("1- HISTORICOS")
                print("2- FILA PRIORIDADE")
                print("3- JOGOS ORDENADOS")
                print("4- SAIR")
                print("================")
                escolharelatorio =  int(input("\nEscolha uma opção: "))
                
                match escolharelatorio:
                    # OPÇÃO PARA VER HISTORICOS (JOGO OU CLIENTE)
                    case 1:
                        tipohistorico = input("Informe qual historico deseja ver (cliente ou jogo): ")
                        
                        if tipohistorico.lower() == "cliente":
                            mostrarhistoricoclientes()
                                
                        elif tipohistorico.lower() == "jogo":
                            mostrarhistoricoestoque()
                            
                        else:
                            print("Opção inválida.")
                    
                    # OPÇÃO PARA VER FILA PRIORIDADE (CLIENTE)        
                    case 2:
                        filaprioridade()
                    
                    # OPÇÃO PARA VER ORDENAÇÃO (JOGO)   
                    case 3:
                        quicksort(estoque, 0, len(estoque)-1)
                        for a in estoque:
                            print(f"Jogo: {a}")
                    
                    # OPÇÃO PARA SAIR DO MENU RELATORIOS
                    case 4:
                        print("Saindo do menu relatorios...")
                        break
                    
                    # OPÇÃO PARA CASO O USUARIO DIGITE UMA OPÇÃO INVÁLIDA
                    case _:
                        print("Opção inválida.")
        
        # OPÇÃO PARA RESTAURAR (JOGO OU CLIENTE)                
        case 6:
            tipodesfazer = input("Informe qual historico deseja desfazer (cliente ou jogo): ")
            
            if tipodesfazer.lower() ==  "cliente":
                restaurarcliente()
            
            elif tipodesfazer.lower() == "jogo":
                restaurarjogo()
                            
            else:
                print("Opção inválida.")

        # OPÇÃO PARA SAIR DO PROGRAMA
        case 7:
            print("Saindo do programa...")
            break
        
        # OPÇÃO PARA CASO O USUARIO DIGITE UMA OPÇÃO INVÁLIDA      
        case _:
            print("Opção inválida.")