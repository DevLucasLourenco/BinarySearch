class BuscaBinaria:

    def __init__(self, lista_referencial: list, procura: object, metodo='find'):
        self.opcoes_de_metodos = 'find', 'count', 'locate'
        self.metodo = BuscaBinaria.if_item_in(metodo, self.opcoes_de_metodos)
        self.lista_referencial = sorted(lista_referencial) # Ordena a lista, visto que a Busca Binária só será funcional caso a lista referida seja permutada.
        self.procura = procura


    @staticmethod
    def if_item_in(item, opcoes):

        if not item in opcoes:
            raise ValueError(f"Indicado: '{item}' | Opções: {opcoes}")
        return item


    def fetch(self):
        left, right = 0, len(self.lista_referencial) - 1 # esqueda e direita
        
        if self.metodo == self.opcoes_de_metodos[0]: # find
            resultado = self.__busca_binaria_find(left, right)

        
        elif self.metodo == self.opcoes_de_metodos[1]: # count
           resultado = self.__busca_binaria_count(left, right)


        elif self.metodo == self.opcoes_de_metodos[2]: # locate
           resultado = self.__busca_binaria_locate(left, right)

        return resultado


    # find
    def __busca_binaria_find(self, l, r):
        while (l <= r):
            meio = (l+r) // 2 # meio
            if (self.lista_referencial[meio] == self.procura):
                return True
            
            elif (self.lista_referencial[meio] > self.procura):
                r = meio-1

            else:
                l = meio+1

        return False


    # count
    def __busca_binaria_count(self, l, r):
        total = 0
        while (l <= r):
            meio = (l+r) // 2 # meio

            if (self.lista_referencial[meio] == self.procura):
                total += 1
                i = meio+1

                while (i < len(self.lista_referencial)) and self.lista_referencial[i] == self.procura:
                    total += 1
                    i += 1

                i = meio-1
                while (i >=  0) and self.lista_referencial[i] == self.procura:
                    total += 1
                    i -= 1

                return total
            

            elif (self.lista_referencial[meio] > self.procura):
                r = meio-1

            else:
                l = meio+1

        return total


    # locate
    def __busca_binaria_locate(self, l, r):
        lista_auxiliar = list()
        while (l <= r):
            meio = (l+r) // 2 # meio

            if (self.lista_referencial[meio] == self.procura):
                lista_auxiliar.append(meio)
                i = meio+1

                while (i < len(self.lista_referencial)) and self.lista_referencial[i] == self.procura:
                    lista_auxiliar.append(i)
                    i += 1

                i = meio-1
                while (i >=  0) and self.lista_referencial[i] == self.procura:
                    lista_auxiliar.append(i)
                    i -= 1

                return lista_auxiliar
            

            elif (self.lista_referencial[meio] > self.procura):
                r = meio-1

            else:
                l = meio+1

        return False




if __name__ == '__main__':
    lista = [1,5,5,5,15,17,20,24,67,76]

    app = BuscaBinaria(metodo='find', lista_referencial=lista, procura=5)
    x = app.fetch()
    print(x)


