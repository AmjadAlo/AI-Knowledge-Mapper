import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_classification_options(topic, context=""):
    """
    Suggest classification strategies based on a given topic.
    Automatically uses GPT-4-turbo with fallback to GPT-3.5-turbo if unavailable.
    """
    prompt = f"""
Given the topic: "{topic}", suggest the most relevant ways it can be classified or structured.

Respond with a short list (3–6 items only). Do not explain, just list classification approaches.

Context (optional):
{context}
"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4-0125-preview",
            messages=[
                {"role": "system", "content": "You are a curriculum architect."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.0,
            max_tokens=200
        )
    except Exception as e:
        print(" Falling back to gpt-3.5-turbo:", e)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a curriculum architect."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.0,
            max_tokens=200
        )

    raw = response.choices[0].message.content
    return [item.strip("-• ").strip() for item in raw.splitlines() if item.strip()]
