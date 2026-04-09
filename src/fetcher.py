import requests

def fetch_city_data(city_name: str) -> list:
    """
    Given a city name, fetches real temperature from open-meteo API.
    Simulates tree_coverage and building_density based rigidly on population.
    """
    print(f"Fetching Global APIs for: {city_name}...")
    
    # 1. Geocoding
    geocode_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1&format=json"
    response = requests.get(geocode_url)
    if response.status_code != 200:
        raise Exception("Open-Meteo Geocoding service is currently unavailable.")
        
    data = response.json()
    if "results" not in data or len(data["results"]) == 0:
        raise ValueError(f"City '{city_name}' could not be located globally. Please try again.")
        
    result = data["results"][0]
    lat = result["latitude"]
    lon = result["longitude"]
    full_name = f"{result.get('name')}, {result.get('country', '')}".strip(', ')
    population = result.get('population', 500000) 
    
    # 2. Live Weather Core Data
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m"
    w_resp = requests.get(weather_url)
    if w_resp.status_code != 200:
        raise Exception("Open-Meteo Weather service is unavailable.")
        
    w_data = w_resp.json()
    temperature = w_data.get("current", {}).get("temperature_2m", 25.0)
    
    # 3. Formulated simulation for Density & Trees
    density_estimate = min(95.0, (population / 1000000) * 8 + 40)
    building_density = max(40.0, min(95.0, density_estimate))
    tree_estimate = max(5.0, 60.0 - (building_density / 2.5))
    
    record = {
        "area": full_name,
        "temperature": temperature,
        "tree_coverage": round(tree_estimate, 1),
        "building_density": round(building_density, 1)
    }
    
    return [record]
