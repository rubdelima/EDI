from funcoes import inserir


class Linha:
    def __init__(self,tamanho):
        self.lista = self.create_list(tamanho)
    
    def create_list(sel,tamanho):
        lista = []
        for i in range(tamanho):
            lista.append(' ')
        return lista

    def inserir(self, texto, inicio, final):
        texto = str(texto)
        j = 0
        for i in range(inicio, final):
            try:
                self.lista[i] = texto[j]
                j += 1
            except:
                break
    
    def inserir_pos(self, pos, item):
        item = str(item)
        self.lista[pos] = item
        
    def inserir2f(self, valor, inicio, final):
        texto = str(round(float(valor),2))
        self.inserir_fim(texto, inicio,final)
        
    
    def inserir_fim(self, texto, inicio, final, preencher='0'):
        texto = str(texto)
        preencher = str(preencher)
        if '.' in texto:
            texto = texto.replace('.', '')
        texto = preencher*((final-inicio)-len(list(texto))) + texto
        self.inserir(texto, inicio, final)
                
            
    
    def print(self):
        string = ''
        for i in self.lista:
            i = str(i)
            string += i
        print (string)
    
    def getLinha(self):
        return self.lista
    

