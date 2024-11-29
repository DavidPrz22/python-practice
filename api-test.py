import requests
import sys
import random
import json

def main():

    try: 
        band = sys.argv[1]
        amount = sys.argv[2]
    except IndexError:
        if not get_list_index(sys.argv, 1):
            band = random.choice(["Wizzer", "Eminem", "Drake", "Adele", "Sia"])

        if not get_list_index(sys.argv, 2):
            amount = random.randint(1, 50)
    
    response = requests.get(f"https://itunes.apple.com/search?entity=song&limit={amount}&term={band}")
    results = response.json()['results']
    
    for result in results:
        print(f"Track: {result["trackName"]}, Release date: {result["releaseDate"]}")


    # print(json.dumps(results, indent=2))

def get_list_index(list, index):
    """
    Safely gets item from list
    """ 

    try:
        return list[index]
    except IndexError:
        return None
    

main()