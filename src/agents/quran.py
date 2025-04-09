from agno.agent import Agent
from dotenv import load_dotenv
from src.utils.quran import QuranUtils
from src.tools.quran import QuranTool
from src.models import GPT_4O

llm = GPT_4O

editions = QuranUtils().get_editions()

quran_agent = Agent(
    name="Quran Agent",
    role="Get Quran Ayahs",
    model=llm,
    instructions=(
        "You are an assistant helping the user find a Quran edition identifier based on their input. "
        "The user will provide a name or partial name of a Quran edition (e.g., 'Fahad', 'Pickthall'). "
        "You need to search for the most relevant edition from the following list and return its identifier. "
        "If the user provides no input or if the input does not match any edition, return 'en.asad' by default. "
        "The identifier is always in the format of 'language.identifier' (e.g., 'en.asad').\n\n"
        "Here is the list of available editions:\n"
        f"{str(editions)}"
    ),
    tools=[QuranTool()],
    show_tool_calls=True,
    markdown=True
)