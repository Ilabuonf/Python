#traccia 2
#matrice e vettore

def main():
    M=int(input('inserire numero di righe della matrice: '))
    N=int(input('inserire numero di colonne della matrice: '))
    while M<8 or M>36:
        print('il numero di righe deve essere compreso tra 8 e 35')
        M=int(input('inserire numero di righe della matrice: '))
    while N<8 or N>36:
        print('il numero di colonne deve essere compreso tra 8 e 35')
        N=int(input('inserire numero di colonne della matrice: '))

    matrice=[[0 for i in range(N)] for j in range(M)]
    for i in range(N):       #ciclo sulle colonne
        for j in range(M):          #ciclo sulle righe
            matrice[j][i]=int(input('\ninserire valori per la matrice: '))
    print('\nla matrice è: ',matrice)

    vettore=[int(input('inserire valori per il vettore: ')) for i in range(N)]
    #prodotto righe per colonne quindi imposto che il vettore abbia la stessa dimensione delle righe
    print('\nil vettore è: ',vettore)

    prodotto=prod(matrice,vettore,N,M)
    print('\nil prodotto tra la matrice e il vettore è: ',prodotto)
    vett_ordinato=ordina(vettore)
    print('\nil vettore ordinato è: ',vett_ordinato)
    percentuale=perc(vett_ordinato)
    print('\nla percentuale dei valori superiori a 30 nei primi 7 valori più grandi del vettore è: ',percentuale)

def prod(mat,vet,n,m):
    p=0
    nuovo_vettore=[]
    for j in range(m):
        for i in range(n):
            p=p+mat[j][i]*vet[i]
        nuovo_vettore.append(p)
        p=0
    
    return nuovo_vettore

def ordina(vet):
    lun=len(vet)
    for i in range(lun-1):
        for j in range(i+1,lun):
            if vet[i]>vet[j]:
                temp=vet[i]
                vet[i]=vet[j]
                vet[j]=temp
    return vet

def perc(vet):
    conta=0
    lun=len(vet)
    for i in range(lun):            #6
        if vet[i]>30:
            conta=conta+1
    perc=(conta/lun)*100

    return perc

main()
            
    
    
