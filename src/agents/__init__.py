from .quran import quran_agent
from .prayer_times import prayer_times_agent
from agno.team import Team
from src.models import GPT_4O

muslim_agent = Team(
    mode="coordinate",
    members=[quran_agent, prayer_times_agent],
    model=GPT_4O,
    success_criteria="A comprehensive Islamic report with clear sections and data-driven insights.",
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)
