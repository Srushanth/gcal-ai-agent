import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar"]


def get_calendar_service():
    """Authenticates the user and returns the Calendar API service object."""
    creds = None
    # The file token.json stores the user's access and refresh tokens.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    return build("calendar", "v3", credentials=creds)


def get_upcoming_events(max_results: int = 10) -> str:
    """
    Retrieves the upcoming events from the user's primary Google Calendar.

    Args:
        max_results: The maximum number of events to return.
    """
    service = get_calendar_service()
    import datetime

    # Get current time in ISO format (required by the API)
    now = datetime.datetime.utcnow().isoformat() + "Z"

    events_result = (
        service.events()
        .list(
            calendarId="primary",
            timeMin=now,
            maxResults=max_results,
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )

    events = events_result.get("items", [])

    if not events:
        return "No upcoming events found."

    # Format the events into a readable string for the LLM
    output = []
    for event in events:
        start = event["start"].get("dateTime", event["start"].get("date"))
        summary = event.get("summary", "No Title")
        output.append(f"{start} - {summary}")

    return "\n".join(output)


def create_calendar_event(summary: str, start_time: str, end_time: str) -> str:
    """
    Creates a new event on the user's primary calendar.

    Args:
        summary: The title or description of the event.
        start_time: The start time in ISO format (e.g., '2026-03-05T09:00:00-07:00').
        end_time: The end time in ISO format (e.g., '2026-03-05T10:00:00-07:00').
    """
    service = get_calendar_service()

    event_payload = {
        "summary": summary,
        "start": {
            "dateTime": start_time,
            "timeZone": "UTC",  # Adjust to your preferred default timezone
        },
        "end": {
            "dateTime": end_time,
            "timeZone": "UTC",
        },
    }

    event = service.events().insert(calendarId="primary", body=event_payload).execute()

    return f"Successfully created event: {event.get('htmlLink')}"
