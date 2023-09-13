#traccia 1
#festival del Cinema

class Film:
    def __init__(self,codice,titolo,regista,nazione,ore,minuti,punteggio):
        self.__codice=codice
        self.__titolo=titolo
        self.__regista=regista
        self.__nazione=nazione
        self.__ore=ore
        self.__minuti=minuti
        self.__punteggio=punteggio

    def set_codice(self,codice):
        self.__codice=codice
    def set_titolo(self,titolo):
        self.__titolo=titolo
    def set_regista(self,regista):
        self.__regista=regista
    def set_nazione(self,nazione):
        self.__nazione=nazione
    def set_ore(self,ore):
        self.__ore=ore
    def set_minuti(self,minuti):
        self.__minuti=minuti
    def set_punteggio(self,punteggio):
        self.__punteggio=punteggio

    def get_codice(self):
        return self.__codice
    def get_titolo(self):
        return self.__titolo
    def get_regista(self):
        return self.__regista
    def get_nazione(self):
        return self.__nazione
    def get_ore(self):
        return self.__ore
    def get_minuti(self):
        return self.__minuti
    def get_punteggio(self):
        return self.__punteggio

    def __str__(self):
        return 'Codice: '+self.__codice+'\ntitolo: '+self.__titolo+'\nregista: '+self.__regista,\
               '\nazione: '+self.__nazione+'\nore: '+self.__ore+'\nminuti: '+self.__minuti,\
               '\npunteggio: '+self.__punteggio

def main():
    N=input('inserire numero di Film: ') #70
    if_integer(N)
    while not if_integer(N):
        N=input('inserire un altro valore: ')
    if int(N)>70:
        N=input('i film in gara sono 70, reinserire il numero: ')
    lista_film=carica(int(N))
    lista_ordinata=ordina(lista_film)

    print('\nEcco i primi 3 film francesi: ')
    for i in lista_ordinata:
        if i.get_nazione()=='francia' or i.get_nazione()=='Francia':
            print('codice: ',i.get_codice())
            print('titolo: ',i.get_titolo())
            print('regista: ',i.get_regista())
            print('ore: ',i.get_ore())
            print('minuti: ',i.get_minuti())
            print('punteggio: ',i.get_punteggio())
            print()

## Controlla carattere per carattere se è numerico
def if_integer(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

#funzione per il caricamento dei dati di tutti i film
def carica(n):
    lista=[]
    for i in range(n):
        print()
        
        codice=input('inserire codice del film: ')
        while codice in lista:
            print('codice già esistente')
            codice=input('inserire un altro codice: ')
            
        titolo=input('inserire titolo del film: ')
        regista=input('inserire regista del film: ')
        nazione=input('inserire la nazione: ')
        
        ore=input('inserire la durata in ore: ')
        while not if_integer(ore):
            ore=input('inserisci un altro valore: ')
        while int(ore)<0 or int(ore)>23:
            print('ore non valide ')
            ore=int(input('inserire la durata in ore: '))
            
        minuti=input('inserire la durata in minuti: ')
        while not if_integer(minuti):
            minuti=input('inserisci un altro valore: ')
        while int(minuti)<0 or int(minuti) >60:
            print('minuti non validi')
            minuti=int(input('inserire la durata in minuti: '))
            
        punteggio=input('inserire il punteggio ottenuto: ')
        while not if_integer(punteggio):
            punteggio=input('inserire un altro valore')
        while int(punteggio)<0 or int(punteggio) >100:
            print('punteggio non valido')
            punteggio=float(input('inserire il punteggio ottenuto: '))

        m=Film(codice,titolo,regista,nazione,ore,minuti,punteggio)
        lista.append(m)
        
    return lista

#funzione che ordina la lista in ordine decrescente di punteggio
def ordina(lista):
    lun=len(lista)
    for i in range(lun-1):
        primo=lista[i]
        for j in range(i+1,lun):
            secondo=lista[j]
            if (primo.get_punteggio())<(secondo.get_punteggio()):
                temp=lista[i]
                lista[i]=lista[j]
                lista[j]=temp
    return lista

main()
            
        
