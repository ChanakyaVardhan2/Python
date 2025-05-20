import requests

pokemon = input("Enter the pokemon name: ").lower()

url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    name = data["name"]
    weight = data["weight"]
    height = data["height"]
    types = [t["type"]["name"] for t in data["types"]]
    moves = [t["move"]["name"] for t in data["moves"]]
    

    print(f"\nName : {name.capitalize()}")
    print(f"Types : {' , '.join(types)}")
    print(f"Weight : {weight}")
    print(f"Height : {height}")
    print(f"\nMoves  ({len(moves)} total):")
    for move in moves[:5]:  
        print(f"- {move}")
else:
    print("Invalid Entry")
