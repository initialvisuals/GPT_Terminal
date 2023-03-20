
import openai  # type: ignore
import os
import sys
import json
import textwrap
import platform
from typing import List, Tuple
import datetime
import contextlib
import subprocess
from prompt_toolkit import PromptSession # type: ignore
from prompt_toolkit.history import FileHistory # type: ignore
from prompt_toolkit.completion import WordCompleter # type: ignore
from prompt_toolkit.formatted_text import FormattedText # type: ignore
from prompt_toolkit.styles import Style # type: ignore


OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    print("Error: OPENAI_API_KEY environment variable not set.")
    sys.exit(1)

openai.api_key = OPENAI_API_KEY

#write to the SETTINGS_FILE in the same directory as the script
SETTINGS_FILE = os.path.join(os.path.dirname(os.path.realpath(__file__)), "settings.json")

DEFAULT_SETTINGS = {
    "preheader": "You are a research ai assistant who focuses on clear and concise, accurate and factual responses. When you do not know the answer or you do not wish to respond, say that you cannot reply at this moment and to try again.",
    "rate": 1,
    "tokens": 300
}

subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)

def load_settings():
    with contextlib.suppress(FileNotFoundError):
        with open(SETTINGS_FILE, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                print("Error: Invalid JSON in settings file. Using default settings.")
    return DEFAULT_SETTINGS.copy()

settings = load_settings()

def save_settings():
    with open(SETTINGS_FILE, "w") as file:
        json.dump(settings, file)

def show_help():
    help_text = """
    preheader: change the preheader of the ai assistant
    rate: change the rate of the ai assistant (integer between 1-5)
    tokens: change the max tokens for the ai assistant (integer between 1-8192)
    reset: reset the settings to default values
    clear: clear the screen
    help: show this message
    """
    print(help_text)

def update_settings(setting_name: str):
    if setting_name == "clear":
        # Clear the screen on Mac, Windows, and Linux
        if sys.platform == "win32":
            os.system("cls")
        else:
            os.system("clear")
    elif setting_name == "help":
        show_help()
    elif setting_name == "preheader":
        preheader = input("Enter new preheader: ")
        settings["preheader"] = preheader
        print(f"Preheader updated to: {settings['preheader']}")
    elif setting_name == "rate":
        try:
            rate = int(input("Enter rate (integer between 1-5): "))
            if 1 <= rate <= 5:
                settings["rate"] = rate
                print(f"Rate updated to {settings['rate']}")
            else:
                print("Invalid rate. Choose an integer between 1 and 5.")
        except ValueError:
            print("Invalid rate. Choose an integer between 1 and 5.")
    elif setting_name == "reset":
        settings.update(DEFAULT_SETTINGS.copy())
        print("Settings reset to default values.")
    elif setting_name == "tokens":
        try:
            tokens = int(input("Enter max tokens (integer between 1-8192): "))
            if 1 <= tokens <= 8192:
                settings["tokens"] = tokens
                print(f"Max tokens updated to {settings['tokens']}")
            else:
                print("Invalid token count. Choose an integer between 1 and 8192.")
        except ValueError:
            print("Invalid token count. Choose an integer between 1 and 8192.")
    else:
        print("Invalid setting name.")

    save_settings()


def parse_arguments(arguments: List[str]) -> str:
    valid_args = ["preheader", "rate", "reset", "clear", "help"]
    return arguments[0] if arguments and arguments[0] in valid_args else ""


def generate_response(prompt, temperature=0.7, max_tokens=8192, rate=1, preheader=settings["preheader"]):
    def fetch_responses():
        return openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": preheader},
                {"role": "user", "content": prompt}
            ],
            temperature=temperature,
            max_tokens=max_tokens,
            n=rate, 
        )

    response = fetch_responses()

    for _ in range(rate):
        if _ > 0:
            response = fetch_responses()
        message = response.choices[0]['message']['content']
        print(f"{_ + 1} ---\n{message}\n" if rate > 1 else message)


def build_completer():
    words = [
        "preheader",
        "rate",
        "reset",
        "clear",
        "help",
        "exit",
        "quit",
        "tokens"
    ]
    return WordCompleter(words, ignore_case=True)


def build_bottom_toolbar():
    def bottom_toolbar():
        working_width = os.get_terminal_size().columns
        current_time = datetime.datetime.now().strftime("%I:%M %p - %B %d, %Y")
        os_name = platform.system()
        python_version = platform.python_version()
        preheader_wrapped = textwrap.fill(settings["preheader"], width=working_width)

        return (
            f"Rate: {settings['rate']} | Tokens: {settings['tokens']} \n"
            f"Preheader: {preheader_wrapped}\n"
            f"OS: {os_name} | Python: {python_version}\n"
            f"Keyboard shortcuts: (Ctrl+C) Exit\n"
            f"{current_time}"
        )

    return bottom_toolbar


def toolbar_input_handler(prompt_message, session, completer, bottom_toolbar):
    return session.prompt(
        prompt_message,
        completer=completer,
        complete_while_typing=True,
        bottom_toolbar=bottom_toolbar,
        style=Style.from_dict(
            {
                "toolbar": "bg:#aaaaaa #000000",
                "bottom-toolbar": "bg:#222222 #ffffff", 
            }
        ),
    )

def main():
    session = PromptSession(history=FileHistory(".assistant_history"))
    completer = build_completer()


    try:
        while True:
            bottom_toolbar = build_bottom_toolbar()
            print("Enter a prompt or a setting (preheader, rate, reset, help, tokens, exit) ")
            user_input = toolbar_input_handler(": ", session, completer, bottom_toolbar)

            if user_input.lower() == 'exit':
                break

            if setting_name := parse_arguments([user_input]):
                update_settings(setting_name)
            elif user_input.lower() in settings:
                setting_name = user_input.lower()
                if setting_name == "tokens":
                    try:
                        tokens = int(input("Enter max tokens (integer between 1-8192): "))
                        if 1 <= tokens <= 8192:
                            settings["tokens"] = tokens
                            print(f"Max tokens updated to {settings['tokens']}")
                        else:
                            print("Invalid token count. Choose an integer between 1 and 8192.")
                    except ValueError:
                        print("Invalid token count. Choose an integer between 1 and 8192.")

            # Generate response from the prompt
            else:
                prompt_input = user_input
                generate_response(prompt_input, rate=settings["rate"], preheader=settings["preheader"], max_tokens=settings["tokens"])

    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit()
        
if __name__ == "__main__":
    main()

