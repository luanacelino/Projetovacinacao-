# =====================================================
# CLASSE NÓ (Base da Lista Encadeada)
# =====================================================

class No:
    def __init__(self, valor):
        # O valor pode ser uma Pessoa (na fila)
        # ou um número de doses (na pilha)
        self.valor = valor

        # Ponteiro para o próximo nó
        self.proximo = None


# =====================================================
# CLASSE FILA (FIFO - First In, First Out)
# =====================================================

class Fila:
    def __init__(self):
        # Primeiro elemento da fila
        self.inicio = None

        # Último elemento da fila
        self.fim = None

        # Controla quantas pessoas estão na fila
        self.tamanho = 0

    # Adiciona pessoa no final da fila
    def enfileirar(self, valor):
        novo = No(valor)

        if self.esta_vazia():
            # Se estiver vazia, início e fim são o mesmo nó
            self.inicio = novo
            self.fim = novo
        else:
            # O antigo último aponta para o novo
            self.fim.proximo = novo
            self.fim = novo

        self.tamanho += 1

    # Remove a primeira pessoa da fila
    def desenfileirar(self):
        if self.esta_vazia():
            return None

        removido = self.inicio
        self.inicio = self.inicio.proximo

        # Se a fila ficar vazia
        if self.inicio is None:
            self.fim = None

        self.tamanho -= 1
        return removido.valor

    # Verifica se está vazia
    def esta_vazia(self):
        return self.inicio is None

    # Mostra todas as pessoas da fila
    def imprimir(self):
        if self.esta_vazia():
            print("Fila vazia!")
            return

        atual = self.inicio
        while atual:
            print(f"Nome: {atual.valor.nome} | CPF: {atual.valor.cpf}")
            atual = atual.proximo


# =====================================================
# CLASSE PILHA (LIFO - Last In, First Out)
# =====================================================

class Pilha:
    def __init__(self):
        # Topo da pilha
        self.topo = None
        self.tamanho = 0

    # Empilha um frasco
    def empilhar(self, valor):
        novo = No(valor)
        novo.proximo = self.topo
        self.topo = novo
        self.tamanho += 1

    # Desempilha um frasco
    def desempilhar(self):
        if self.esta_vazia():
            return None

        removido = self.topo
        self.topo = self.topo.proximo
        self.tamanho -= 1
        return removido.valor

    # Verifica se está vazia
    def esta_vazia(self):
        return self.topo is None

    # Retorna valor do topo sem remover
    def espiar(self):
        if self.esta_vazia():
            return None
        return self.topo.valor


# =====================================================
# CLASSE PESSOA
# =====================================================

class Pessoa:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf


# =====================================================
# INICIALIZAÇÃO DO SISTEMA
# =====================================================

fila = Fila()               # Fila começa vazia
pilha_frascos = Pilha()     # Pilha começa vazia
vacinados = []              # Lista para guardar nomes vacinados

# Empilha automaticamente 3 frascos com 5 doses cada
for i in range(3):
    pilha_frascos.empilhar(5)

# Contador de doses aplicadas
total_doses_aplicadas = 0


# =====================================================
# MENU PRINCIPAL
# =====================================================

while True:
    print("\n===== MENU =====")
    print("1 - Adicionar pessoa")
    print("2 - Imprimir Pessoas da Fila")
    print("3 - Imprimir quantas doses tem disponíveis")
    print("4 - Vacinar uma pessoa")
    print("5 - Exibir total de pessoas vacinadas")
    print("0 - Sair")

    opcao = input("Escolha: ")

    # -------------------------------------------------
    # 1 - ADICIONAR PESSOA
    # -------------------------------------------------
    if opcao == "1":

        # Não pode ter mais que 15 pessoas (15 doses no dia)
        if fila.tamanho >= 15:
            print("Fila cheia! Máximo de 15 pessoas por dia.")
        else:
            nome = input("Nome: ")
            cpf = input("CPF: ")

            pessoa = Pessoa(nome, cpf)
            fila.enfileirar(pessoa)

            print("Pessoa adicionada com sucesso!")

    # -------------------------------------------------
    # 2 - IMPRIMIR FILA
    # -------------------------------------------------
    elif opcao == "2":
        fila.imprimir()

    # -------------------------------------------------
    # 3 - MOSTRAR DOSES DISPONÍVEIS
    # -------------------------------------------------
    elif opcao == "3":
        print(f"Doses aplicadas: {total_doses_aplicadas}")
        print(f"Doses disponíveis: {15 - total_doses_aplicadas}")

    # -------------------------------------------------
    # 4 - VACINAR UMA PESSOA
    # -------------------------------------------------
    elif opcao == "4":

        if fila.esta_vazia():
            print("Não há pessoas na fila.")

        elif total_doses_aplicadas >= 15:
            print("Limite diário de 15 doses atingido!")

        else:
            # Remove a pessoa da fila
            pessoa = fila.desenfileirar()

            # Pega quantidade de doses do frasco atual
            doses_frasco_atual = pilha_frascos.espiar()

            # Aplica uma dose
            doses_frasco_atual -= 1
            total_doses_aplicadas += 1

            print(f"\nVacinando: {pessoa.nome} | CPF: {pessoa.cpf}")
            print(f"Dose número: {total_doses_aplicadas}")

            # Guarda nome na lista de vacinados
            vacinados.append(pessoa.nome)

            # Se o frasco acabou, desempilha
            if doses_frasco_atual == 0:
                pilha_frascos.desempilhar()
                print("Frasco finalizado!")
            else:
                # Atualiza número de doses no topo
                pilha_frascos.topo.valor = doses_frasco_atual

    # -------------------------------------------------
    # 5 - TOTAL DE VACINADOS
    # -------------------------------------------------
    elif opcao == "5":
        print(f"Total de pessoas vacinadas: {len(vacinados)}")

    # -------------------------------------------------
    # SAIR
    # -------------------------------------------------
    elif opcao == "0":
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida!")
