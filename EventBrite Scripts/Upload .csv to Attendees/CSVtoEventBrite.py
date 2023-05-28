import requests
import csv
import json

def upload_attendees(api_key, event_id, csv_file):
    url = f"https://www.eventbriteapi.com/v3/events/{event_id}/attendees/token={api_key}"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    with open(csv_file, "r") as file:
        csv_data = csv.reader(file)
        next(csv_data)  # Skip the header row

        attendees = []

        for row in csv_data:
            first_name = row[0]
            last_name = row[1]
            email = row[2]
            gender = row[3]
            phone_number = row[4]

            attendee = {
                "profile": {
                    "email": email,
                    "first_name": first_name,
                    "last_name": last_name,
                    "gender": gender,
                    "phone_number": phone_number,
                    # Add more fields as required
                }
            }
            attendees.append(attendee)

        payload = {"attendees": attendees}

        response = requests.patch(url, headers=headers, json=payload)

        if response.status_code == 201:
            print("Attendees uploaded successfully.")
        else:
            print("Failed to upload attendees. Error:", response.text)

# Replace with your Eventbrite API key
api_key = "API_KEY"

# Replace with the Eventbrite event ID
event_id = "EVENT_ID"

# Replace with the path to your attendee CSV file
csv_file = "Path/To/File_Name.CSV"

upload_attendees(api_key, event_id, csv_file)
