class Linha:
    def __init__(self,tamanho):
        self.lista = self.create_list(tamanho)
    
    def create_list(tamanho):
        lista = []
        for i in range(tamanho):
            lista.append(' ')
        return lista

    def inserir(self, texto, inicio, final):
        j = 0
        for i in range(inicio, final):
            try:
                self.lista[i] = texto[j]
                j += 1
            except:
                break
    
    def inserir_pos(self, pos, item):
        self.lista[pos] = item
    
    def print(self):
        string = ''
        for i in self.lista:
            i = str(i)
            string += i
        print (string)
    
    def getLinha(self):
        return self.lista
