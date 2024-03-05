# Cpanel-Chatbot-Intergration

This project is a chat application integration with a cPanel website. The application allows users to engage in conversations with a AI assistant, to ask questions or seek assistance on various topics.

## Features

- **Conversation Interface:** The chat interface allows for continued discussion and history between the user and the AI assistant.
- **Chat History:** Chat between the AI persists in the session, and will only go away upon the users using the option to reset the chat history, clearing previous conversations and starting anew.
- **Responsive Design:** The application is designed to be responsive, ensuring a consistent experience across different devices and screen sizes.

## Technologies Used

- **Python:** The backend of the application is built using Python.
- **Flask:** Flask is used as the web framework for handling HTTP requests and responses.
- **OpenAI API:** The application integrates with the OpenAI API to interact with AI.
- **HTML/CSS:** The frontend interface is created using HTML and CSS for styling and layout.

## Usage

1. **Start Chatting:** Upon visiting the application, users are greeted a screen regarding whether they want to continue, or reset the chat history.
2. **Ask Questions:** Users can type their questions or queries into the input field and submit them to AI.
3. **Receive Responses:** The AI will generate responses based on the user's input, providing assistance or information as needed.

## Setup Instructions

1. Clone the repository to your local machine.
2. Open up the cPanel admin panel and navigate to the Python webhooks page.
3. Create a Python webhook:
   - Application startup file as `app.py`.
   - Application Entry point as `app`.
4. Obtain an API key from OpenAI and set it as an environment variable.
5. Open up the directory created in cPanel File Manager and replace the existing `app.py` file with the one from the repository.
6. Edit the `app.py` file, and rename the `{model_name_goes_here}` to the model you want to use and the {secret_key_goes_here} to a random key.
7. Install the requirements (`openai`, `flask`).
8. (optional) you can edit the sys_prompt.txt to preload the chatbot with a system prompt. It's set to a decent one by default, so need to worry otherwise.
9. Run the web app, and access the application through your web browser at the specified URL.

## Contributing

Contributions to the project are welcome! If you have any suggestions, bug fixes, or feature enhancements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

Developed with ❤️ by Carnae
