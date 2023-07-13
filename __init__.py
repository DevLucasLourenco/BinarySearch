class BinarySearch:
    """
    Realização de Buscas Binárias.\n
      Parâmetros
        ----------\n
            referencial : list or tuple
                Iterable onde será procurado a informação
            metodo : str
                existem três opções 'find', 'count', 'locate'\n
      Métodos
        ----------\n
            fetch(procura = x)
                Realiza a Busca Binária com o valor de x passado no parâmetro 'procura'

    """         

    def __init__(self, referencial:list, metodo:str = 'find'):
        self.opcoes_de_metodos = 'find', 'count', 'locate'
        self.metodo = BinarySearch.__if_item_in(metodo, self.opcoes_de_metodos).lower()
        self.referencial = sorted(referencial) # Ordena a lista, visto que a Busca Binária só será funcional caso a lista referida seja permutada.
        self.procura = None

    
    
    @staticmethod
    def __if_item_in(item, opcoes):

        if not item in opcoes:
            raise ValueError(f"Indicado: '{item}' | Opções: {opcoes}")
        return item


    def fetch(self, procura):
        self.procura = procura
        INDICE_MIN, INDICE_MAX = 0, len(self.referencial) - 1 # esqueda e direita
        

        class OpcoesMetodos(BinarySearch):
            op_find = self.opcoes_de_metodos[0]
            op_count = self.opcoes_de_metodos[1]
            op_locate = self.opcoes_de_metodos[2]


        match self.metodo:

            case OpcoesMetodos.op_find:
                resultado = self.__busca_binaria_find(INDICE_MIN, INDICE_MAX)
                return resultado

            case OpcoesMetodos.op_count:
                resultado = self.__busca_binaria_count(INDICE_MIN, INDICE_MAX)
                return resultado

            case OpcoesMetodos.op_locate:
                resultado = self.__busca_binaria_locate(INDICE_MIN, INDICE_MAX)
                return resultado


    # find
    def __busca_binaria_find(self, indice_esquerda, indice_direita):
        while (indice_esquerda <= indice_direita):
            meio = (indice_esquerda+indice_direita) // 2 # meio
            
            if (self.referencial[meio] == self.procura):
                return True
            
            elif (self.referencial[meio] > self.procura):
                indice_direita = meio-1

            else:
                indice_esquerda = meio+1
        
        return False


    # count
    def __busca_binaria_count(self, indice_esquerda, indice_direita):
        total = 0
        
        while (indice_esquerda <= indice_direita):
            meio = (indice_esquerda+indice_direita) // 2 # meio

            if (self.referencial[meio] == self.procura):
                total += 1
                i = meio+1

                while (i < len(self.referencial)) and (self.referencial[i] == self.procura):
                    total += 1
                    i += 1

                i = meio-1
                while (i >= 0) and (self.referencial[i] == self.procura):
                    total += 1
                    i -= 1

                return total
            

            elif (self.referencial[meio] > self.procura):
                indice_direita = meio-1

            else:
                indice_esquerda = meio+1

        return total


    # locate
    def __busca_binaria_locate(self, indice_esquerda, indice_direita):
        lista_auxiliar = list()
        
        while (indice_esquerda <= indice_direita):
            meio = (indice_esquerda+indice_direita) // 2 # meio

            if (self.referencial[meio] == self.procura):
                lista_auxiliar.append(meio)
                i = meio+1

                while (i < len(self.referencial)) and (self.referencial[i] == self.procura):
                    lista_auxiliar.append(i)
                    i += 1

                i = meio-1
                while (i >=  0) and (self.referencial[i] == self.procura):
                    lista_auxiliar.append(i)
                    i -= 1

                return lista_auxiliar
            

            elif (self.referencial[meio] > self.procura):
                indice_direita = meio-1

            else:
                indice_esquerda = meio+1

        return False




if __name__ == '__main__':
    lista = [1,5,5,5,15,17,20,24,67,76]
    res = BinarySearch(referencial=lista, metodo='find').fetch(5)
    
    print(res))
