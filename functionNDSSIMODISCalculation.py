import os
import rasterio
import numpy as np
from matplotlib import pyplot as plt

def calculate_ndssi_MODIS(caminho_b3, caminho_b2):
    with rasterio.open(caminho_b3) as src_b3, rasterio.open(caminho_b2) as src_b2:
        # Ler os dados das bandas como matrizes numpy
        b3 = src_b3.read(1).astype(float)
        b2 = src_b2.read(1).astype(float)

        # Calcular e imprimir o maior e o menor valor após a normalização
        print(f'--------------- BEGIN NDSSI MODIS CALCULATION')
        print(f'Max value in b3: {np.max(b3)}')
        if np.min(b3)==0:
            # Encontrar o menor valor em b3 maior que zero
            min_positive_b3 = np.min(b3[(b3 > 0)])
            # Exibir o menor valor presente em b3 maior que zero
            print(f'Min value in b3: {min_positive_b3}')
        else:
            print(f'Min value in b3: {np.min(b3)}')
        print(f'Max value in b2: {np.max(b2)}')
        if np.min(b2)==0:
            # Encontrar o menor valor em b2 maior que zero
            min_positive_b2 = np.min(b2[(b2 > 0)])
            # Exibir o menor valor presente em b2 maior que zero
            print(f'Min value in b2: {min_positive_b2}')
        else:
            print(f'Min value in b2: {np.min(b2)}')

        # Mostrar o número de elementos em b2
        print(f'Number of elements in b2: {np.size(b2)}')
        # Mostrar o número de elementos em b3
        print(f'Number of elements in b3: {np.size(b3)}')

        # Contar o número de elementos com valor 0 em b2
        num_zeros_b2 = np.count_nonzero(b2 == 0)
        print(f'Number of elements with value 0 in b2: {num_zeros_b2}')
        # Contar o número de elementos com valor 0 em b3
        num_zeros_b3 = np.count_nonzero(b3 == 0)
        print(f'Number of elements with value 0 in b3: {num_zeros_b3}')

        # Máscara para considerar apenas valores diferentes de zero em b3 e b2
        mask_nonzero = (b3 != 0) & (b2 != 0)

        # Calcular NDSSI apenas para os valores não nulos em b3 e b2
        ndssi = np.zeros_like(b3, dtype=float)
        ndssi[mask_nonzero] = (b3[mask_nonzero] - b2[mask_nonzero]) / (b3[mask_nonzero] + b2[mask_nonzero])

        # Exibir o NDSSI resultante
        print(f'Max value in ndssi: {np.max(ndssi)}')
        # Encontrar o menor valor em ndssi maior que zero
        #min_positive_ndssi = np.min(ndssi[(ndssi > 0)])
        ###
        ###
        if np.min(ndssi)==0:
            min_positive_ndssi = np.min(ndssi[(ndssi > 0)])
        else:
            min_positive_ndssi = np.min(ndssi)
        ###
        ###
        # Exibir o menor valor presente em ndssi maior que zero
        print(f'Min value in ndssi: {min_positive_ndssi}')

        # Nome da pasta anterior (pasta pai) à pasta onde a imagem será salva
        folder_name = os.path.basename(os.path.abspath(os.path.join(os.path.dirname(caminho_b3), os.pardir)))
        
        # Caminho para o diretório do arquivo de origem
        output_directory = os.path.abspath(os.path.join(os.path.dirname(caminho_b3), os.pardir))
        
        # Caminho completo para o arquivo de saída do gráfico
        output_graph_path = os.path.join(output_directory, f'ndssi_modis_graph_{folder_name}.png')

        # Exibir o NDSSI
        plt.imshow(ndssi, cmap='coolwarm', vmin=-1, vmax=1)
        plt.colorbar(label='NDSSI')
        plt.title('Índice de Concentração de Sedimentos Suspensos (NDSSI)')
        plt.savefig(output_graph_path)
        plt.show()
        print(f"Gŕafico NDSSI salvo em {output_graph_path}")
        print(f'--------------- END NDSSI MODIS CALCULATION')

        return ndssi