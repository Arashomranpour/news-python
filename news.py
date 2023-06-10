import requests as re
from sys import argv

api_key = "b268dcd9bda8413891e9a540ae9d1217"
url = "https://newsapi.org/v2/top-headlines?"


def get_cat(category):
    query_cat = {
        "category": category,
        "sortBy": "popularity",
        "apiKey": api_key,
        "language": "en",
    }
    return _get_article(query_cat)


def _get_article(params):
    response = re.get(url, params=params)
    articles = response.json()["articles"]
    results = []
    for article in articles:
        results.append(
            {
                "titles": article["title"],
                "description": article["description"],
                "url": article["url"],
            }
        )

    for res in results:
        print("Title : " + res["titles"] + "\n")
        print("Description : " + res["description"] + "\n")
        print("link to read more :" + res["url"] + "\n")
        print("\n")


def get_cat_query(q):
    query_parameters = {
        # "category": category,
        "q": q,
        "apiKey": api_key,
        "sortBy": "popularity",
        "language": "en",
    }
    return _get_article(query_parameters)


if __name__ == "__main__":
    print("Getting news ..")
    if len(argv) < 2 or not argv[1]:
        get_cat("news")
    else:
        get_cat_query(argv[1])

    print(f"retrived top News")
