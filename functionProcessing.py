from functionMODISCutWithShapefile import recortar_e_salvar_MODIS
from functionNDCIMODISCalculation import calculate_ndci_MODIS
from functionNDSSIMODISCalculation import calculate_ndssi_MODIS
from functionNDWIMODISCalculation import calculate_ndwi_MODIS
from functionOLICutWithShapefile import recortar_e_salvar_OLI
from functionNDWIOLICalculation import calculate_ndwi_OLI
from functionNDCIOLICalculation import calculate_ndci_OLI
from functionNDSSIOLICalculation import calculate_ndssi_OLI

def processar_imagens(caminhos_imagens_OLI, caminhos_imagens_MODIS, caminho_shapefile,
                      diretorio_destino_pai_OLI, diretorio_destino_pai_MODIS):
    
    # Processamento para imagens OLI
    imagens_cortadas_OLI = recortar_e_salvar_OLI(caminhos_imagens_OLI, caminho_shapefile, diretorio_destino_pai_OLI)

    caminho_b2_OLI = next(caminho for caminho in imagens_cortadas_OLI if "B2" in caminho)
    caminho_b3_OLI = next(caminho for caminho in imagens_cortadas_OLI if "B3" in caminho)
    caminho_b4_OLI = next(caminho for caminho in imagens_cortadas_OLI if "B4" in caminho)
    caminho_b5_OLI = next(caminho for caminho in imagens_cortadas_OLI if "B5" in caminho)

    # Calcular índices para imagens OLI
    ndwi_OLI = calculate_ndwi_OLI(caminho_b3_OLI, caminho_b5_OLI)
    ndci_OLI = calculate_ndci_OLI(caminho_b5_OLI, caminho_b4_OLI)
    ndssi_OLI = calculate_ndssi_OLI(caminho_b2_OLI, caminho_b5_OLI)

    # Processamento para imagens MODIS
    imagens_cortadas_MODIS = recortar_e_salvar_MODIS(caminhos_imagens_MODIS, caminho_shapefile, diretorio_destino_pai_MODIS)

    caminho_b1_MODIS = next(caminho for caminho in imagens_cortadas_MODIS if "B1" in caminho)
    caminho_b2_MODIS = next(caminho for caminho in imagens_cortadas_MODIS if "B2" in caminho)
    caminho_b3_MODIS = next(caminho for caminho in imagens_cortadas_MODIS if "B3" in caminho)
    caminho_b4_MODIS = next(caminho for caminho in imagens_cortadas_MODIS if "B4" in caminho)

    # Calcular índices para imagens MODIS
    ndwi_MODIS = calculate_ndwi_MODIS(caminho_b4_MODIS, caminho_b2_MODIS)
    ndci_MODIS = calculate_ndci_MODIS(caminho_b1_MODIS, caminho_b2_MODIS)
    ndssi_MODIS = calculate_ndssi_MODIS(caminho_b3_MODIS, caminho_b2_MODIS)

    # Retornar os resultados
    return ndwi_OLI, ndci_OLI, ndssi_OLI, ndwi_MODIS, ndci_MODIS, ndssi_MODIS