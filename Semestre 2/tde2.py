class No:
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor
        self.esquerda = None
        self.direita = None
        self.altura = 1


class Arvore:
    def __init__(self):
        self.raiz = None

    def _altura(self, no):
        if no is None:
            return 0
        return no.altura

    def _fator_balanceamento(self, no):
        if no is None:
            return 0
        return self._altura(no.esquerda) - self._altura(no.direita)

    def _atualizar_altura(self, no):
        no.altura = 1 + max(self._altura(no.esquerda), self._altura(no.direita))

    def _rotacao_direita(self, y):
        x = y.esquerda
        z = x.direita
        x.direita = y
        y.esquerda = z
        self._atualizar_altura(y)
        self._atualizar_altura(x)
        return x

    def _rotacao_esquerda(self, x):
        y = x.direita
        z = y.esquerda
        y.esquerda = x
        x.direita = z
        self._atualizar_altura(x)
        self._atualizar_altura(y)
        return y

    def _balancear(self, no):
        self._atualizar_altura(no)
        fb = self._fator_balanceamento(no)

        if fb > 1 and self._fator_balanceamento(no.esquerda) >= 0:
            return self._rotacao_direita(no)

        if fb > 1 and self._fator_balanceamento(no.esquerda) < 0:
            no.esquerda = self._rotacao_esquerda(no.esquerda)
            return self._rotacao_direita(no)

        if fb < -1 and self._fator_balanceamento(no.direita) <= 0:
            return self._rotacao_esquerda(no)

        if fb < -1 and self._fator_balanceamento(no.direita) > 0:
            no.direita = self._rotacao_direita(no.direita)
            return self._rotacao_esquerda(no)

        return no

    def _inserir(self, no, chave, valor):
        if no is None:
            return No(chave, valor)
        if chave < no.chave:
            no.esquerda = self._inserir(no.esquerda, chave, valor)
        elif chave > no.chave:
            no.direita = self._inserir(no.direita, chave, valor)
        else:
            no.valor = valor
            return no
        return self._balancear(no)

    def inserir(self, chave, valor):
        self.raiz = self._inserir(self.raiz, chave.lower(), valor)

    def _minimo(self, no):
        atual = no
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual

    def _remover(self, no, chave):
        if no is None:
            return no, False
        encontrou = False
        if chave < no.chave:
            no.esquerda, encontrou = self._remover(no.esquerda, chave)
        elif chave > no.chave:
            no.direita, encontrou = self._remover(no.direita, chave)
        else:
            encontrou = True
            if no.esquerda is None:
                return no.direita, encontrou
            elif no.direita is None:
                return no.esquerda, encontrou
            else:
                sucessor = self._minimo(no.direita)
                no.chave = sucessor.chave
                no.valor = sucessor.valor
                no.direita, _ = self._remover(no.direita, sucessor.chave)
        return self._balancear(no), encontrou

    def remover(self, chave):
        self.raiz, encontrou = self._remover(self.raiz, chave.lower())
        return encontrou

    def _buscar(self, no, chave):
        if no is None:
            return None
        if chave == no.chave:
            return no.valor
        elif chave < no.chave:
            return self._buscar(no.esquerda, chave)
        else:
            return self._buscar(no.direita, chave)

    def buscar(self, chave):
        return self._buscar(self.raiz, chave.lower())

    def _em_ordem(self, no, resultado):
        if no is not None:
            self._em_ordem(no.esquerda, resultado)
            resultado.append(no.valor)
            self._em_ordem(no.direita, resultado)

    def em_ordem(self):
        resultado = []
        self._em_ordem(self.raiz, resultado)
        return resultado

    def _pre_ordem(self, no, resultado):
        if no is not None:
            resultado.append(no.valor)
            self._pre_ordem(no.esquerda, resultado)
            self._pre_ordem(no.direita, resultado)

    def pre_ordem(self):
        resultado = []
        self._pre_ordem(self.raiz, resultado)
        return resultado

    def _pos_ordem(self, no, resultado):
        if no is not None:
            self._pos_ordem(no.esquerda, resultado)
            self._pos_ordem(no.direita, resultado)
            resultado.append(no.valor)

    def pos_ordem(self):
        resultado = []
        self._pos_ordem(self.raiz, resultado)
        return resultado

    def esta_vazia(self):
        return self.raiz is None


