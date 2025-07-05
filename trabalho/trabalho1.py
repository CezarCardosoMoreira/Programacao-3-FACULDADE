"""
A. Deve-se implementar uma Lista Encadeada Simples em que: [EXIGÊNCIA DE CÓDIGO 1 de 7];
a. O Nodo representa um cartão numerado contendo: número, cor e um ponteiro para o próximo;
b. A lista é não circular, ou seja, seu último elemento aponta para nulo"""
class Nodo:

    #exigencia 1) ->  a: contém número, cor e um ponteiro para o próximo
    def __init__(self, numero, cor):
        self.numero = numero
        self.cor = cor
        self.proximo = None #exigencia 1) ->  b: último elemento aponta para nulo

class FilaDeAtendimento:


    def __init__(self):
        self.cabeça = None
        # Contadores para numeração automática dos cartões
        self.contador_v = 1  # Verde inicia em 1
        self.contador_a = 201  # Amarelo inicia em 201



    # E. Deve-se implementar a função imprimirListaEspera() em que: [EXIGÊNCIA DE CÓDIGO 5 de 7];
    # a. Deve-se imprimir todos os cartões e seus respectivos números a partir do primeiro até o último da lista



    # exigencia 5) implementar a função imprimirListaEspera()
    def imprimirListaEspera(self):

        # exigencia 5) a: Imprime todos os dados da lista de espera do iníco até o final
        print("-" * 30)
        print("FILA DE ESPERA ATUAL:")
        if self.cabeça is None:
            print("A fila está vazia.")
        else:
            no_atual = self.cabeça
            while no_atual:
                print(f"-> Cartão {no_atual.cor}{no_atual.numero}")
                no_atual = no_atual.proximo
        print("-" * 30)



#B. Deve-se implementar a função inserirSemPrioridade(nodo) em que: [EXIGÊNCIA DE CÓDIGO 2 de 7];
#a. Deve-se andar pela lista a partir da cabeça (head) e inserir o nodo no final da lista."""

    #exigencia 2) ->  a: Inicia apartir do head e adiciona no final da lista
    def inserirSemPrioridade(self, nodo):
        if self.cabeça is None:
            self.cabeça = nodo
        else:
            no_atual = self.cabeça
            # Percorre a lista até encontrar o último nó
            while no_atual.proximo:
                no_atual = no_atual.proximo
            # Adiciona o novo nó no final
            no_atual.proximo = nodo


    # C. Deve-se implementar a função inserirComPrioridade(nodo) em que: [EXIGÊNCIA DE CÓDIGO 3 de 7];
    # a. Deve-se andar pela lista a partir da cabeça (head) e inserir o nodo após todos os nodos com cor “A” que estão na lista.
    # b. O nodo inserido deve sempre estar antes de todos os nodos com cor “V”.


    # exigencia 3) implementar a função inserirComPrioridade
    def inserirComPrioridade(self, nodo):

        # exigencia 3) a:Percorrer lista apartir do HEAD
        # Verifica se estiva vazio ou se é Verde, se verdadeiro o Amarelo vira o primeiro
        if self.cabeça is None or self.cabeça.cor == 'V': # exigencia 3) b:nodo inserido deve sempre estar antes de todos os nodos com cor “V”
            nodo.proximo = self.cabeça
            self.cabeça = nodo
        else:
            # Procura na lista pelo último paciente com cartão Amarelo
            no_atual = self.cabeça
            while no_atual.proximo and no_atual.proximo.cor == 'A':
                no_atual = no_atual.proximo

            # Adiciona a lista o novo paciente Amarelo,  logo após o último Amarelo
            nodo.proximo = no_atual.proximo
            no_atual.proximo = nodo


    """ D. Deve-se implementar a função inserir() em que: [EXIGÊNCIA DE CÓDIGO 4 de 7]; 
     a. Deve-se solicitar ao usuário a cor (“A” ou “V”).
     b. A partir da cor, o número (inteiro) do paciente deve ser atribuído automaticamente seguindo a 
     ordem numérica. Por exemplo: o primeiro paciente “V” será o 1, o segundo 2, e assim por diante. 
     c. Deve-se criar um nodo com a cor e o número atribuído ao paciente. 
     d. Se a lista estiver vazia, a cabeça (head) da lista deve apontar para o nodo criado. 
     Senão, se a cor do nodo for “V”, deve-se chamar a função inserirSemPrioridade(nodo). 
     Senão, se a cor do nodo for “A”, deve-se chamar a função inserirComPriordade(nodo)."""

    # exigencia 4) : implementar a função inserir()
    def inserir(self):


        while True:
            #exigencia 4) a: Solicita cor ao usuário (A - Amarelo ou V - Verde)
            cor = input("Digite a cor do cartão (A - Amarelo / V - Verde): ").upper() #imput capturando do teclado a opção de cor do usuário
            if cor in ['A', 'V']: #verifica se foi digitado A ou V
                break
            else:
                #Caso cor seja diferente devolve erro de cor invalida e pede cor novamente
                print("Opção inválida. Por favor, digite 'A' ou 'V'.")

        #exigencia 4) b: contador automatico
        if cor == 'V':
            numero = self.contador_v
            self.contador_v += 1
        else:  # cor == 'A'
            numero = self.contador_a
            self.contador_a += 1

        #exigencia 4) c: Cria um nodo com a cor e o número
        novo_nodo = Nodo(numero, cor)
        print(f"Paciente com cartão {cor}{numero} adicionado à fila.")

        #exigencia 4) d: Decide onde inserir o nodo na lista
        if self.cabeça is None:
            self.cabeça = novo_nodo
        elif novo_nodo.cor == 'V':
            self.inserirSemPrioridade(novo_nodo)
        else:  # novo_nodo.cor == 'A'
            self.inserirComPrioridade(novo_nodo)


    #F. Deve-se implementar a função atenderPaciente() em que: [EXIGÊNCIA DE CÓDIGO 6 de 7];
    #a. Deve-se remover o primeiro paciente da fila e imprimir uma mensagem
    # chamando o paciente para atendimento informando o número do seu cartão.

    # exigencia 6) implementar a função atenderPaciente()
    def atenderPaciente(self):

        # exigencia 6) a:Remove o primeiro paciente da fila e imprime a mensagem de chamada.
        if self.cabeça is None:
            print("Não há pacientes na fila para atender.")
        else:
            paciente_chamado = self.cabeça
            self.cabeça = self.cabeça.proximo
            print("~" * 60)
            print(
                f"CHAMANDO PACIENTE: Cartão {paciente_chamado.cor}{paciente_chamado.numero} - DIRIGIR-SE AO CONSULTÓRIO 1")
            print("~" * 60)



