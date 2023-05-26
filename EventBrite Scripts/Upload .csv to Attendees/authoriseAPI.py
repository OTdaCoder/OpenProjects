import requests

def authorize_api(api_key):
    url = "https://www.eventbriteapi.com/v3/users/me/?token={api_key}"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        user_data = response.json()
        user_id = user_data["id"]
        user_name = user_data["name"]
        print(f"API key authorization successful. User ID: {user_id}, User Name: {user_name}")
    else:
        print("Failed to authorize API key. Error:", response.text)

# Replace with your Eventbrite API key
api_key = "API_KEY"

authorize_api(api_key)
