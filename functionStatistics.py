import numpy as np
from scipy import stats

def calcular_estatisticas_indices(ndwi_OLI, ndci_OLI, ndssi_OLI, ndwi_MODIS, ndci_MODIS, ndssi_MODIS, localAndYear):
    # Lista de índices
    indices = [ndwi_OLI, ndci_OLI, ndssi_OLI, ndwi_MODIS, ndci_MODIS, ndssi_MODIS]

    # Lista para armazenar os resultados
    resultados = []

    for i, indice in enumerate(indices, start=1):
        # Remover valores zero
        indice_sem_zero = indice[indice != 0]

        # Calcular estatísticas para cada índice
        if len(indice_sem_zero) > 0:
            media = np.mean(indice_sem_zero)
            mediana = np.median(indice_sem_zero)
            moda = stats.mode(indice_sem_zero).mode[0]
            desvio_padrao = np.std(indice_sem_zero)
            variancia = np.var(indice_sem_zero)
        else:
            # Se todos os valores são zero, definir estatísticas como NaN
            media = mediana = moda = desvio_padrao = variancia = np.nan

        # Adicionar resultados à lista
        resultados.append({
            'indice': i,
            'localAndYear': f"{indice}_{localAndYear}",
            'media': media,
            'mediana': mediana,
            'moda': moda,
            'desvio_padrao': desvio_padrao,
            'variancia': variancia
        })

    return resultados

## Exemplo de uso
#localAndYear = "Linhares_2023"  # Substitua com o valor correto
#resultados = calcular_estatisticas_indices(ndwi_OLI, ndci_OLI, ndssi_OLI, ndwi_MODIS, ndci_MODIS, ndssi_MODIS, localAndYear)

## Imprimir os resultados
#for resultado in resultados:
#    print(f"Estatísticas para o índice {resultado['indice']} ({resultado['localAndYear']}):")
#    print(f"  Média: {resultado['media']}")
#    print(f"  Mediana: {resultado['mediana']}")
#    print(f"  Moda: {resultado['moda']}")
#    print(f"  Desvio Padrão: {resultado['desvio_padrao']}")
#    print(f"  Variância: {resultado['variancia']}")
#    print("\n")
