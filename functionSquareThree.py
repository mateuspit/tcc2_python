def calcular_vertices_quadrado(lat, lon):
    # Distância por grau de latitude na linha do equador (aproximadamente 111.32 km)
    dist_por_grau_lat = 111.32

    # Distância por grau de longitude na linha do equador (aproximadamente 111.32 km)
    dist_por_grau_lon = 111.32

    # Tamanho do lado do quadrado em km
    tamanho_lado = 3

    # Calcular a mudança em graus de latitude e longitude
    mudanca_lat = tamanho_lado / dist_por_grau_lat
    mudanca_lon = tamanho_lado / dist_por_grau_lon

    # Calcular os outros três vértices
    ponto_superior_esquerdo = {"latitude": lat, "longitude": lon}
    ponto_superior_direito = {"latitude": lat, "longitude": lon + mudanca_lon}
    ponto_inferior_direito = {"latitude": lat - mudanca_lat, "longitude": lon + mudanca_lon}
    ponto_inferior_esquerdo = {"latitude": lat - mudanca_lat, "longitude": lon}

    return {
        "ponto_superior_esquerdo": ponto_superior_esquerdo,
        "ponto_superior_direito": ponto_superior_direito,
        "ponto_inferior_direito": ponto_inferior_direito,
        "ponto_inferior_esquerdo": ponto_inferior_esquerdo
    }
