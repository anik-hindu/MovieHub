from modules.api import get_trending_movies

def main():
    print("Welcome to MovieHub!")
    movies = get_trending_movies()

    print(f"\nTop {len(movies)} Trending Movies:\n")

    for i, movie in enumerate(movies[:10], 1):
            print(f"{i}. {movie['title']} ({movie.get('release_date', 'N/A')})")


if __name__ == "__main__":
    main()