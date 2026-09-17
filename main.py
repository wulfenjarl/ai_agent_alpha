
import os
import argparse
from dotenv import load_dotenv
from openai import OpenAI

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
    {"role": "user", "content": args.user_prompt},
    ]   

    response = client.chat.completions.create(model=model,messages=messages)

    if not response.usage:
        raise RuntimeError('No response executed - check input calls.')

    prompt_tokens = response.usage.prompt_tokens
    response_tokens = response.usage.completion_tokens
    user_prompt = args.user_prompt

    if args.verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")
        print(response.choices[0].message.content)
    else:    
        print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
