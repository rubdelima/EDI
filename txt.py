def showLines(txt):
    for i in txt:
        print(*i)

def loadTxt():
    with open('teste.txt', 'r') as txr:
        i = txr.read()
        i = i.splitlines()
        i = [j.split('=') for j in i]
        return i

def newTxt(table):
    with open('teste.txt', 'w') as txr:
        for linh in table:
            linh = "=".join(linh)
            print(linh, file=txr)

documento = loadTxt()
showLines(documento)
newTxt(documento)
documento = loadTxt()
showLines(documento)