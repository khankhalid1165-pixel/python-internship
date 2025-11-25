# rule_based_chatbot.py

def chatbot():
    """
    Main chatbot function that handles user interaction
    """
    print("🤖 Welcome to RuleBot! I'm a simple rule-based chatbot.")
    print("Type 'quit', 'exit', or 'bye' to end the conversation\n")
    
    while True:
        # Collect user input and convert to lowercase for easier matching
        user_input = input("You: ").lower().strip()
        
        # Exit condition - break the loop
        if user_input in ['quit', 'exit', 'bye', 'goodbye']:
            print("Bot: Goodbye! Thanks for chatting with me! 👋")
            break
        
        # Handle empty input
        elif not user_input:
            print("Bot: I didn't catch that. Could you please type something?")
            continue
        
        # Greeting responses
        elif any(word in user_input for word in ['hello', 'hi', 'hey', 'hola']):
            print("Bot: Hello there! How can I assist you today? 😊")
        
        # How are you responses
        elif any(word in user_input for word in ['how are you', 'how do you do']):
            print("Bot: I'm just a bunch of code, but I'm functioning perfectly! How about you?")
        
        # Name questions
        elif any(word in user_input for word in ['your name', 'who are you']):
            print("Bot: I'm RuleBot, a simple rule-based chatbot created with Python!")
        
        # Time questions (simple response)
        elif any(word in user_input for word in ['time', 'what time']):
            print("Bot: I don't have access to real-time clock, but you can check your device time!")
        
        # Weather questions
        elif any(word in user_input for word in ['weather', 'temperature']):
            print("Bot: I'm just a simple bot and don't have weather data. You might want to check a weather app!")
        
        # Help request
        elif any(word in user_input for word in ['help', 'what can you do']):
            print("Bot: I can chat about simple topics! Try asking about my name, time, or just say hello!")
        
        # Thanks responses
        elif any(word in user_input for word in ['thank', 'thanks']):
            print("Bot: You're welcome! Happy to help! 😊")
        
        # Joke request
        elif any(word in user_input for word in ['joke', 'funny']):
            print("Bot: Why do programmers prefer dark mode? Because light attracts bugs! 😄")
        
        # Programming questions
        elif any(word in user_input for word in ['python', 'programming', 'code']):
            print("Bot: Python is awesome! I was built using Python's if-else statements.")
        
        # Default response for unmatched inputs
        else:
            print("Bot: I'm still learning! Could you try asking something else?")
        
        # Add a small separator for better readability
        print("-" * 50)

def test_chatbot():
    """
    Function to test the chatbot with predefined inputs
    """
    test_cases = [
        "hello",
        "what's your name?",
        "how are you?",
        "what time is it?",
        "tell me a joke",
        "thank you",
        "what can you do?",
        "random question",
        "bye"
    ]
    
    print("\n🧪 Testing Chatbot Functionality:")
    print("=" * 40)
    
    for test_input in test_cases:
        print(f"Test Input: '{test_input}'")
        # Simulate the chatbot response logic
        user_input = test_input.lower().strip()
        
        if user_input in ['quit', 'exit', 'bye', 'goodbye']:
            print("Response: Goodbye! Thanks for chatting with me! 👋")
            break
        elif any(word in user_input for word in ['hello', 'hi', 'hey', 'hola']):
            print("Response: Hello there! How can I assist you today? 😊")
        # ... (similar responses as in main chatbot)
        else:
            print("Response: I'm still learning! Could you try asking something else?")
        print("-" * 30)


if __name__ == "__main__":
    # Run the main chatbot
    chatbot()
    
    # Uncomment the line below to run tests
    # test_chatbot()