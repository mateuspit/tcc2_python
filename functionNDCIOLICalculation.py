import os
import rasterio
import numpy as np
from matplotlib import pyplot as plt

def calculate_ndci_OLI(caminho_b5, caminho_b4):
    with rasterio.open(caminho_b5) as src_b5, rasterio.open(caminho_b4) as src_b4:
        # Ler os dados das bandas como matrizes numpy
        b5 = src_b5.read(1).astype(float)
        b4 = src_b4.read(1).astype(float)

        # Calcular e imprimir o maior e o menor valor após a normalização
        print(f'--------------- BEGIN NDCI OLI CALCULATION')
        print(f'Max value in b5: {np.max(b5)}')
        if np.min(b5)==0:
            # Encontrar o menor valor em b5 maior que zero
            min_positive_b5 = np.min(b5[(b5 > 0)])
            # Exibir o menor valor presente em b5 maior que zero
            print(f'Min value in b5: {min_positive_b5}')
        else:
            print(f'Min value in b5: {np.min(b5)}')
        print(f'Max value in b4: {np.max(b4)}')
        if np.min(b4)==0:
            # Encontrar o menor valor em b4 maior que zero
            min_positive_b4 = np.min(b4[(b4 > 0)])
            # Exibir o menor valor presente em b4 maior que zero
            print(f'Min value in b4: {min_positive_b4}')
        else:
            print(f'Min value in b4: {np.min(b4)}')

        # Mostrar o número de elementos em b4
        print(f'Number of elements in b4: {np.size(b4)}')
        # Mostrar o número de elementos em b5
        print(f'Number of elements in b5: {np.size(b5)}')

        # Contar o número de elementos com valor 0 em b4
        num_zeros_b4 = np.count_nonzero(b4 == 0)
        print(f'Number of elements with value 0 in b4: {num_zeros_b4}')
        # Contar o número de elementos com valor 0 em b5
        num_zeros_b5 = np.count_nonzero(b5 == 0)
        print(f'Number of elements with value 0 in b5: {num_zeros_b5}')

        # Máscara para considerar apenas valores diferentes de zero em b5 e b4
        mask_nonzero = (b5 != 0) & (b4 != 0)

        # Calcular NDCI apenas para os valores não nulos em b5 e b4
        ndci = np.zeros_like(b5, dtype=float)
        ndci[mask_nonzero] = (b5[mask_nonzero] - b4[mask_nonzero]) / (b5[mask_nonzero] + b4[mask_nonzero])

        # Exibir o NDCI resultante
        if np.max(ndci) == 0:
            max_negative_ndci = np.max(ndci[ndci < 0]) 
            print(f'Max value in ndci: {max_negative_ndci}')
        else:
            print(f'Max value in ndci: {np.max(ndci)}')
        # Encontrar o menor valor em ndci maior que zero
        if np.min(ndci)==0:
            min_positive_ndci = np.min(ndci[(ndci > 0)])
        else:
            min_positive_ndci = np.min(ndci)
        # Exibir o menor valor presente em ndci maior que zero
        print(f'Min value in ndci: {min_positive_ndci}')

        # Nome da pasta anterior (pasta pai) à pasta onde a imagem será salva
        folder_name = os.path.basename(os.path.abspath(os.path.join(os.path.dirname(caminho_b4), os.pardir)))
        
        # Caminho para o diretório do arquivo de origem
        output_directory = os.path.abspath(os.path.join(os.path.dirname(caminho_b4), os.pardir))
        
        # Caminho completo para o arquivo de saída do gráfico
        output_graph_path = os.path.join(output_directory, f'ndci_oli_graph_{folder_name}.png')

        # Exibir o NDCI
        plt.imshow(ndci, cmap='RdYlGn', vmin=-1, vmax=1)
        plt.colorbar(label='NDCI')
        plt.title('Índice de Concentração de Deoxirribonucleico (NDCI)')
        plt.savefig(output_graph_path)
        plt.show()
        print(f"Gŕafico NDCI salvo em {output_graph_path}")
        print(f'--------------- END NDCI OLI CALCULATION')

        return ndci