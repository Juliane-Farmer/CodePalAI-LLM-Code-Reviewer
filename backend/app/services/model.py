import os
from pathlib import Path
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

PROMPT_DIR = Path(__file__).parent.parent.parent / "prompts"
TEMPLATE = (PROMPT_DIR / "code_review.txt").read_text()

def review_code(code: str, language: str) -> str:
    prompt = TEMPLATE.format(language=language, code=code)

    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"You are an expert {language} code reviewer."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"500: OpenAI API error: {str(e)}"