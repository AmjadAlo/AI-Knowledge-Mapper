import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def run_synthesizer(raw_data: dict, topic: str):
    def stringify(value):
        if isinstance(value, list):
            return "\n".join([str(v) for v in value])
        return str(value)

    combined_text = "\n".join([stringify(v) for v in raw_data.values()])

    prompt = f"""
You are a concept map architect specializing in clean, structured roadmaps.

Topic: "{topic}"

Your task:
######### WRITE YOUR PROMPT  ############

Context:
{combined_text}
"""







    try:
        response = openai.ChatCompletion.create(
            model="gpt-4-0125-preview",
            messages=[
                {"role": "system", "content": "You are a helpful roadmap planning assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.0,
            max_tokens=1000
        )
    except Exception as e:
        print(" GPT-4 failed, falling back to GPT-3.5-turbo:", e)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful roadmap planning assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.0,
            max_tokens=1000
        )

    return response.choices[0].message.content.strip()
