import requests


def check_user_name_availability():
    username = input("Enter username you want to choose\n$ ")

    r = requests.get(f"https://github.com/{username}")

    if r.status_code == 200:
        return "⛔ Username already taken"
    else:
        return " ✅ Username is available"


while(1):
    resp = check_user_name_availability()
    print(resp)
    nxt = input("Do you want to check another name\n$ ")
    if nxt in ["No", "n", "N", "NO"]:
        break
    elif nxt in ["Yes", "Y", "y", "yes"]:
        continue
    else:
        print("Invalid input exiting...\n")
