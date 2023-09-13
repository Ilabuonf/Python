#3
#treni stazione di bari

class Treni:
    def __init__(self,targa,denominazione,tipo_locomotiva,ore,minuti,num_passeggeri):
        self.__targa=targa
        self.__denominazione=denominazione
        self.__tipo_locomotiva=tipo_locomotiva
        self.__ore=ore
        self.__minuti=minuti
        self.__num_passeggeri=num_passeggeri

    def set_targa(self,targa):
        self.__targa=targa
    def set_denominazione(self,denominazione):
        self.__denominazione=denominazione
    def set_tipo_locomotiva(self,tipo_locomotiva):
        self.__tipo_locomotiva=tipo_locomotiva
    def set_ore(self,ore):
        self.__ore=ore
    def set_minuti(self,minuti):
        self.__minuti=minuti
    def set_num_passeggerii(self,num_passeggeri):
        self.__num_passeggeri=num_passeggeri

    def get_targa(self):
        return self.__targa
    def get_denominazione(self):
        return self.__denominazione
    def get_tipo_locomotiva(self):
        return self.__tipo_locomotiva
    def get_ore(self):
        return self.__ore
    def get_minuti(self):
        return self.__minuti
    def get_num_passeggeri(self):
        return self.__num_passeggeri


    def __str__(self):
        return 'targa: '+self.__targa+'denominazione; '+self.__denominazione,\
               'tipo di locomotiva: '+self.__tipo_locomotiva+'ore: '+self.__ore,\
               'minuti: '+self.__minuti+'numero di passeggeri: '+self.__num_passeggeri

def main():
    N=int(input('inserire numero di treni: ' ))
    dict_treni=carica(N)
    M=int(input('inserire numero di cui si vuole calcola la media dei primi X treni: '))
    primi_M=ordina(dict_treni,M)

    somma=0
    for i in primi_M:
        n_passeggeri=i.get_num_passeggeri()
        somma=somma+n_passeggeri
        
    media=somma/M
    print('\nla media dei primi ',M,' treni è: ',media)

def carica(n):
    dizionario={}
    for i in range(n):
        print()
        targa=input('inserire targa: ')
        while targa in dizionario:
            print('targa già esistente')
            targa=input('reinserire targa: ')
        denominazione=input('inserire denominazione: ')
        tipo_locomotiva=input('inserire tipo di locomotiva: ')
        ore=int(input('inserire orario di partenza in ore: '))
        while ore<0 or ore>23:
            print('ora non valida')
            ore=int(input('inserire ora corretta: '))
        minuti=int(input('inserire orario di partenza in minuti: '))
        while minuti<0 or minuti>59:
            print('minuti non validi')
            minuti=int(input('inserire orario di partenza in minuti corretto: '))
        num_passeggeri=int(input('inserisci numero di passeggeri: '))
        while num_passeggeri<=0:
            print('numero non valido')
            num_passeggeri=int(input('reinserire numero di passeggeri: '))

        m=Treni(targa,denominazione,tipo_locomotiva,ore,minuti,num_passeggeri)
        dizionario[targa]=m

    return dizionario

def ordina(dizionario,m):
    orario=[]
    for key in dizionario:
        time=dizionario.get(key)
        h=time.get_ore()
        m=time.get_minuti()
        orario.append(time)

    lun=len(orario)
    for i in range(lun-1):
        primo=orario[i]
        for j in range(i+1,lun):
            secondo=orario[j]
            if (primo.get_ore())<(secondo.get_ore()):
                if (primo.get_minuti())<(secondo.get_minuti()):
                    temp=orario[i]
                    orario[i]=orario[j]
                    orario[j]=temp

    primi_m=orario[:(m-1)]
    return primi_m
                    
main()
            
