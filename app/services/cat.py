import httpx

async def validate_breed(breed_name: str) -> bool:
    url = "https://api.thecatapi.com/v1/breeds"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        breeds = response.json()
        return any(breed_name.lower() == b['name'].lower() for b in breeds)
