from src.agents.quran import quran_agent

prompt = input('Enter your prompt or tap q to exit: ')

while prompt != 'q':

    quran_agent.print_response(prompt)
    prompt = input('Enter your prompt or tap q to exit: ')