"""
    G. Deve-se implementar um menu para utilização do sistema em que: [EXIGÊNCIA DE CÓDIGO 7 de 7];
    a. Deve-se apresentar as opções (1 – adicionar paciente a fila, 2 – mostrar pacientes na fila, 3 – chamar paciente, 4 – sair)

    b. Se escolhida a opção 1, chamar a função inserir().

    c. Se escolhida a opção 2, chamar a função imprimirListaEspera().

    d. Se escolhida a opção 3, chamar a função atenderPaciente().

    e. Se escolhida a opção 4, encerrar o programa.

    f. Se escolhida uma opção diferente as opções disponíveis, volte para o menu."""

# exigencia 7) implementar um menu para utilização do sistema
def menu_principal():
    """
    Apresenta o menu de opções e gerencia a interação do usuário com o sistema.
    """
    fila = FilaDeAtendimento()

    while True:

        # exigencia 7) a: Apresenta as opções
        print("\n--- SISTEMA DE TRIAGEM HOSPITALAR ---")
        print("1 – Adicionar paciente à fila")
        print("2 – Mostrar pacientes na fila")
        print("3 – Chamar próximo paciente")
        print("4 – Sair")

        opcao = input("Escolha uma opção: ")

        # exigencia 7) b: Se escolhida a opção 1, chamar a função inserir().
        if opcao == '1':
            fila.inserir()
        # exigencia 7) c: Se escolhida a opção 2, chamar a função imprimirListaEspera().
        elif opcao == '2':
            fila.imprimirListaEspera()
        # exigencia 7) d: Se escolhida a opção 3, chamar a função atenderPaciente().
        elif opcao == '3':
            fila.atenderPaciente()
        # exigencia 7) e: Se escolhida a opção 4, encerrar o programa.
        elif opcao == '4':
            print("Encerrando o sistema. Tenha um bom dia!")
            break
        # exigencia 7) f: Se escolhida uma opção diferente, volte para o menu.
        else:
            print("Opção inválida. Por favor, escolha uma opção de 1 a 4.")


# Inicia a execução do programa
if __name__ == "__main__":
    menu_principal()