#exigencia 2)implementação das Listas Encadeadas Simples
class Nodo:

    #exigencia 1) a: O Nodo representa um Estado contendo: sigla, nomeEstado e um ponteiro para o próximo.
    def __init__(self, sigla, nomeEstado):
        self.sigla = sigla
        self.nomeEstado = nomeEstado
        self.proximo = None


#exigencia 1)tabela Hash e suas funções
class TabelaHash:

    #Classe que implementa a Tabela Hash com endereçamento em cadeia.
    def __init__(self):
        """
        #exigencia 1) a: Construtor da Tabela Hash. Inicializa uma lista de 10 posições com None.
        """
        self.tamanho = 10
        self.tabela = [None] * self.tamanho

    #exigencia 5)implementação da função hash
    def funcao_hash(self, sigla):

        sigla = sigla.upper()

        if sigla == 'DF':
            return 7

        if len(sigla) == 2:
            char1_ascii = ord(sigla[0])
            char2_ascii = ord(sigla[1])
            return (char1_ascii + char2_ascii) % self.tamanho

        return 0

    #exigencia 3)inserção no início da lista encadeada
    def inserir(self, sigla, nomeEstado):

        #Insere um estado na tabela hash
        #da posição calculada (encadeamento).
        posicao = self.funcao_hash(sigla)
        novo_nodo = Nodo(sigla, nomeEstado)

        if self.tabela[posicao] is not None:
            novo_nodo.proximo = self.tabela[posicao]

        self.tabela[posicao] = novo_nodo

    #exigencia 4) Impressão da tabela hash
    def imprimir_tabela(self):

        #Imprime a Tabela Hash
        for i in range(self.tamanho):
            print(f"Posição {i}: ", end="")
            no_atual = self.tabela[i]
            if no_atual is None:
                print("-> None", end="")
            else:
                while no_atual:
                    print(f"-> [{no_atual.sigla}]", end=" ")
                    no_atual = no_atual.proximo
            print()


# --- INICIO ---
if __name__ == "__main__":

    # Cria a instância da Tabela Hash
    tabela_estados = TabelaHash()

    # ----SAÍDA DE CONSOLE 1----
    # Apresentar a tabela vazia
    print("---- Tabela Hash Inicial (Vazia) ---")
    tabela_estados.imprimir_tabela()
    print("-" * 45)

    #exigencia 6) inserção dos 27 estados
    estados_brasil = [
        ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'),
        ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'),
        ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')
    ]

    for sigla, nome in estados_brasil:
        tabela_estados.inserir(sigla, nome)

    # ----SAÍDA DE CONSOLE 2----
    # apresentar a tabela com 26 estados e o Distrito Federal
    print("\n----- Tabela Após Inserir os 27 Estados -----")
    tabela_estados.imprimir_tabela()
    print("-" * 45)

    #exigencia 7) Inserção do estado fictício

    tabela_estados.inserir('CZ', 'Cezar Moreira')

    # ----SAÍDA DE CONSOLE 3----
    # apresentar a tabela com 27 estados e o estado fictício
    print("\n------- Tabela Final com Estado Fictício ---------")
    tabela_estados.imprimir_tabela()
    print("-" * 45)