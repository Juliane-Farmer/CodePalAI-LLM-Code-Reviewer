

# import os
# from openai import OpenAI
# from fastapi import HTTPException

# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# def review_code(code: str):
#     try:
#         response = client.chat.completions.create(
#             model=os.getenv("MODEL_NAME", "gpt-3.5-turbo"),
#             messages=[
#                 {"role": "system", "content": "You're an expert Python code reviewer. Review the code, explain bugs or bad practices, and suggest improvements."},
#                 {"role": "user", "content": f"Review this Python code:\n\n{code}"}
#             ]
#         )
#         return response.choices[0].message.content

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"OpenAI API error: {str(e)}")


import os
from pathlib import Path
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Load prompt from file
PROMPT_DIR = Path(__file__).parent.parent.parent / "prompts"
TEMPLATE = (PROMPT_DIR / "code_review.txt").read_text()

def review_code(code: str) -> str:
    prompt = TEMPLATE.format(code=code)

    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert Python code reviewer."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"500: OpenAI API error: {str(e)}"