convidados = []

def moreOne():
            maisUm = input('você gostaria de adicionar mais uma pessoa?[s/n] ')
            if maisUm == 'n':
                print("ESTA É A SUA LISTA DE CONVIDADOS!")
                print("---------------------------------")
                for x in convidados:
                    print(x)
            elif maisUm == 's':
                q = input('quem? ')
                convidados.append(q)
                moreOne()
                
def addconv():
    if not convidados:
        pri = input('Adcione a primeira pessoa na sua lista de convidados: ')
        convidados.append(pri)
        addconv()
    elif convidados:
        moreOne()
        
                
addconv()
