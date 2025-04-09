from src.agents import muslim_agent

def main():
    print("Welcome to the Muslim Assistant! You can ask questions related to Quran, prayer times, and more.")
    print("Type 'q' to exit.")
    
    while True:
        prompt = input('Enter your question: ')

        if prompt.lower() == 'q':
            print("Goodbye! May peace be upon you.")
            break

        muslim_agent.print_response(prompt)

if __name__ == "__main__":
    main()
