{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/usr/lib/python3/dist-packages/scipy/__init__.py:146: UserWarning: A NumPy version >=1.17.3 and <1.25.0 is required for this version of SciPy (detected version 1.26.2\n",
      "  warnings.warn(f\"A NumPy version >={np_minversion} and <{np_maxversion}\"\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "from scipy import stats\n",
    "\n",
    "def calcular_estatisticas_indices(ndwi_OLI, ndci_OLI, ndssi_OLI, ndwi_MODIS, ndci_MODIS, ndssi_MODIS):\n",
    "    # Lista de índices\n",
    "    indices = [ndwi_OLI, ndci_OLI, ndssi_OLI, ndwi_MODIS, ndci_MODIS, ndssi_MODIS]\n",
    "\n",
    "    # Lista para armazenar os resultados\n",
    "    resultados = []\n",
    "\n",
    "    for indice in indices:\n",
    "        # Remover valores zero\n",
    "        indice_sem_zero = indice[indice != 0]\n",
    "\n",
    "        # Calcular estatísticas para cada índice\n",
    "        if len(indice_sem_zero) > 0:\n",
    "            media = np.mean(indice_sem_zero)\n",
    "            mediana = np.median(indice_sem_zero)\n",
    "            moda = stats.mode(indice_sem_zero).mode[0]\n",
    "            desvio_padrao = np.std(indice_sem_zero)\n",
    "            variancia = np.var(indice_sem_zero)\n",
    "        else:\n",
    "            # Se todos os valores são zero, definir estatísticas como NaN\n",
    "            media = mediana = moda = desvio_padrao = variancia = np.nan\n",
    "\n",
    "        # Adicionar resultados à lista\n",
    "        resultados.append({\n",
    "            'media': media,\n",
    "            'mediana': mediana,\n",
    "            'moda': moda,\n",
    "            'desvio_padrao': desvio_padrao,\n",
    "            'variancia': variancia\n",
    "        })\n",
    "\n",
    "    return resultados"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