historico_clientes = []
historico_jogos = []
fila_prioridade = []

arvore_clientes = Arvore()
arvore_jogos = Arvore()


def cadastrar_cliente():
    nome = input("\nNome do cliente: ").strip()
    if not nome:
        print("Nome inválido.")
        return
    plano = input("Plano (VIP ou NORMAL): ").strip()
    if plano.lower() not in ("vip", "normal"):
        print("Plano inválido.")
        return
    arvore_clientes.inserir(nome, (nome, plano.upper()))
    fila_prioridade.append((nome, plano.upper()))
    print(f"Cliente '{nome}' cadastrado com sucesso!")


def buscar_cliente():
    if arvore_clientes.esta_vazia():
        print("Nenhum cliente cadastrado.")
        return
    nome = input("\nNome do cliente: ").strip()
    resultado = arvore_clientes.buscar(nome)
    if resultado:
        print(f"Cliente encontrado -> Nome: {resultado[0]} | Plano: {resultado[1]}")
    else:
        print("Cliente não encontrado.")


def editar_cliente():
    if arvore_clientes.esta_vazia():
        print("Nenhum cliente cadastrado.")
        return
    nome = input("\nNome do cliente que deseja editar: ").strip()
    if arvore_clientes.buscar(nome) is None:
        print("Cliente não encontrado.")
        return
    novo_nome = input("Novo nome: ").strip()
    novo_plano = input("Novo plano (VIP ou NORMAL): ").strip()
    if novo_plano.lower() not in ("vip", "normal"):
        print("Plano inválido.")
        return
    arvore_clientes.remover(nome)
    arvore_clientes.inserir(novo_nome, (novo_nome, novo_plano.upper()))
    indice = 0
    while indice < len(fila_prioridade):
        if fila_prioridade[indice][0].lower() == nome.lower():
            fila_prioridade[indice] = (novo_nome, novo_plano.upper())
            break
        indice += 1
    print("Cliente atualizado!")


def remover_cliente():
    if arvore_clientes.esta_vazia():
        print("Nenhum cliente cadastrado.")
        return
    nome = input("\nNome do cliente a remover: ").strip()
    valor = arvore_clientes.buscar(nome)
    if valor is None:
        print("Cliente não encontrado.")
        return
    arvore_clientes.remover(nome)
    historico_clientes.append(valor)
    indice = 0
    while indice < len(fila_prioridade):
        if fila_prioridade[indice][0].lower() == nome.lower():
            fila_prioridade.pop(indice)
            break
        indice += 1
    print(f"Cliente '{nome}' removido e salvo no histórico.")


def restaurar_cliente():
    if len(historico_clientes) == 0:
        print("Histórico de clientes vazio.")
        return
    ultimo = historico_clientes.pop()
    arvore_clientes.inserir(ultimo[0], ultimo)
    fila_prioridade.append(ultimo)
    print(f"Cliente '{ultimo[0]}' restaurado!")


def cadastrar_jogo():
    nome = input("\nNome do jogo: ").strip()
    if not nome:
        print("Nome inválido.")
        return
    status = input("Status (disponivel ou alugado): ").strip()
    if status.lower() not in ("disponivel", "disponível", "alugado"):
        print("Status inválido.")
        return
    arvore_jogos.inserir(nome, (nome, status.lower()))
    print(f"Jogo '{nome}' cadastrado com sucesso!")


def buscar_jogo():
    if arvore_jogos.esta_vazia():
        print("Nenhum jogo cadastrado.")
        return
    nome = input("\nNome do jogo: ").strip()
    resultado = arvore_jogos.buscar(nome)
    if resultado:
        print(f"Jogo encontrado -> Nome: {resultado[0]} | Status: {resultado[1]}")
    else:
        print("Jogo não encontrado.")


