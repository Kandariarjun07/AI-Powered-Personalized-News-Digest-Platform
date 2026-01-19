import os
from openai import OpenAI
from dotenv import load_dotenv

# Load env variables
load_dotenv()

def test_llm_connection():
    api_key = os.getenv("OPENROUTER_API_KEY")
    
    print("--- LLM Connection Test ---")
    if not api_key:
        print("ERROR: OPENROUTER_API_KEY is missing from .env")
        return

    # Print masked key for verification
    masked_key = f"{api_key[:8]}...{api_key[-4:]}" if len(api_key) > 12 else "INVALID KEY LENGTH"
    print(f"Using API Key: {masked_key}")
    
    # Check if it looks like an OpenAI key
    if api_key.startswith("sk-proj-"):
        print("\n⚠️  WARNING: This looks like an OpenAI Project Key (starts with 'sk-proj-').")
        print("   If you are trying to use OpenRouter, this key will NOT work.")
        print("   You must get a key from https://openrouter.ai/keys")
        print("   OR change the code to use the official OpenAI API.\n")
    elif api_key.startswith("sk-or-v1-"):
        print("✅ Key format looks correct for OpenRouter.")

    print("Attempting to connect to OpenRouter...")
    
    try:
        client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=api_key,
        )

        response = client.chat.completions.create(
            model="qwen/qwen-2.5-coder-32b-instruct",
            messages=[
                {"role": "user", "content": "Say 'Hello!' if you can hear me."}
            ],
        )
        
        print("\n✅ SUCCESS! Response received:")
        print(response.choices[0].message.content)

    except Exception as e:
        print("\n❌ FAILED. Error details:")
        print(e)
        
        # Additional debug info
        print("\nTip: If you see '401 Unauthorized', your API Key is invalid for this endpoint.")

if __name__ == "__main__":
    test_llm_connection()
