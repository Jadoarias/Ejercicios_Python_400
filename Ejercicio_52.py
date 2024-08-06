def Histograma(texto):
    histo = {}
    for i in texto:
        if i in histo:
            histo[i] +=1
        else:
            histo[i] = 1
    print(histo)

Histograma('abracadabra')