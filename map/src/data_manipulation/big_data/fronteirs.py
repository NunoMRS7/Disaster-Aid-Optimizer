import geopandas as gpd
import json
import os

# Define the directory where the geojson files are located
geojson_dir = 'data/before/geojson/'
output_file = 'data/before/neighbors.json'

def get_neighbors(municipality_name, gdf):
    # Get the geometry of the current municipality
    municipality_geom = gdf[gdf['Municipio'] == municipality_name].geometry.values[0]
    # Find neighbors by checking if their geometries intersect with a small buffer
    neighbors = gdf[gdf.geometry.buffer(0.001).intersects(municipality_geom)]
    neighbors = neighbors[neighbors['Municipio'] != municipality_name]
    return neighbors['Municipio'].tolist()

# List to store all municipalities and their neighbors
municipalities_neighbors = {}

# Process each .geojson file in the directory
for file_name in os.listdir(geojson_dir):
    if file_name.endswith('.geojson'):
        print("Parsing " + file_name + "\nThis may take a few minutes...")
        file_path = os.path.join(geojson_dir, file_name)
        gdf = gpd.read_file(file_path)
        
        # Iterate over each municipality in the file
        for municipality_name in gdf['Municipio'].unique():
            neighbors = get_neighbors(municipality_name, gdf)
            municipalities_neighbors[municipality_name] = neighbors

# Save the result in JSON format
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(municipalities_neighbors, f, ensure_ascii=False, indent=4)

print(f"'{output_file}' successfully created!")
