def chatbot():
    print("🤖 Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello" or user_input == "hi":
            print("🤖 Chatbot: Hi there!")
        
        elif user_input == "how are you":
            print("🤖 Chatbot: I'm fine, thanks! 😊")
        
        elif user_input == "your name":
            print("🤖 Chatbot: I am a simple chatbot.")
        
        elif user_input == "help":
            print("🤖 Chatbot: You can say hello, ask my name, or ask how I am.")
        
        elif user_input == "bye":
            print("🤖 Chatbot: Goodbye! 👋")
            break
        
        else:
            print("🤖 Chatbot: Sorry, I don't understand.")

# Run chatbot
chatbot()