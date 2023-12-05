import os
import rasterio
import numpy as np
from matplotlib import pyplot as plt

def calculate_ndwi_OLI(caminho_b3, caminho_b5):
    with rasterio.open(caminho_b3) as src_b3, rasterio.open(caminho_b5) as src_b5:
        # Ler os dados das bandas como matrizes numpy
        b3 = src_b3.read(1).astype(float)
        b5 = src_b5.read(1).astype(float)

        # Calcular e imprimir o maior e o menor valor em b3
        print(f'--------------- BEGIN NDWI OLI CALCULATION')

        # Encontrar o maior valor em b3
        print(f'Max value in b3: {np.max(b3)}')
        # Encontrar o menor valor em b3, valores com 0 não contam
        min_b3 = np.min(b3[(b3 > 0)])
        print(f'Min value in b3: {min_b3}')

        # Encontrar o maior valor em b5
        print(f'Max value in b5: {np.max(b5)}')
        # Encontrar o menor valor em b5, valores com 0 não contam
        min_b5 = np.min(b5[(b5 > 0)])
        print(f'Min value in b5: {min_b5}')

        # Mostrar o número de elementos em b3
        print(f'Number of elements in b3: {np.size(b3)}')
        # Mostrar o número de elementos em b5
        print(f'Number of elements in b5: {np.size(b5)}')

        # Contar o número de elementos com valor 0 em b3
        num_zeros_b3 = np.count_nonzero(b3 == 0)
        print(f'Number of elements with value 0 in b3: {num_zeros_b3}')
        # Contar o número de elementos com valor 0 em b5
        num_zeros_b5 = np.count_nonzero(b5 == 0)
        print(f'Number of elements with value 0 in b5: {num_zeros_b5}')

        # Máscara para considerar apenas valores diferentes de zero em b3 e b5
        mask_nonzero = (b3 != 0) & (b5 != 0)

        # Calcular NDWI apenas para os valores não nulos em b3 e b5
        ndwi = np.zeros_like(b3, dtype=float)
        ndwi[mask_nonzero] = (b3[mask_nonzero] - b5[mask_nonzero]) / (b3[mask_nonzero] + b5[mask_nonzero])

        # Exibir o NDWI resultante
        # Encontrar o maior valor em ndwi maior que zero
        if np.max(ndwi)==0:
            max_ndci = np.min(ndwi[(ndwi > 0)])
        else:
            max_ndci = np.max(ndwi)
        # Exibir o maior valor presente em ndwi maior que zero
        print(f'Max value in ndwi: {max_ndci}')

        # Encontrar o menor valor em ndwi maior que zero
        if np.min(ndwi)==0:
            min_ndwi = np.min(ndwi[(ndwi > 0)])
        else:
            min_ndwi = np.min(ndwi)
        # Exibir o menor valor presente em ndwi maior que zero
        print(f'Min value in ndwi: {min_ndwi}')

        # Nome da pasta anterior (pasta pai) à pasta onde a imagem será salva
        folder_name = os.path.basename(os.path.abspath(os.path.join(os.path.dirname(caminho_b3), os.pardir)))
        
        # Caminho para o diretório do arquivo de origem
        output_directory = os.path.abspath(os.path.join(os.path.dirname(caminho_b3), os.pardir))
        
        # Caminho completo para o arquivo de saída do gráfico
        output_graph_path = os.path.join(output_directory, f'ndwi_oli_graph_{folder_name}.png')

        # Exibir o NDWI
        plt.imshow(ndwi, cmap='RdYlBu', vmin=-1, vmax=1)
        plt.colorbar(label='NDWI')
        plt.title('Índice de Água de Diferença Normalizada (NDWI)')
        plt.savefig(output_graph_path)
        plt.show()
        print(f"Gŕafico NDWI OLI salvo em {output_graph_path}")
        print(f'--------------- END NDWI OLI CALCULATION')

        return ndwi