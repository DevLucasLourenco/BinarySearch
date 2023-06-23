class BinarySearch:
    """
    Uma classe destinada à realização de Buscas Binárias.\n
      Parâmetros
        ----------\n
            referencial : list or tuple
                lista a qual será procurada a informação
            metodo : str
                existem três opções 'find', 'count', 'locate'\n
      Métodos
        ----------\n
            fetch(procura = x)
                Realiza a Busca Binária com o valor de x passado no parâmetro 'procura'

    """         

    def __init__(self, referencial:list, metodo:str = 'find'):
        self.opcoes_de_metodos = 'find', 'count', 'locate'
        self.metodo = BinarySearch.if_item_in(metodo, self.opcoes_de_metodos).lower()
        self.referencial = sorted(referencial) # Ordena a lista, visto que a Busca Binária só será funcional caso a lista referida seja permutada.
        self.procura = ...

    
    
    @staticmethod
    def if_item_in(item, opcoes):

        if not item in opcoes:
            raise ValueError(f"Indicado: '{item}' | Opções: {opcoes}")
        return item


    def fetch(self, procura):
        self.procura = procura
        INDICE_MIN, INDICE_MAX = 0, len(self.referencial) - 1 # esqueda e direita
        
        if self.metodo == self.opcoes_de_metodos[0]: # find
            resultado = self.__busca_binaria_find(INDICE_MIN, INDICE_MAX)

        
        elif self.metodo == self.opcoes_de_metodos[1]: # count
           resultado = self.__busca_binaria_count(INDICE_MIN, INDICE_MAX)


        elif self.metodo == self.opcoes_de_metodos[2]: # locate
           resultado = self.__busca_binaria_locate(INDICE_MIN, INDICE_MAX)

        return resultado


    # find
    def __busca_binaria_find(self, l, r):
        while (l <= r):
            meio = (l+r) // 2 # meio
            if (self.referencial[meio] == self.procura):
                return True
            
            elif (self.referencial[meio] > self.procura):
                r = meio-1

            else:
                l = meio+1

        return False


    # count
    def __busca_binaria_count(self, l, r):
        total = 0
        while (l <= r):
            meio = (l+r) // 2 # meio

            if (self.referencial[meio] == self.procura):
                total += 1
                i = meio+1

                while (i < len(self.referencial)) and self.referencial[i] == self.procura:
                    total += 1
                    i += 1

                i = meio-1
                while (i >=  0) and self.referencial[i] == self.procura:
                    total += 1
                    i -= 1

                return total
            

            elif (self.referencial[meio] > self.procura):
                r = meio-1

            else:
                l = meio+1

        return total


    # locate
    def __busca_binaria_locate(self, l, r):
        lista_auxiliar = list()
        while (l <= r):
            meio = (l+r) // 2 # meio

            if (self.referencial[meio] == self.procura):
                lista_auxiliar.append(meio)
                i = meio+1

                while (i < len(self.referencial)) and self.referencial[i] == self.procura:
                    lista_auxiliar.append(i)
                    i += 1

                i = meio-1
                while (i >=  0) and self.referencial[i] == self.procura:
                    lista_auxiliar.append(i)
                    i -= 1

                return lista_auxiliar
            

            elif (self.referencial[meio] > self.procura):
                r = meio-1

            else:
                l = meio+1

        return False




if __name__ == '__main__':
    lista = [1,5,5,5,15,17,20,24,67,76]
    
    app = BinarySearch(referencial=lista, metodo='find')
    x = app.fetch(5)
    print(x)

