import requests
types = ["Programming", "Misc", "Dark", "Pun", "Spooky", "Christmas"]

def jokes(query):
    query.capitalize()
    if query not in types:
        query="Any"
    url = f"https://v2.jokeapi.dev/joke/{query}?blacklistFlags=nsfw&type=single"
    r = requests.get(url)
    joke_json = r.json()
    return joke_json
