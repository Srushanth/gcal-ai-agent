from google.adk.agents import LlmAgent
from google.adk.tools import AgentTool
from gcal_ai_agent.tools import get_upcoming_events
from gcal_ai_agent.tools import create_calendar_event

# 2. Define the ADK Agent
# ADK integrates natively with Gemini models, making it seamless to use here.
formatter_agent = LlmAgent(
    name="EventFormatter",
    model="gemini-2.5-flash",
    instruction=(
        "You are an expert at formatting calendar events. "
        "Your task is to take a raw list of calendar events "
        "and format them into a clean, easy-to-read, and visually appealing output."
    ),
)

root_agent = LlmAgent(
    name="GoogleCalendarAssistant",
    model="gemini-2.5-flash",  # Native Gemini integration
    tools=[get_upcoming_events, create_calendar_event, AgentTool(formatter_agent)],
    instruction=(
        "You are an AI scheduling assistant. "
        "Use your tools to check the user's Google Calendar for availability "
        "and schedule new events accurately based on their requests. "
        "Use the EventFormatter agent to properly format the listed calendar events before presenting them to the user."
    ),
)
