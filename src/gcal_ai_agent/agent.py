from google.adk.agents import LlmAgent
from gcal_ai_agent.tools import get_upcoming_events
from gcal_ai_agent.tools import create_calendar_event

# 2. Define the ADK Agent
# ADK integrates natively with Gemini models, making it seamless to use here.
root_agent = LlmAgent(
    name="GoogleCalendarAssistant",
    model="gemini-2.5-flash",  # Native Gemini integration
    tools=[get_upcoming_events, create_calendar_event],
    instruction=(
        "You are an AI scheduling assistant. "
        "Use your tools to check the user's Google Calendar for availability "
        "and schedule new events accurately based on their requests."
    ),
)
