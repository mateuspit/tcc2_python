import os
import rasterio
import numpy as np
from matplotlib import pyplot as plt

def calculate_ndci_MODIS(caminho_b1, caminho_b2):
    with rasterio.open(caminho_b1) as src_b2, rasterio.open(caminho_b2) as src_b1:
        # Ler os dados das bandas como matrizes numpy
        b2 = src_b2.read(1).astype(float)
        b1 = src_b1.read(1).astype(float)

        # Calcular e imprimir o maior e o menor valor após a normalização
        print(f'--------------- BEGIN NDCI MODIS CALCULATION')

        # Encontrar o maior valor em b2
        print(f'Max value in b2: {np.max(b2)}')
        # Encontrar o menor valor em b2, valores com 0 não contam
        min_b2 = np.min(b2[(b2 > 0)])
        print(f'Min value in b2: {min_b2}')


        # Encontrar o maior valor em b1
        print(f'Max value in b1: {np.max(b1)}')
        # Encontrar o menor valor em b1, valores com 0 não contam
        min_b1 = np.min(b1[(b1 > 0)])
        print(f'Min value in b1: {min_b1}')

        # Mostrar o número de elementos em b1
        print(f'Number of elements in b1: {np.size(b1)}')
        # Mostrar o número de elementos em b2
        print(f'Number of elements in b2: {np.size(b2)}')

        # Contar o número de elementos com valor 0 em b1
        num_zeros_b1 = np.count_nonzero(b1 == 0)
        print(f'Number of elements with value 0 in b1: {num_zeros_b1}')
        # Contar o número de elementos com valor 0 em b2
        num_zeros_b2 = np.count_nonzero(b2 == 0)
        print(f'Number of elements with value 0 in b2: {num_zeros_b2}')

        # Máscara para considerar apenas valores diferentes de zero em b2 e b1
        mask_nonzero = (b2 != 0) & (b1 != 0)

        # Calcular NDCI apenas para os valores não nulos em b2 e b1
        ndci = np.zeros_like(b2, dtype=float)
        ndci[mask_nonzero] = (b2[mask_nonzero] - b1[mask_nonzero]) / (b2[mask_nonzero] + b1[mask_nonzero])

        # Exibir o NDCI resultante
        # Encontrar o maior valor em ndci maior que zero
        if np.max(ndci)==0:
            max_ndci = np.max(ndci[(ndci < 0)])
        else:
            max_ndci = np.max(ndci)
        # Exibir o maior valor presente em ndci maior que zero
        print(f'Max value in ndci: {max_ndci}')

        # Encontrar o menor valor em ndci maior que zero
        if np.min(ndci)==0:
            min_ndci = np.min(ndci[(ndci > 0)])
        else:
            min_ndci = np.min(ndci)
        # Exibir o menor valor presente em ndci maior que zero
        print(f'Min value in ndci: {min_ndci}')

        # Nome da pasta anterior (pasta pai) à pasta onde a imagem será salva
        folder_name = os.path.basename(os.path.abspath(os.path.join(os.path.dirname(caminho_b1), os.pardir)))
        
        # Caminho para o diretório do arquivo de origem
        output_directory = os.path.abspath(os.path.join(os.path.dirname(caminho_b1), os.pardir))
        
        # Caminho completo para o arquivo de saída do gráfico
        output_graph_path = os.path.join(output_directory, f'ndci_modis_graph_{folder_name}.png')

        # Exibir o NDCI
        plt.imshow(ndci, cmap='RdYlGn', vmin=-1, vmax=1)
        plt.colorbar(label='NDCI')
        plt.title('Índice de Clorofila Normalizado (NDCI)')
        plt.savefig(output_graph_path)
        plt.show()
        print(f"Gŕafico NDCI salvo em {output_graph_path}")
        print(f'--------------- END NDCI MODIS CALCULATION')

        return ndci