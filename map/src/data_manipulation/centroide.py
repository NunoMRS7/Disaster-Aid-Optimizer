import json
from shapely.geometry import shape, MultiPolygon
from pyproj import Proj, Transformer
import matplotlib.pyplot as plt

# Define as projeções
etrs_tm06 = Proj("EPSG:3763")  # ETRS 1989 TM06
wgs84 = Proj("EPSG:4326")      # WGS 84
transformer = Transformer.from_proj(etrs_tm06, wgs84)  # Criar o transformador

# Definir os caminhos para os ficheiros GeoJSON
geojson_files = ['map/data/before/geojson/collapsed_info-continental.geojson']

# Lista para armazenar todas as features
all_features = []

# Carregar e processar cada GeoJSON
for file_path in geojson_files:
    print("Creating centroids for", file_path.replace('geojson/', '').replace('.geojson', ''))
    with open(file_path, 'r', encoding='utf-8') as f:
        geojson_data = json.load(f)
        for feature in geojson_data["features"]:
            # Extrair e processar a geometria
            polygon_geom = shape(feature["geometry"])
            
            # Verificar se a geometria é válida
            if not polygon_geom.is_valid:
                print(f"Geometria inválida para a feature: {feature['properties']}")
                continue
            
            # Calcular o centróide usando a envoltória convexa se for MultiPolygon
            if isinstance(polygon_geom, MultiPolygon):
                hull = polygon_geom.convex_hull
                centroid = hull.centroid
                
                # Visualizar todos os polígonos dentro do MultiPolygon
                for poly in polygon_geom.geoms:  # Usar .geoms para iterar sobre os polígonos
                    x, y = poly.exterior.xy
                    plt.fill(x, y, alpha=0.5, fc='blue', ec='black')
            else:
                centroid = polygon_geom.centroid
                x, y = polygon_geom.exterior.xy
                plt.fill(x, y, alpha=0.5, fc='blue', ec='black')

            # Transformar as coordenadas
            lon, lat = transformer.transform(centroid.x, centroid.y)

            # Remover a geometria e adicionar o centróide
            del feature["geometry"]
            feature["properties"]["centroide"] = [lon, lat]

            # Adicionar a feature processada à lista geral
            all_features.append(feature)
           
            ## Adicionar o ponto do centróide à visualização
            #plt.plot(centroid.x, centroid.y, 'ro')  # Ponto do centróide
            #plt.title(feature['properties']['Municipio'])
            #plt.xlabel('Longitude')
            #plt.ylabel('Latitude')
            #plt.show()

# Ordenar todas as features alfabeticamente pelo município
all_features.sort(key=lambda x: x["properties"]["Municipio"])

# Criar a estrutura do GeoJSON final
final_geojson = {
    "type": "FeatureCollection",
    "name": "collapsed_info",
    "crs": {
        "type": "name",
        "properties": {
            "name": "urn:ogc:def:crs:EPSG::3763"
        }
    },
    "features": all_features
}

# Guardar o GeoJSON combinado num único ficheiro
with open('map/data/before/final.geojson', 'w', encoding='utf-8') as f:
    json.dump(final_geojson, f, ensure_ascii=False, indent=4)
