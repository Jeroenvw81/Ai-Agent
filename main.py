import os
import sys
from dotenv import load_dotenv      #imports the dotenv function
from google import genai
from google.genai import types      #the way genai handles data

from prompts import system_prompt
from call_function import available_functions, call_function


def main():
    load_dotenv()       # This reads the .env file and loads variables into the environment

    verbose = "--verbose" in sys.argv
    
    user_prompt = " ".join([arg for arg in sys.argv[1:] if arg != "--"])
    if not user_prompt:
        print("Error, AI-Agent needs a querry!!")
        print('\nUsage: python main.py "your querry here"')
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    messages = [
         types.Content(role = "user", parts = [types.Part(text = user_prompt)]),        #creates a list containing chat history, atm solely user
    ]
    generate_content(client, messages, user_prompt, verbose)

def generate_content(client, messages, user_prompt, verbose):
    if verbose:
        print(f"User prompt: {user_prompt}\n")
    response = client.models.generate_content(
        model = "gemini-2.0-flash-001",
        contents = messages,
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt),
    )
    if verbose:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)

    if not response.function_calls:
        return response.text
    
    function_responses = []
    for function_call_part in response.function_calls:
        function_call_result = call_function(function_call_part, verbose)
        if (
            not function_call_result.parts or not function_call_result.parts[0].function_response
        ):
            raise Exception("empty function call result")
        if verbose:
            print(f" -> {function_call_result.parts[0].function_response.response}")
        function_responses.append(function_call_result.parts[0])
    
    if not function_responses:
        raise Exception("no function responses generated, exiting.")

if __name__ == "__main__":
    main()