import requests

def fetch_users():
    url = "https://jsonplaceholder.typicode.com/users"

    try:
        response = requests.get(url)
        response.raise_for_status()  

        users = response.json()

        if not users:
            print("No users found.")
            return

        count = 1
        for user in users:
            name = user.get("name", "N/A")
            username = user.get("username", "N/A")
            email = user.get("email", "N/A")
            city = user.get("address", {}).get("city", "N/A")

            if not city.lower().startswith('s'):
                continue

            print(f"User {count}:")
            print(f"Name: {name}")
            print(f"Username: {username}")
            print(f"Email: {email}")
            print(f"City: {city}")
            print("-" * 25)
            count += 1

        if count == 1:
            print("No users found with city starting with 'S'.")

    except requests.exceptions.RequestException as e:
        print("Error fetching data from API:", e)


if __name__ == "__main__":
    fetch_users()
