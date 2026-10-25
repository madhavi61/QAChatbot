import spacy

# Preserve spaCy's original model loader.
original_spacy_load = spacy.load


def load_model_without_saved_tokenizer(
    name, *args, **kwargs
):
    """Load the English model without its saved tokenizer."""
    if name == "en_core_web_sm":
        excluded = list(kwargs.get("exclude") or [])
        if "tokenizer" not in excluded:
            excluded.append("tokenizer")
        kwargs["exclude"] = excluded

    return original_spacy_load(name, *args, **kwargs)


# Apply the workaround before ChatterBot initializes.
spacy.load = load_model_without_saved_tokenizer

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


def create_chatbot():
    """Create and train a chatbot with sample conversations."""

    bot = ChatBot(
        "SimpleQAChatbot",
        storage_adapter="chatterbot.storage.SQLStorageAdapter",
        logic_adapters=[
            {
                "import_path": "chatterbot.logic.BestMatch",
                "maximum_similarity_threshold": 0.90,
                "default_response": "Sorry, I don't understand that question yet."
            }
        ],
        database_uri="sqlite:///chatbot.sqlite3"
    )

    trainer = ListTrainer(bot)

    # Training data: sample questions and answers
    conversations = [
    # Greetings
    ["Hello", "Hi! How can I help you?"],
    ["Hi", "Hello! How can I help you?"],
    ["Hey", "Hey! What can I do for you?"],
    ["Good morning", "Good morning! How are you?"],
    ["Good evening", "Good evening! How was your day?"],

    # General conversation
    ["How are you?", "I am doing well, thank you!"],
    ["I am fine", "Glad to hear that!"],
    ["What is your name?", "I am a Python chatbot."],
    ["Who created you?", "I was created using Python and ChatterBot."],

    # Technical questions
    ["What is Python?", "Python is a programming language."],
    ["What is Django?", "Django is a Python web framework."],
    ["What is AI?", "AI stands for Artificial Intelligence."],
    ["What is machine learning?",
     "Machine learning helps computers learn from data."],
    ["What is a chatbot?",
     "A chatbot is a program that can communicate with users."],

    # Questions about the chatbot
    ["What is your name?", "I am a Python chatbot."],
    ["Who are you?", "I am a Python chatbot."],
    ["Tell me about yourself", "I am a simple chatbot built using Python."],
    ["What can you do?", "I can answer simple questions."],

    # Closing conversation
    ["Thank you", "You're welcome!"],
    ["Thanks", "Happy to help!"],
    ["Goodbye", "Have a nice day!"],
    ["Bye", "Goodbye!"]
    ]

    # Train the chatbot using known conversations
    for conversation in conversations:
        trainer.train(conversation)

    return bot


def main():
    """Run the chatbot in the terminal."""

    print("Welcome to Simple Q&A Chatbot!")
    print("Type 'exit' to end the conversation.")

    bot = create_chatbot()

    while True:
        try:
            user_input = input("\nYou: ").strip()

            # Exit the conversation
            if user_input.lower() in ("exit", "quit"):
                print("Bot: Goodbye!")
                break

            # Prevent empty messages
            if not user_input:
                print("Bot: Please enter a message.")
                continue

            # Generate a response using ChatterBot
            response = bot.get_response(user_input)
            print(f"Bot: {response}")

        except (KeyboardInterrupt, EOFError):
            print("\nBot: Goodbye!")
            break


if __name__ == "__main__":
    main()
