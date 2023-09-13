#simulazione 1

class Agenzia:
    def __init__(self,codice_univoco,indirizzo,città,prezzo):
        self.__codice_univoco=codice_univoco
        self.__indirizzo=indirizzo
        self.__città=città
        self.__prezzo=prezzo

    def set_codice_univoco(self,codice_univoco):
        self.__codice_univoco=codice_univoco
    def set_indirizzo(self,indirizzo):
        self.__indirizzo=indirizzo
    def set_città(self,città):
        self.__città=città
    def set_prezzo(self,prezzo):
        self.__prezzo=prezzo

    def get_codice_univoco(self):
        return self.__codice_univoco
    def get_indirizzo(self):
        return self.__indirizzo
    def get_città(self):
        return self.__città
    def get_prezzo(self):
        return self.__prezzo

    def __str__(self):
        return 'codice univoco: '+self.__codice_univoco+'\nindirizzo: '+self.__indirizzo,\
               '\ncittà: '+self.__città+'\nprezzo: '+self.__prezzo
    
AGGIUNGI_CASA=1
SALVA_CASA=2
MOSTRA_CASE=3
CERCA=4
ESCI=5
diz_case={}

def main():
    choice=get_menu_choice()
    while choice!=ESCI:
        if choice == AGGIUNGI_CASA:
            aggiungi()
        elif choice== SALVA_CASA:
            salva()
        elif choice == MOSTRA_CASE:
            mostra()
        elif choice == CERCA:
            cerca()
        else:
            print('esco dal programma')
            
        choice=get_menu_choice()

def get_menu_choice():
    print()
    print('menu: ')
    print('1) aggiungi una casa')
    print('2) salva case nel file di testo')
    print('3) mostra le case presenti nel file di testo')
    print('''4) cerca case all'interno di un range di prezzo''')
    print('5) esci dal programma')

    choice=int(input('inserire una scelta: '))
    while choice<AGGIUNGI_CASA or choice>ESCI:
        print('scelta non valida')
        choice=int(input('inserisci una scelta tra le presenti: '))

    return choice

def aggiungi():
    print()
    codice_univoco=input('inserisci codice univoco alfanumerico: ')
    while codice_univoco in diz_case:
        print('codice già esistente')
        codice_univoco=input('inserisci un altro codice: ')
    indirizzo=input('inserire indirizzo della casa: ')
    città=input('inserire città in cui si trova la casa: ')
    prezzo=float(input('inserire il prezzo della casa: '))
    while prezzo<=0:
        print('prezzo non valido')
        prezzo=int(input('inserire un prezzo corretto: '))

    c=Agenzia(codice_univoco,indirizzo,città,prezzo)
    diz_case[codice_univoco]=c

    return diz_case

def salva():
    #salva su file tesuale le case
    file=open('case.txt','w')
    for key in diz_case:
        file.write(str(diz_case[key].get_codice_univoco())+'\n')
        file.write(str(diz_case[key].get_indirizzo())+'\n')
        file.write(str(diz_case[key].get_città())+'\n')
        file.write(str(diz_case[key].get_prezzo())+'\n')
        file.write(str())
        
    file.close()
    print('''\ni dati sono stati salvati sul file di testo 'case.txt' ''')

def mostra():
    #stampa  a schermo il catalogo delle case gestite dall'agenzia immobiliare
    print('\necco tutte i dati delle case: ')
    for key in diz_case:
        print('\ndati: ')
        print('codice univoco: ',diz_case[key].get_codice_univoco())
        print('indirizzo: ',diz_case[key].get_indirizzo())
        print('città: ',diz_case[key].get_città())
        print('prezzo: ',diz_case[key].get_prezzo())
        print()

def cerca():
    #cerca le case all'interno di un range di prezzo
    print('''\nsi desidera cercare le case all'interno di un certo range di prezzo: ''')
    minimo=int(input('inserire un prezzo minimo '))
    massimo=int(input('inserire un prezzo massimo '))
    for key in diz_case:
        if diz_case[key].get_prezzo() >= minimo and diz_case[key].get_prezzo() <= massimo:
            print('\necco i dati: ')
            print('codice univoco: ',diz_case[key].get_codice_univoco())
            print('indirizzo: ',diz_case[key].get_indirizzo())
            print('città: ',diz_case[key].get_città())
            print('prezzo: ',diz_case[key].get_prezzo())
            print()
        else:
            print('''non ci sono case all'interno del range inserito''')
main()
