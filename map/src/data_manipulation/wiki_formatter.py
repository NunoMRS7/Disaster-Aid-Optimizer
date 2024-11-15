# Load the data file and perform cleaning

# Reading the file content
file_path = 'data/before/wiki_municipalities.txt'
cleaned_data = ["Name", "Population"]

# Define the transformation function
def transform_line(line):
    # Split by tabs, assuming this structure based on example:
    # Municipality Name \t Creation Date \t Code \t Population
    parts = line.strip().split('\t')
    
    if len(parts) >= 4:
        # Extract municipality name and population
        municipality_name = parts[0]
        population = parts[-1].replace(" ", "")  # Join population by removing spaces

        # Append the transformed data in the specified format
        cleaned_data.append(f'"{municipality_name}";{population}')

# Read the file and process each line
with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()
    
    # Skip the header and process each line
    for line in lines[1:]:
        transform_line(line)

# Save the cleaned data to a new CSV file
output_file_path = 'data/before/simple_municipalities.csv'
with open(output_file_path, 'w', encoding='utf-8') as file:
    file.write("\n".join(cleaned_data))

output_file_path

