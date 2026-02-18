# -----------------------------
# Classe Nó (Lista Encadeada)
# -----------------------------
class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


# -----------------------------
# Classe Fila
# -----------------------------
class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def enfileirar(self, valor):
        novo = No(valor)
        if self.esta_vazia():
            self.inicio = novo
            self.fim = novo
        else:
            self.fim.proximo = novo
            self.fim = novo
        self.tamanho += 1

    def desenfileirar(self):
        if self.esta_vazia():
            return None
        removido = self.inicio
        self.inicio = self.inicio.proximo
        if self.inicio is None:
            self.fim = None
        self.tamanho -= 1
        return removido.valor

    def esta_vazia(self):
        return self.inicio is None

    def imprimir(self):
        atual = self.inicio
        while atual:
            print(f"Nome: {atual.valor.nome} | CPF: {atual.valor.cpf}")
            atual = atual.proximo


# -----------------------------
# Classe Pilha
# -----------------------------
class Pilha:
    def __init__(self):
        self.topo = None
        self.tamanho = 0

    def empilhar(self, valor):
        novo = No(valor)
        novo.proximo = self.topo
        self.topo = novo
        self.tamanho += 1

    def desempilhar(self):
        if self.esta_vazia():
            return None
        removido = self.topo
        self.topo = self.topo.proximo
        self.tamanho -= 1
        return removido.valor

    def esta_vazia(self):
        return self.topo is None

    def espiar(self):
        if self.esta_vazia():
            return None
        return self.topo.valor


# -----------------------------
# Classe Pessoa
# -----------------------------
class Pessoa:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf


# -----------------------------
# Inicialização do Sistema
# -----------------------------
fila = Fila()
pilha_frascos = Pilha()
vacinados = []

# Empilhar 3 frascos com 5 doses cada
for i in range(3):
    pilha_frascos.empilhar(5)

total_doses_aplicadas = 0


# -----------------------------
# Menu
# -----------------------------
while True:
    print("\n===== MENU =====")
    print("1 - Adicionar pessoa")
    print("2 - Imprimir Pessoas da Fila")
    print("3 - Imprimir quantas doses tem disponíveis")
    print("4 - Vacinar uma pessoa")
    print("5 - Exibir total de pessoas vacinadas")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        if fila.tamanho >= 15:
            print("Fila cheia! Máximo de 15 pessoas.")
        else:
            nome = input("Nome: ")
            cpf = input("CPF: ")
            pessoa = Pessoa(nome, cpf)
            fila.enfileirar(pessoa)
            print("Pessoa adicionada com sucesso!")

    elif opcao == "2":
        if fila.esta_vazia():
            print("Fila vazia!")
        else:
            fila.imprimir()

    elif opcao == "3":
        doses_restantes = total_doses_aplicadas
        print(f"Doses aplicadas: {total_doses_aplicadas}")
        print(f"Doses disponíveis: {15 - total_doses_aplicadas}")

    elif opcao == "4":
        if fila.esta_vazia():
            print("Não há pessoas na fila.")
        elif pilha_frascos.esta_vazia():
            print("Não há mais vacinas disponíveis.")
        else:
            pessoa = fila.desenfileirar()
            doses_frasco_atual = pilha_frascos.espiar()

            doses_frasco_atual -= 1
            total_doses_aplicadas += 1

            print(f"Vacinando: {pessoa.nome} | CPF: {pessoa.cpf}")
            print(f"Dose número: {total_doses_aplicadas}")

            vacinados.append(pessoa.nome)

            if doses_frasco_atual == 0:
                pilha_frascos.desempilhar()
                print("Frasco finalizado!")
            else:
                pilha_frascos.topo.valor = doses_frasco_atual

    elif opcao == "5":
        print(f"Total de pessoas vacinadas: {len(vacinados)}")

    elif opcao == "0":
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida!")
