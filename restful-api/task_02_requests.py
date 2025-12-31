import requests
import csv

BASE_URL = "https://jsonplaceholder.typicode.com"
POSTS_ENDPOINT = "/posts"

def fetch_and_print_posts():
    url = BASE_URL + POSTS_ENDPOINT
    response = requests.get(url)

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])
    else:
        print("Failed to fetch posts.")

def fetch_and_save_posts():
    url = BASE_URL + POSTS_ENDPOINT
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        structured_posts = [
            {"id": post["id"], "title": post["title"], "body": post["body"]}
            for post in posts
        ]

        with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(structured_posts)
    else:
        print("Failed to fetch posts.")