def editar_jogo():
    if arvore_jogos.esta_vazia():
        print("Nenhum jogo cadastrado.")
        return
    nome = input("\nNome do jogo que deseja editar: ").strip()
    if arvore_jogos.buscar(nome) is None:
        print("Jogo não encontrado.")
        return
    novo_nome = input("Novo nome: ").strip()
    novo_status = input("Novo status (disponivel ou alugado): ").strip()
    if novo_status.lower() not in ("disponivel", "disponível", "alugado"):
        print("Status inválido.")
        return
    arvore_jogos.remover(nome)
    arvore_jogos.inserir(novo_nome, (novo_nome, novo_status.lower()))
    print("Jogo atualizado!")


def remover_jogo():
    if arvore_jogos.esta_vazia():
        print("Nenhum jogo cadastrado.")
        return
    nome = input("\nNome do jogo a remover: ").strip()
    valor = arvore_jogos.buscar(nome)
    if valor is None:
        print("Jogo não encontrado.")
        return
    arvore_jogos.remover(nome)
    historico_jogos.append(valor)
    print(f"Jogo '{nome}' removido e salvo no histórico.")


def restaurar_jogo():
    if len(historico_jogos) == 0:
        print("Histórico de jogos vazio.")
        return
    ultimo = historico_jogos.pop()
    arvore_jogos.inserir(ultimo[0], ultimo)
    print(f"Jogo '{ultimo[0]}' restaurado!")


def particao(arr, esquerda, direita):
    pivo = arr[direita][0].lower()
    i = esquerda - 1
    for j in range(esquerda, direita):
        if arr[j][0].lower() <= pivo:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[direita] = arr[direita], arr[i + 1]
    return i + 1


def quicksort(arr, esquerda, direita):
    if esquerda < direita:
        pi = particao(arr, esquerda, direita)
        quicksort(arr, esquerda, pi - 1)
        quicksort(arr, pi + 1, direita)


def relatorio_clientes():
    print("\n==== RELATÓRIO DE CLIENTES ====")
    print("\n== Em Ordem ==")
    lista = arvore_clientes.em_ordem()
    if not lista:
        print("Nenhum cliente cadastrado.")
    else:
        for c in lista:
            print(f"  Nome: {c[0]} | Plano: {c[1]}")
    print("\n-- Pré-Ordem --")
    for c in arvore_clientes.pre_ordem():
        print(f"  Nome: {c[0]} | Plano: {c[1]}")
    print("\n-- Pós-Ordem --")
    for c in arvore_clientes.pos_ordem():
        print(f"  Nome: {c[0]} | Plano: {c[1]}")


def relatorio_jogos():
    print("\n==== RELATÓRIO DE JOGOS ====")
    print("\n== Em Ordem ==")
    lista = arvore_jogos.em_ordem()
    if not lista:
        print("Nenhum jogo cadastrado.")
    else:
        for j in lista:
            print(f"  Nome: {j[0]} | Status: {j[1]}")
    print("\n-- Pré-Ordem --")
    for j in arvore_jogos.pre_ordem():
        print(f"  Nome: {j[0]} | Status: {j[1]}")
    print("\n-- Pós-Ordem --")
    for j in arvore_jogos.pos_ordem():
        print(f"  Nome: {j[0]} | Status: {j[1]}")


def relatorio_jogos_ordenados():
    lista = arvore_jogos.em_ordem()
    if not lista:
        print("Nenhum jogo cadastrado.")
        return
    copia = list(lista)
    quicksort(copia, 0, len(copia) - 1)
    print("\n==== JOGOS ORDENADOS ====")
    for j in copia:
        print(f"  Nome: {j[0]} | Status: {j[1]}")


