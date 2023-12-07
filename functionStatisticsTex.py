import numpy as np
from scipy import stats

def calcular_estatisticas_indices_tex(ndwi_OLI, ndci_OLI, ndssi_OLI, ndwi_MODIS, ndci_MODIS, ndssi_MODIS, localAndYear):
    # Lista de índices
    indices = [ndwi_OLI, ndci_OLI, ndssi_OLI, ndwi_MODIS, ndci_MODIS, ndssi_MODIS]

    # Mapeamento de rótulos para os índices
    rotulos = {
        1: "NDWI OLI",
        2: "NDCI OLI",
        3: "NDSSI OLI",
        4: "NDWI MODIS",
        5: "NDCI MODIS",
        6: "NDSSI MODIS",
    }

    # Lista para armazenar os resultados em formato LaTeX
    resultados_tex = []

    for i, indice in enumerate(indices, start=1):
        # Remover valores zero
        indice_sem_zero = indice[indice != 0]

        # Calcular estatísticas para cada índice
        if len(indice_sem_zero) > 0:
            media = np.round(np.mean(indice_sem_zero), 4)
            mediana = np.round(np.median(indice_sem_zero), 4)
            moda = np.round(stats.mode(indice_sem_zero).mode[0], 4)
            desvio_padrao = np.round(np.std(indice_sem_zero), 4)
            variancia = np.round(np.var(indice_sem_zero), 4)
        else:
            # Se todos os valores são zero, definir estatísticas como NaN
            media = mediana = moda = desvio_padrao = variancia = np.nan

        # Adicionar resultados à lista
        resultados_tex.append(
            f"      & \\multicolumn{{5}}{{c|}}{{{rotulos[i]} para {localAndYear}}} \\\\ \\hline\n"
            f"      & \\multicolumn{{1}}{{c|}}{{Média}} & \\multicolumn{{1}}{{c|}}{{Mediana}} & \\multicolumn{{1}}{{c|}}{{Moda}} "
            f"& \\multicolumn{{1}}{{c|}}{{Desvio Padrão}} & Variância \\\\ \\hline\n"
            f"OLI   & \\multicolumn{{1}}{{c|}}{{{media}}} & \\multicolumn{{1}}{{c|}}{{{mediana}}} & \\multicolumn{{1}}{{c|}}{{{moda}}} "
            f"& \\multicolumn{{1}}{{c|}}{{{desvio_padrao}}} & {variancia} \\\\ \\hline\n"
            f"MODIS & \\multicolumn{{1}}{{c|}}{{{media}}} & \\multicolumn{{1}}{{c|}}{{{mediana}}} & \\multicolumn{{1}}{{c|}}{{{moda}}} "
            f"& \\multicolumn{{1}}{{c|}}{{{desvio_padrao}}} & {variancia} \\\\ \\hline"
        )

    # Unir resultados em uma string única
    resultado_final_tex = "\n".join(resultados_tex)

    return resultado_final_tex

## Exemplo de uso
#localAndYear = "Linhares_2023"  # Substitua com o valor correto
#resultado_tex = calcular_estatisticas_indices_tex(ndwi_OLI_L14, ndci_OLI_L14, ndssi_OLI_L14, ndwi_MODIS_L14, ndci_MODIS_L14, ndssi_MODIS_L14, localAndYear)

## Imprimir o resultado em formato LaTeX
#print("\\begin{table}[]")
#print("\\begin{tabular}{|l|lllll|}")
#print("\\hline")
#print(resultado_tex)
#print("\\end{tabular}")
#print("\\end{table}")
