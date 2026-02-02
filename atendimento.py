class Nodo:
    def __init__(self, numero, prioridade):
        self.numero = numero
        self.prioridade = prioridade
        self.proximo = None

class ListaLigada:
    def __init__(self):
        self.head = None

    def inserir(self, nodo):
        if self.head is None or (nodo.prioridade == 'P' and self.head.prioridade == 'C'):
            nodo.proximo = self.head
            self.head = nodo
        else:
            atual = self.head
            while atual.proximo and not (nodo.prioridade == 'P' and atual.proximo.prioridade == 'C') and \
                  not (nodo.prioridade == atual.proximo.prioridade and nodo.numero < atual.proximo.numero):
                atual = atual.proximo
            nodo.proximo = atual.proximo
            atual.proximo = nodo

    def mostrar_fila(self):
        atual = self.head
        print("\n--- FILA ATUAL ---")
        while atual:
            print(f"Prioridade: {atual.prioridade} | Senha: {atual.numero}")
            atual = atual.proximo
        print("------------------\n")

# Menu Interativo
fila = ListaLigada()
while True:
    print("1. Adicionar cliente")
    print("2. Mostrar fila")
    print("3. Sair")
    op = input("Opção: ")
    if op == '1':
        num = int(input("Número da senha: "))
        prio = input("Prioridade (P/C): ").upper()
        fila.inserir(Nodo(num, prio))
    elif op == '2':
        fila.mostrar_fila()
    elif op == '3':
        break