import os
import rasterio
import numpy as np
from matplotlib import pyplot as plt

def calculate_ndwi_MODIS(caminho_b4, caminho_b2):
    with rasterio.open(caminho_b4) as src_b4, rasterio.open(caminho_b2) as src_b2:
        # Ler os dados das bandas como matrizes numpy
        b4 = src_b4.read(1).astype(float)
        b2 = src_b2.read(1).astype(float)

        # Calcular e imprimir o maior e o menor valor em b4
        print(f'--------------- BEGIN NDWI MODIS CALCULATION')

        # Encontrar o maior valor em b4
        print(f'Max value in b4: {np.max(b4)}')
        # Encontrar o menor valor em b4, valores com 0 não contam
        min_b4 = np.min(b4[(b4 > 0)])
        print(f'Min value in b4: {min_b4}')


        # Encontrar o maior valor em b2
        print(f'Max value in b2: {np.max(b2)}')
        # Encontrar o menor valor em b2, valores com 0 não contam
        min_b2 = np.min(b2[(b2 > 0)])
        print(f'Min value in b2: {min_b2}')

        # Mostrar o número de elementos em b4
        print(f'Number of elements in b4: {np.size(b4)}')
        # Mostrar o número de elementos em b2
        print(f'Number of elements in b2: {np.size(b2)}')

        # Contar o número de elementos com valor 0 em b4
        num_zeros_b4 = np.count_nonzero(b4 == 0)
        print(f'Number of elements with value 0 in b4: {num_zeros_b4}')
        # Contar o número de elementos com valor 0 em b2
        num_zeros_b2 = np.count_nonzero(b2 == 0)
        print(f'Number of elements with value 0 in b2: {num_zeros_b2}')

        # Máscara para considerar apenas valores diferentes de zero em b4 e b2
        mask_nonzero = (b4 != 0) & (b2 != 0)

        # Calcular NDWI apenas para os valores não nulos em b4 e b2
        ndwi = np.zeros_like(b4, dtype=float)
        ndwi[mask_nonzero] = (b4[mask_nonzero] - b2[mask_nonzero]) / (b4[mask_nonzero] + b2[mask_nonzero])

        # Exibir o NDWI resultante
        # Encontrar o maior valor em ndwi maior que zero
        if np.max(ndwi)==0:
            max_ndci = np.max(ndwi[(ndwi < 0)])
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
        folder_name = os.path.basename(os.path.abspath(os.path.join(os.path.dirname(caminho_b4), os.pardir)))
        
        # Caminho para o diretório do arquivo de origem
        output_directory = os.path.abspath(os.path.join(os.path.dirname(caminho_b4), os.pardir))
        
        # Caminho completo para o arquivo de saída do gráfico
        output_graph_path = os.path.join(output_directory, f'ndwi_modis_graph_{folder_name}.png')

        # Exibir o NDWI
        plt.imshow(ndwi, cmap='RdYlBu', vmin=-1, vmax=1)
        plt.colorbar(label='NDWI')
        plt.title('Índice de Água de Diferença Normalizada (NDWI)')
        plt.savefig(output_graph_path)
        plt.show()
        print(f"Gŕafico NDWI MODIS salvo em {output_graph_path}")
        print(f'--------------- END NDWI MODIS CALCULATION')

        return ndwi