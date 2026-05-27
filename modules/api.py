import requests
from config import API_KEY, BASE_URL

def main():
    trending_movies = get_trending_movies()
    print(trending_movies)


def get_trending_movies():
    url = f"{BASE_URL}/trending/movie/day"
    params = {"api_key" : API_KEY}
    response = requests.get(url, params)
    
    if response.status_code == 200:
        return response.json()["results"]
    else:
        print("Error", response.status_code)


if __name__ == "__main__":
    main()