#1 file
#Classe reperto con attributi: ID, luogo_ritrovamento, anno, mese, peso
#Caricare 3000 reperti. Cercare quello più vecchio del 14 secolo senza ordinamento
#Ordinare in maniera decrescente di peso e che provengono da pompei

class Reperto:
    def __init__(self,ID,luogo_ritrovamento,anno,mese,peso):
        self.__ID=ID
        self.__luogo_ritrovamento=luogo_ritrovamento
        self.__anno=anno
        self.__mese=mese
        self.__peso=peso

    def set_ID(self,ID):
        self.__ID=ID
    def set_luogo_ritrovamento(self,luogo_ritrovamento):
        self.__luogo_ritrovamento=luogo_ritrovamento
    def set_anno(self,anno):
        self.__anno=anno
    def set_mese(self,mese):
        self.__,mese=mese
    def set_peso(self,peso):
        self.__peso=peso

    def get_ID(self):
        return self.__ID
    def get_luogo_ritrovamento(self):
        return self.__luogo_ritrovamento
    def get_anno(self):
        return self.__anno
    def get_mese(self):
        return self.__mese
    def get_peso(self):
        return self.__peso

    def str__(self):
        return 'ID: '+self.__ID+'\nLuogo di ritrovamento: '+self.__luogo_ritrovamento,\
               'Anno: '+self.__anno+'Mese: '+self.__mese+'Peso: '+self.__peso

def main():
    N=int(input('inserire numero di reperti: '))
    #chiama la funzione che carica tutti i dati
    lista_reperti=carica(N)
    #cercare reperto più vecchio del 14° secolo
    print('\nreperto più vecchio del 14° secolo: ')
    for i in lista_reperti:
        if int((i.get_anno()))<14:
            print('Secolo: ',i.get_anno())
            print('ID: ',i.get_ID())
            print('luogo_ritrovamento: ',i.get_luogo_ritrovamento())
            print('mese: ',i.get_mese())
            print('peso: ',i.get_peso())
            print()
     #chiama la funzione che ordina in ordine decrescente di peso
    lista_ordinata=ordina(lista_reperti)
    print('reperti in ordine decrecente di peso che provengono da pompei: ')
    for i in lista_ordinata:
        if (i.get_luogo_ritrovamento())=='pompei' or (i.get_luogo_ritrovamento())=='Pompei':
            print('luogo_ritrovamento: ',i.get_luogo_ritrovamento())
            print('ID: ',i.get_ID())
            print('Secolo: ',i.get_anno())
            print('mese: ',i.get_mese())
            print('peso: ',i.get_peso())
            print()
            
            

def carica(n):
    lista=[]
    mesi=['gennaio','febbraio','marzo','aprile','maggio','giugno','luglio','agosto','settembre','ottobre','novembre','dicembre']
    for i in range(n):
        print()
        ID=int(input('inserire ID reperto n. '+str(i+1)+': '))
        while ID in lista:
            print('ID già presente')
            ID=int(input('inserire un altro ID: '))
        luogo_ritrovamento=input('inserire luogo di ritrovamento: ')
        anno=input('inserire secolo: ')
        mese=input('inserire mese: ')
        while mese not in mesi:
            print('mese non valido')
            mese=input('inserire un mese corretto: ')
        peso=int(input('inserire peso: '))

        m=Reperto(ID,luogo_ritrovamento,anno,mese,peso)
        lista.append(m)
        
    return lista

def ordina(lista):
    lun=len(lista)
    for i in range(lun-1):
        primo=lista[i]
        for j in range(i+1,lun):
            secondo=lista[j]
            if (primo.get_peso())<(secondo.get_peso()):
                temp=lista[i]
                lista[i]=lista[j]
                lista[j]=temp
                
    return lista

main()
        
