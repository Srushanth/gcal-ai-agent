# gcal-ai-agent

An AI-powered assistant for automating Google Calendar scheduling, event management, and smart reminders using the Google Calendar API and Google Gen AI (Gemini via Google ADK).

## Features

- **Fetch Upcoming Events**: Simply ask the agent to retrieve your upcoming calendar events.
- **Create Calendar Events**: Schedule new meetings or reminders seamlessly using natural language.
- **Powered by Gemini**: Uses the native `gemini-2.5-flash` model via Google ADK to understand and execute scheduling commands accurately.

## Prerequisites

- Python 3.13 or higher
- A Google Cloud Project with the **Google Calendar API** enabled
- OAuth 2.0 Client IDs (Desktop application) for authentication

## Setup & Installation

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd gcal-ai-agent
```

### 2. Set up the virtual environment

This project uses [`uv`](https://docs.astral.sh/uv/) for dependency management out-of-the-box.

```bash
uv sync
```

### 3. Configure Google Credentials

To authenticate the client library with Google Calendar, follow these steps:

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project (or select an existing one) and navigate to **APIs & Services**.
3. Enable the **Google Calendar API**.
4. Go to **Credentials**, click **Create Credentials**, and select **OAuth client ID**.
5. Set the Application type to **Desktop app**.
6. Download the generated JSON file and save it as `credentials.json` in the root (or `src/` directory depending on your working directory).

_Note: On your first run, the app will open a browser window asking you to log in and authorize the application (via OAuth) to access your calendar. A `token.json` will be saved locally for subsequent runs._

## Testing with ADK Web UI

You can interactively test the agent's behavior using the built-in ADK Web UI.

1. Create a `.env` file inside the `src/` directory.
2. Add your Gemini API key to the `.env` file:
   ```env
   GOOGLE_API_KEY=your_gemini_api_key_here
   ```
3. Navigate to the `src` directory.
4. Run the `adk web` command.

```bash
cd src
adk web
```

5. Open the provided local URL (typically `http://127.0.0.1:8000`) in your browser to start chatting with the `GoogleCalendarAssistant` agent.

## Usage

You can run the agent and interact with it using Google ADK's native `LlmAgent`.

```python
from gcal_ai_agent.agent import root_agent

# Use the GoogleCalendarAssistant agent
response = root_agent("What are my upcoming events for today?")
print(response)

response = root_agent("Schedule a meeting with the team tomorrow at 10 AM for 1 hour.")
print(response)
```

## Project Structure

- `pyproject.toml` / `uv.lock`: Dependency management metadata.
- `src/gcal_ai_agent/agent.py`: Defines the `GoogleCalendarAssistant` LLM Agent powered by Gemini.
- `src/gcal_ai_agent/tools.py`: Contains the actual Python functions that interact with the Google Calendar API (`get_upcoming_events`, `create_calendar_event`).
- `notebooks/`: Jupyter notebooks (`create-calendar-event.ipynb`, `get-upcoming-events.ipynb`) for testing and development logic.
