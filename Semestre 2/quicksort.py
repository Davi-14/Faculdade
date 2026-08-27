lista = [19, 7, 1 ,3, 90, 5, 0, 10, 16, 67, 14]

def quicksort(arr, esquerda, direita):
    if esquerda < direita:
        pi = particao(arr, esquerda, direita)
        quicksort(arr, esquerda, pi-1)
        quicksort(arr, pi+1, direita)
        
def particao(arr, esquerda, direita):
    pivo = arr[direita]
    i = esquerda -1
    
    for j in range(esquerda, direita):
        if arr[j] <= pivo:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
            
    arr[i+1], arr[direita] = arr[direita], arr[i+1]
    return i+1
            
quicksort(lista, 0, len(lista)-1)

print(lista)