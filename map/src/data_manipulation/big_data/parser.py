# Script responsável por unir as informações de coordenadas aos .dbf através do identificar único
# é necessário ter os 4 ficheiros na mesma diretoria: .dbf, .prj, .shp e .shx

import geopandas as gpd
import os
import pandas as pd

def parse(path, name):
    # Lista para armazenar os GeoDataFrames
    gdfs = []

    # Iterar sobre os arquivos shapefile
    for file in os.listdir(path):

        if file.endswith('.shp') and "_Mun_" in file:
            gdf = gpd.read_file(os.path.join(path, file), encoding='utf-8')
            gdfs.append(gdf)

    # Concatenar os GeoDataFrames
    gdf_final = pd.concat(gdfs)

    # Criar destino do ficheiro
    output_dir = "data/before/geojson"
    file_name = os.path.join(output_dir, f"collapsed_info-{name}.geojson")

    # Criar o diretório caso ele não exista
    os.makedirs(output_dir, exist_ok=True)

    # Salvar como GeoJSON
    gdf_final.to_file(file_name, driver='GeoJSON')

# Definir o diretório com os shapefiles
main_dir = "data/before/data/"
print("Parsing", main_dir)
parse(main_dir, "continental")

print("Parsing complete!\n")


