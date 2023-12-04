import geopandas as gpd
import rasterio
from rasterio.mask import mask
from shapely.geometry import mapping
import os

def recortar_e_salvar_OLI(caminhos_imagens, caminho_shapefile, diretorio_destino_pai):
    caminhos_destino = []  # Lista para armazenar os caminhos de destino

    # Abrir o shapefile com geopandas
    gdf = gpd.read_file(caminho_shapefile)

    # Reprojetar a geometria do shapefile para o CRS da imagem raster (EPSG:32624)
    gdf = gdf.to_crs(epsg=32624)

    for caminho_imagem in caminhos_imagens:
        # Abrir a imagem TIFF com rasterio
        with rasterio.open(caminho_imagem) as src:
            # Recuperar a geometria da máscara do shapefile
            geometria_mascara = gdf.geometry.values[0]
            # Converta a geometria para um formato que o rasterio entenda
            geometria_mascara = [mapping(geometria_mascara)]

            # Recortar a imagem usando a geometria do shapefile como máscara
            imagem_recortada, transformacao_recortada = mask(src, geometria_mascara, crop=True)

            # Atualizar a transformação da imagem recortada
            profile = src.profile
            profile['transform'] = transformacao_recortada
            profile['height'] = imagem_recortada.shape[1]  # Update height
            profile['width'] = imagem_recortada.shape[2]   # Update width

        # Obter o nome da banda a partir do caminho da imagem
        nome_banda = os.path.basename(caminho_imagem).split('_')[-1][1]

        # Caminho para o diretório de destino específico para cada banda
        diretorio_destino = os.path.join(diretorio_destino_pai, f'LL14CUTB{nome_banda}')

        # Criar o diretório se não existir
        os.makedirs(diretorio_destino, exist_ok=True)

        # Obter o nome do arquivo da imagem original
        nome_arquivo = os.path.basename(caminho_imagem)

        # Salvar a imagem recortada em um novo arquivo TIFF
        caminho_destino = os.path.join(diretorio_destino, f'{nome_arquivo[:-4]}_CUT.tif')
        with rasterio.open(caminho_destino, 'w', **profile) as dst:
            dst.write(imagem_recortada)

        # Adicionar o caminho de destino à lista
        caminhos_destino.append(caminho_destino)

        # Exibir mensagem de sucesso
        print(f'Imagem OLI recortada salva em: {caminho_destino}')

    return caminhos_destino