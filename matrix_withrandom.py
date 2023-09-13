#2 file
#matrice A 15x20 con solo numeri pari e matrice B 17x13 solo multipli di 5
#annullare tutte le celle della matrice A multiple di 4
#trovare l'indice della colonna della matrice B con somma minore

import random

def main():
    rA=15
    cA=20
    rB=17
    cB=13

    #funzione che crea le matrici A e B
    matriceA,matriceB=crea_mat(rA,cA,rB,cB)
    print('\nla matrice A è: ',matriceA)
    print('\nla matrice B è: ',matriceB)

    #funzione che annulla le celle della matrice A multiple di 4
    new_matriceA=annulla_celle(matriceA,rA,cA)
    print('\nla matrice A priva di multipli di 4 è: ',new_matriceA)

    #trova l'indice della colonna della matrice B con somma minore
    min_index=colonne(matriceB,rB,cB)
    print('''\nl'indice della colonna della matrice B con somma minore è: ''',min_index)

def crea_mat(r1,c1,r2,c2):
    #la matrice A deve contenere numeri pari
    print('\nla matrice A deve essere formata da numeri pari')
    mat1=[[0 for j in range(c1)] for i in range(r1)]
    for i in range(r1):
        for j in range(c1):
            n=random.randint(1,100)
            while n==0 or n%2!=0:
                #print('il numero non è pari')
                n=random.randint(1,100)
            mat1[i][j]=n

    #la matrice B deve contenere multipli di cinque
    print('\nla matrice B deve essere formata solo da multipli di 5')
    mat2=[[0 for j in range(c2)]for i in range(r2)]
    for i in range(r2):
        for j in range(c2):
            n=random.randint(1,100)
            while n==0 or n%5!=0:
                #print('numero non multiplo di 5')
                n=random.randint(1,100)
            mat2[i][j]=n

    return mat1,mat2

def annulla_celle(mat1,r1,c1):
    for i in range(r1):
        for j in range(c1):
            if mat1[i][j]%4==0:
                mat1[i][j]=0
                
    return mat1

def colonne(mat2,r2,c2):
    dizionario={}
    for j in range(c2):
        somma=0
        for i in range(r2):
            somma=somma+mat2[i][j]
        print('la somma della colonna ',(j+1),' é: ', somma)
        dizionario[j]=somma

    minimo=dizionario[0]
    min_col=0
    for j in range(c2):
        for i in range(r2):
            while dizionario[j]<dizionario[0]:
                minimo=dizionario[j]
                min_col=j
    
    return min_col

main()
