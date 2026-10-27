
import os
import argparse
import json
from dotenv import load_dotenv
from openai import OpenAI
from prompts import system_prompt
from call_functions import available_functions
from call_functions import call_functions

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")


def main():
    if not api_key:
        raise RuntimeError('No API key found!')

    parser = argparse.ArgumentParser(description="LLM Query")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    # Now we can access `args.user_prompt`

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )
    model = "openrouter/free"
    messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": args.user_prompt},
    ] 

    response = client.chat.completions.create(
    model="openrouter/free",
    messages=messages,
    temperature=0,
    tools=available_functions,
    )

    if not response.usage:
        raise RuntimeError('No response executed - check input calls.')

    prompt_tokens = response.usage.prompt_tokens
    response_tokens = response.usage.completion_tokens
    user_prompt = args.user_prompt

    message = response.choices[0].message
    if message.tool_calls:
        for tool_call in message.tool_calls:
            result_message = call_functions(tool_call, args.verbose)
            if not result_message["content"]:
                raise Exception("No results! Function ran, but returned no results.")
            if args.verbose:
                    print(f"-> {result_message['content']}")             
    else:    
        print(response.choices[0].message.content)

    if args.verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")
    
if __name__ == "__main__":
    main()
