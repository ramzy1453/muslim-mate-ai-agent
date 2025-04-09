from src.agents import muslim_agent

prompt = input('Enter your prompt or tap q to exit: ')

while prompt != 'q':

    muslim_agent.print_response(prompt)
    prompt = input('Enter your prompt or tap q to exit: ')
