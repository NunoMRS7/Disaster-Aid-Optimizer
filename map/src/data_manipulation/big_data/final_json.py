import json

# Carregar dados de final.geojson
with open('data/before/final.geojson', 'r', encoding='utf-8') as geojson_file:
    geojson_data = json.load(geojson_file)

# Carregar dados de neighbors.json
with open('data/before/neighbors.json', 'r', encoding='utf-8') as neighbors_file:
    neighbors_data = json.load(neighbors_file)

# Criar estrutura para o novo JSON
municipios_data = {}

# Iterar sobre cada município em geojson_data
for feature in geojson_data['features']:
    nome_municipio = feature['properties']['Municipio']
    centroide = feature['properties']['centroide']
    vizinhos = neighbors_data.get(nome_municipio, [])
    
    municipios_data[nome_municipio] = {
        "centroide": centroide,
        "vizinhos": vizinhos
    }

# Guardar o novo JSON
with open('data/before/final.json', 'w', encoding='utf-8') as output_file:
    json.dump(municipios_data, output_file, ensure_ascii=False, indent=4)

print("File 'data/before/final.json' successfully created!")
