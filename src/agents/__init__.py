from .quran import quran_agent
from .prayer_times import prayer_times_agent
from agno.team import Team
from src.models import GPT_4O

llm = GPT_4O

muslim_agent = Team(
    mode="coordinate",
    members=[quran_agent, prayer_times_agent],
    model=llm,
    success_criteria="Provide comprehensive Islamic assistance, including Quranic verses, prayer times, and other helpful information for Muslims.",
    instructions=[
        "Assist Muslims in finding Quranic verses based on their queries.",
        "Provide accurate prayer times based on location and date.",
        "Offer helpful Islamic knowledge and guidance where needed.",
        "Always be respectful, informative, and culturally sensitive."
    ],
    show_tool_calls=True,
    markdown=True,
)
