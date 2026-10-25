# Simple Q&A Chatbot Using Python

## Project Description

This project is a simple question-and-answer chatbot developed using Python and the ChatterBot library. The chatbot allows users to enter messages through the terminal and receive responses based on previously trained conversations.

The project also includes a Django project structure as required for the assignment.

## Technologies Used

- Python 3.11
- Django 5.2
- ChatterBot 1.2
- spaCy
- SQLite
- Visual Studio Code

## How to Run the Project

1. Clone or download the GitHub repository.
2. Open the project folder in VS Code.
3. Create a Python virtual environment.
4. Activate the virtual environment.
5. Install the dependencies from `requirements.txt`.
6. Install the compatible spaCy English language model.
7. Run `python chatbot.py`.
8. Enter questions in the terminal and type `exit` to stop.

## Features

- Accepts user questions through the terminal.
- Generates responses using ChatterBot.
- Uses sample conversations for training.
- Stores trained conversations in a SQLite database.
- Handles empty input and supports an exit command.

## Limitations

The chatbot is trained on a small collection of conversations. It may return incorrect answers when users enter unfamiliar questions or use different wording.

A temporary spaCy tokenizer-loading workaround is included because the saved tokenizer produced an error in the development environment.

## Conclusion

This project helped me understand how a basic machine-learning chatbot works. I learned how to train a chatbot with sample conversations, process user input, and generate responses. I also learned that the quality of training data plays an important role in how accurately a chatbot answers questions.