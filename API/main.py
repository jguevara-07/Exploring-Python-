import asyncio
import aiohttp
import pandas as pd
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("WEATHERSTACK_API_KEY")
WS_URL = "http://api.weatherstack.com/current"
INPUT_FILE = "cities.txt"
OUTPUT_FILE = "weather_data.csv"


async def fetch_weather(session, city):
    """Fetch weather data for a single city asynchronously."""
    params = {'access_key': API_KEY, 'query': city}
    try:
        async with session.get(WS_URL, params=params) as response:
            if response.status != 200:
                print(f"Warning: Failed to fetch {city}: HTTP {response.status}")
                return None

            data = await response.json()

            if "current" not in data or "location" not in data:
                print(f"Warning: Invalid data for {city}: {data.get('error', 'Unknown error')}")
                return None

            return {
                "city": city,
                "temperature": data["current"]["temperature"],
                "localtime": data["location"]["localtime"]
            }

    except Exception as e:
        print(f"Warning: Exception fetching {city}: {e}")
        return None


async def gather_weather_data(cities):
    """Fetch weather for all cities concurrently."""
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_weather(session, city) for city in cities]
        results = await asyncio.gather(*tasks)
        return [r for r in results if r]


async def main():
    # Load cities
    with open(INPUT_FILE) as f:
        cities = [line.strip() for line in f if line.strip()]

    print(f"Fetching weather data for {len(cities)} cities...")

    # Fetch data concurrently
    results = await gather_weather_data(cities)

    # Convert to Pandas DataFrame
    df = pd.DataFrame(results)
    df["fetch_time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("\nDataFrame Preview:")
    print(df)

    # Save to CSV
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"\nData saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    asyncio.run(main())
