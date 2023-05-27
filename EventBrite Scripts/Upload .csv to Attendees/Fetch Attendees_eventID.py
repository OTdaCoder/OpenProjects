# import requests

# def fetch_event_ids(api_key):
#     url = "https://www.eventbriteapi.com/v3/users/me/events/"

#     headers = {
#         "Authorization": f"Bearer {api_key}",
#         "Content-Type": "application/json"
#     }

#     response = requests.get(url, headers=headers)

#     if response.status_code == 200:
#         events = response.json()["events"]
#         event_ids = [event["id"] for event in events]
#         print("Event IDs fetched successfully:", event_ids)
#     else:
#         print("Failed to fetch event IDs. Error:", response.text)

# # Replace with your Eventbrite API key
# api_key = "API_KEY"

# fetch_event_ids(api_key)

import requests

def fetch_attendees(event_id, oauth_token):
    url = f"https://www.eventbriteapi.com/v3/events/{event_id}/attendees/"

    headers = {
        "Authorization": f"Bearer {oauth_token}",
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        attendees = response.json()
        print("Attendees fetched successfully:", attendees)
    else:
        print("Failed to fetch attendees. Error:", response.text)

# Replace with your OAuth token
oauth_token = "API_KEY"

# Replace with the Eventbrite event ID you want to fetch attendees from
event_id = "EVENT_ID"

fetch_attendees(event_id, oauth_token)
