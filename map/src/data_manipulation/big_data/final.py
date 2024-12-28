import json
import csv

# Carrega o ficheiro final.json
with open('map/data/before/final.json', 'r') as json_file:
    municipios_data = json.load(json_file)

# Carrega o ficheiro municipalities_population.csv
population_data = {}
with open('map/data/before/municipalities_population.csv', 'r') as csv_file:
    reader = csv.reader(csv_file, delimiter=';')
    for row in reader:
        municipio = row[0].strip('"')
        population = int(row[1])
        population_data[municipio] = population

# Atualiza os dados de cada município com a população
for municipio, dados in municipios_data.items():
    if municipio in population_data:
        dados['population'] = population_data[municipio]
    else:
        dados['population'] = 'N/A'

# Salva o novo ficheiro finalizado
with open('map/data/after/final_output.json', 'w') as output_file:
    json.dump(municipios_data, output_file, indent=4, ensure_ascii=False)

print("File 'map/data/after/final_output.json' successfully created.")
