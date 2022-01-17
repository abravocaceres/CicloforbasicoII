def biggie_size(listadenumeros):
    for i in range(len(listadenumeros)):
        if listadenumeros[i] > 0:
            listadenumeros[i] = "big"
    print(listadenumeros)




biggie_size([-2,-6,7,4,-8])