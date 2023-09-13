#5 traccia

#Dato l’elenco di 5000 romanzi in una libreria individuati da titolo, autore, genere e prezzo implementare
#le seguenti funzioni con variabili locali:
#1) caricare i dati di tutti i romanzi tramite la funzione 'carica' controllando che siano tutti di genere
#'fantascienza' o 'giallo' o 'narrativa'
#2) funzione 'media' che permette di calcolare la media dei prezzi dei romanzi con indice dispari,
#dopo aver ordinato i romanzi in ordine decrescente di prezzo. Tale media deve essere stampata
#nel main

class Libro:
    def __init__(self,titolo,autore,genere,prezzo):
        self.__titolo=titolo
        self.__autore=autore
        self.__genere=genere
        self.__prezzo=prezzo

    def set_titolo(self,titolo):
        self.__titolo=titolo
    def set_autore(self,autore):
        self.__autore=autore
    def set_genere(self,genere):
        self.__genere=genere
    def set_prezzo(self,prezzo):
        self.__prezzo=prezzo

    def get_titolo(self):
        return self.__titolo
    def get_autore(self):
        return self.__autore
    def get_genere(self):
        return self.__genere
    def get_prezzo(self):
        return self.__prezzo

    def __str__(self):
        return 'Titolo: ',+self.__titolo+'autore: '+self.__autore,\
               'genere: '+self.__genere+'prezzo: '+self.__prezzo

def main():
    N=int(input('inserire numero di romanzi: '))
    dict_libri=carica(N)
    lista_prezzi=ordina(dict_libri)
    for i in lista_prezzi:
        stampa_p=i.get_prezzo()
        print('stampa prezzo: ',stampa_p)
  
    somma=0
    indici_dispari=[]
    for i in lista_prezzi:
        if lista_prezzi.index(i)%2==1 and lista_prezzi.index(i)!=0:
            P=i.get_prezzo()
            print('P: ',P)
            indici_dispari.append(P)
            somma=somma+P
            print('somma: ',somma)
    print('lista indici dispari: ',indici_dispari)

    lun=len(indici_dispari)
    print('lunghezza: ',lun)
    media=somma/lun
    print('\nla media dei prezzi dei romanzi con indice dispari è: ',media)

def carica(n):
    dizionario={}
    tipologia=['giallo','narrativa','fantascienza']
    for i in range(n):
        print()
        genere=input('inserire genere del libro: ')
        while genere not in tipologia:
            print('genere non valido')
            genere=input('inserire uno dei seguenti generi: giallo,narrativa o fantascienza. ')
        titolo=input('inserire titolo del libro: ')
        autore=input('inserire autore: ')
        prezzo=int(input('inserire prezzo del libro: '))
        while prezzo<=0:
            print('prezzo non valido')
            prezzo=int(input('inserire il prezzzo corretto: '))

        m=Libro(titolo,autore,genere,prezzo)
        dizionario[titolo]=m

    return dizionario

def ordina(dizionario):
    prezzi=[]
    for key in dizionario:
        costo=dizionario.get(key)
        p=costo.get_prezzo()
        prezzi.append(costo)

    lun=len(prezzi)
    for i in range(lun-1):
        primo=prezzi[i]
        for j in range(i+1,lun):
            secondo=prezzi[j]
            if (primo.get_prezzo())<(secondo.get_prezzo()):
                temp=prezzi[i]
                prezzi[i]=prezzi[j]
                prezzi[j]=temp

    return prezzi
    
main()
                   
