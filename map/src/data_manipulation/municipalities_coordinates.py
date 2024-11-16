import csv
import requests
import time


def get_municipalities_coordinates(municipality):
    url = f"https://nominatim.openstreetmap.org/search?q={municipality},Portugal&format=json"
    headers = {'User-Agent': 'PortugalMunicipalitiesGraph/1.0'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200 and response.json():
        data = response.json()[0]
        return float(data['lat']), float(data['lon'])
    print(f"Status code:{response.status_code} for url: {url}")
    return None, None


# Load municipality names from file
def load_municipalities(municipalities):
    with open(municipalities, 'r') as file:
        return [line.strip().strip('"') for line in file if line.strip()]


# Save coordinates data to CSV
def save_coordinates_to_csv(municipalities, filename="data/after/municipalities.csv"):
    with open(filename, mode="w", newline='', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Name", "Latitude", "Longitude", "Population"])  # Header

        for municipality_and_population in municipalities:
            municipality, population = municipality_and_population.split('";') 
            lat, lon = get_municipalities_coordinates(municipality)
            if lat and lon:
                writer.writerow([municipality, lat, lon, population])
                print(f"Saved {municipality} with coordinates ({lat}, {lon}) and population {population}.")
            else:
                print(f"Coordinates not found for {municipality}")
            time.sleep(1)  # Pause to respect rate limits


# Main function
def main():
    municipalities = load_municipalities("data/before/simple_municipalities.csv")
    save_coordinates_to_csv(municipalities, "data/after/municipalities.csv")


if __name__ == "__main__":
    main()

