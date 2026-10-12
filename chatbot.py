def chatbot():
    print("🤖 Chatbot: Hello! Welcome to my chatbot!")
    print("Type 'bye' to exit the conversation.")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input == "hello" or user_input == "hi":
            print("Chatbot: Hi! Nice to meet you!")

        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks!")

        elif user_input == "what is your name":
            print("Chatbot: I'm a Basic Python Chatbot!")

        elif user_input == "bye":
            print("Chatbot: Goodbye! Have a nice day!")
            break

        else:
            print("Chatbot: Sorry, I don't understand that.")


if __name__ == "__main__":
    chatbot()