def relatorio_fila_prioridade():
    if not fila_prioridade:
        print("Fila de atendimento vazia.")
        return
    print("\n==== FILA DE PRIORIDADE ====")
    for c in fila_prioridade:
        if c[1] == "VIP":
            print(f"  [VIP]    {c[0]}")
    for c in fila_prioridade:
        if c[1] == "NORMAL":
            print(f"  [NORMAL] {c[0]}")


def relatorio_historico_clientes():
    if not historico_clientes:
        print("Histórico de clientes vazio.")
        return
    print("\n==== HISTÓRICO DE CLIENTES REMOVIDOS ====")
    for i in range(len(historico_clientes) - 1, -1, -1):
        print(f"  {i + 1}. Nome: {historico_clientes[i][0]} | Plano: {historico_clientes[i][1]}")


def relatorio_historico_jogos():
    if not historico_jogos:
        print("Histórico de jogos vazio.")
        return
    print("\n==== HISTÓRICO DE JOGOS REMOVIDOS ====")
    for i in range(len(historico_jogos) - 1, -1, -1):
        print(f"  {i + 1}. Nome: {historico_jogos[i][0]} | Status: {historico_jogos[i][1]}")


def filtrar_jogos_disponiveis():
    lista = arvore_jogos.em_ordem()
    disponiveis = []
    indice = 0
    while indice < len(lista):
        if lista[indice][1] in ("disponivel", "disponível"):
            disponiveis.append(lista[indice])
        indice += 1
    print("\n==== JOGOS DISPONÍVEIS ====")
    if not disponiveis:
        print("Nenhum jogo disponível.")
    else:
        for j in disponiveis:
            print(f"  Nome: {j[0]}")


while True:
    print("\n==== MENU ====")
    print("1 - Cadastro")
    print("2 - Buscar")
    print("3 - Editar")
    print("4 - Remover")
    print("5 - Relatórios")
    print("6 - Desfazer remoção")
    print("7 - Sair")
    print("================")

    escolha = int(input("Opção: "))

    match escolha:
        case 1:
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

        case 2:
            tipo = input("Buscar (cliente ou jogo): ").strip().lower()
            if tipo == "cliente":
                buscar_cliente()
            elif tipo == "jogo":
                buscar_jogo()
            else:
                print("Opção inválida.")

        case 3:
            tipo = input("Editar (cliente ou jogo): ").strip().lower()
            if tipo == "cliente":
                editar_cliente()
            elif tipo == "jogo":
                editar_jogo()
            else:
                print("Opção inválida.")

        case 4:
            tipo = input("Remover (cliente ou jogo): ").strip().lower()
            if tipo == "cliente":
                remover_cliente()
            elif tipo == "jogo":
                remover_jogo()
            else:
                print("Opção inválida.")

        case 5:
            while True:
                print("\n==== MENU RELATÓRIOS ====")
                print("1 - Clientes (travessias da árvore)")
                print("2 - Jogos (travessias da árvore)")
                print("3 - Jogos ordenados")
                print("4 - Fila de prioridade")
                print("5 - Histórico de clientes")
                print("6 - Histórico de jogos")
                print("7 - Filtrar jogos disponíveis")
                print("8 - Sair")

                escolha_relatorios = int(input("Opção: "))

                match escolha_relatorios:
                    case 1: 
                        relatorio_clientes()                 
                    case 2: 
                        relatorio_jogos()                      
                    case 3: 
                        relatorio_jogos_ordenados()                        
                    case 4: 
                        relatorio_fila_prioridade()                        
                    case 5: 
                        relatorio_historico_clientes()               
                    case 6: 
                        relatorio_historico_jogos()
                    case 7: 
                        filtrar_jogos_disponiveis()
                    case 8:
                        print("Saindo do menu relatorios...")
                        break
                    case _: print("Opção inválida.")

        case 6:
            tipo = input("Restaurar (cliente ou jogo): ").strip().lower()
            if tipo == "cliente":
                restaurar_cliente()
            elif tipo == "jogo":
                restaurar_jogo()
            else:
                print("Opção inválida.")

        case 7:
            print("Saindo do sistema.")
            break

        case _:
            print("Opção inválida.")