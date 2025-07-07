import os
import requests
from pathlib import Path

PROMPT_DIR = Path(__file__).parent.parent.parent / "prompts"
TEMPLATE = (PROMPT_DIR / "code_review.txt").read_text()

def review_code(code: str) -> str:
    prompt = TEMPLATE.format(code=code)
    model_name = os.getenv("OLLAMA_MODEL", "tinyllama")  

    try:
        resp = requests.post(
        "http://ollama:11434/api/generate",
        json={
            "model": model_name,
            "prompt": prompt,
            "stream": False  
        },
    )

        resp.raise_for_status()
        return resp.json().get("response", "")
    except requests.RequestException as e:
        raise RuntimeError(f"Ollama API error: {e}")
