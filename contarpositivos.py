def contarpositivos(listadenumeros):
    contadordepositivos = 0
    for element in listadenumeros:
        if element > 0:
            contadordepositivos = contadordepositivos + 1
    ultimoindice = len(listadenumeros)-1
    listadenumeros[ultimoindice] = contadordepositivos
    print(listadenumeros)




contarpositivos([1,2,5,-1,-5])