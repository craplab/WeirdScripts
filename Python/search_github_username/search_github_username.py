import requests
import sys
import itertools

GITHUB_URL = "https://github.com/"

def generate_char_combinations(username_length: int, characters: str):
    yield from itertools.product(*([characters] * username_length))

def is_available(username: str):
    url = GITHUB_URL + username
    r =requests.get(url)
    return True if r.status_code == 404 else False

if __name__ == "__main__":
    welcome_msg = ("*" * 50) + "\nThis program checks github username availablity.\n" + ("*" * 50) + "\n"
    print(welcome_msg)

    username_length = int(input("Enter an integer for username length. example: 3 --> "))
    characters = input("Enter a string containing of characters you want to use in username. example: abc --> ")
    print(f"\nchecking all github usernames of length {username_length} containing characters {characters}\n")

    username_generator = generate_char_combinations(username_length, characters)
    for item in username_generator:
        username = ''.join(item)
        available = ("*" * 20  + "Yes" + "*" * 20) if is_available(username) else "No"
        print(f"is username {username} available? {available}")