import sys

def calculalona(hh):
    n = len(hh)
    hist_esquerda = []
    hist_direita = []
    print('\n')
    print(hh)

    major = 0
    #Primeira passada: historicos de maximo da esquerda pra direita
    for h in hh:
        if h > major:
            major = h
        hist_esquerda.append(major)
    print(hist_esquerda)

    major = 0
    #Segunda passada: historicos de maximo da direita pra esquerda
    for h in reversed(hh):
        if h > major:
            major = h
        hist_direita.append(major)
    hist_direita = list(reversed(hist_direita))
    print(hist_direita)

    solucao = sys.maxsize
    # Terceira passada: calcular a solucao
    for i in range(n+1):
        # Corner case 1: apenas uma lona, a da direita
        if i == 0:
            lona_direita = n * hist_direita[i]
            if lona_direita < solucao:
                solucao = lona_direita
            print(f"Partindo em {i}, achei {lona_direita}")
        # Corner case 2: apenas uma lona, a da esquerda
        elif i == n:
            lona_esquerda = n * hist_esquerda[i-1]
            if lona_esquerda < solucao:
                solucao = lona_esquerda
            print(f"Partindo em {i}, achei {lona_esquerda}")
        else:
            lona_esquerda = i * hist_esquerda[i-1]
            lona_direita = (n - i) * hist_direita[i]
            duas_lonas = lona_esquerda + lona_direita
            if duas_lonas < solucao:
                solucao = duas_lonas
            #print(f"Partindo em {i}, achei {lona_esquerda} + {lona_direita}")
            print(f"Partindo em {i}, achei {lona_esquerda+lona_direita}")

    return solucao


if __name__ == '__main__':

    H = [3, 1, 4]
    print("Esperado: 10 - Calculado: ", calculalona(H))
    H = [5, 3, 2, 4]
    print("Esperado: 17 - Calculado: ", calculalona(H))
    H = [5, 3, 5, 2, 1]
    print("Esperado: 19 - Calculado: ", calculalona(H))
    H = [7, 7, 3, 7, 7]
    print("Esperado: 35 - Calculado: ", calculalona(H))
    H = [1, 1, 7, 6, 6, 6]
    print("Esperado: 30 - Calculado: ", calculalona(H))









