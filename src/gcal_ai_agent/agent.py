from google.adk.agents import LlmAgent
from google.adk.sessions import InMemorySessionService
from gcal_ai_agent.tools import get_upcoming_events
from gcal_ai_agent.tools import create_calendar_event

# 1. Initialize session memory to keep track of the conversation context
# This can be connected to Vertex AI memory stores for persistence
agent_session = InMemorySessionService()

# 2. Define the ADK Agent
# ADK integrates natively with Gemini models, making it seamless to use here.
calendar_agent = LlmAgent(
    name="GoogleCalendarAssistant",
    model="gemini-pro",  # Native Gemini integration
    tools=[get_upcoming_events, create_calendar_event],
    # session=agent_session,
    instruction=(
        "You are an AI scheduling assistant. "
        "Use your tools to check the user's Google Calendar for availability "
        "and schedule new events accurately based on their requests."
    ),
)
