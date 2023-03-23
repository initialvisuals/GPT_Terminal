# GPT_Terminal

![Image description](GPT_Terminal@4x.png)

**GPT_Terminal** is a command-line AI assistant built using OpenAI's GPT-4. It provides customizable preheaders for adding formatting and styling to your AI-generated responses. This project allows you to interact with the GPT-4 model in a terminal interface, making it easy to ask questions and receive answers quickly.

Demo Video: https://www.youtube.com/watch?v=FRTy8jV2FTo

GitHub repository: https://github.com/initialvisuals/GPT_Terminal

**Installation**

Clone the GitHub repository:

`git clone https://github.com/initialvisuals/GPT_Terminal.git`

Change to the GPT_Terminal directory:

`cd GPT_Terminal`

Install the required packages:

`pip install -r requirements.txt`

**Usage**

Before using GPT_Terminal, you need to set up an environment variable for the OpenAI API key. Replace your_api_key with your actual OpenAI API key.

For Linux:


`export OPENAI_API_KEY=your_api_key`

For Windows:

`set OPENAI_API_KEY=your_api_key`

To create an alias for GPT_Terminal on Linux/MacOS, add the following line to your shell profile (e.g., ~/.bashrc, ~/.bash_profile, or ~/.zshrc), replacing /path/to/GPT_Terminal with the actual path to the GPT_Terminal directory:


`alias ai="python /path/to/GPT_Terminal/ai.py"`

For Windows, create a doskey macro by adding the following line to a new or existing batch file (e.g., ai_macro.bat), replacing C:\path\to\GPT_Terminal with the actual path to the GPT_Terminal directory:


`doskey ai=python C:\path\to\GPT_Terminal\ai.py $*`

Run the batch file to load the doskey macro:

`ai_macro.bat`

After setting up the alias or doskey macro, you can simply type ai in the terminal or command prompt to start GPT_Terminal.

To interact with the AI, enter your prompt or question, and the AI will generate a response. You can also adjust settings like mode, preheader, rate, tokens, and more.

For help with settings, type help within GPT_Terminal.

**License**

This project is licensed under the MIT License.
