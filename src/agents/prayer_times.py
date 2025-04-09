from agno.agent import Agent
from typing import Optional
from datetime import datetime, timedelta
from src.tools.prayer_times import PrayerTimesTool
import dateparser
from src.models import GPT_4O

prayer_times_agent = Agent(
    name="Prayer Time Agent",
    role="Provide Prayer Times",
    model=GPT_4O,
    instructions=(
        "You are an assistant that helps the user find prayer times for a specific address (city and country) "
        "and date. The user will provide an address (e.g., 'Paris, France') and an optional date (e.g., 'tomorrow'). "
        "You should fetch prayer times for the given address and date. "
        "If the user provides no date, default to today's prayer times. If the user provides a relative date like 'tomorrow' or 'next week', convert that to a specific date. "
        "If no address is provided, ask for the address.\n\n"
        "The date format is 'YYYY-MM-DD' for specific dates, and relative date terms like 'tomorrow', 'next week' are supported.\n\n"
        "If the user doesn't specify a date, return prayer times for today."
    ),
    tools=[PrayerTimesTool()],
    show_tool_calls=True,
    markdown=True
)