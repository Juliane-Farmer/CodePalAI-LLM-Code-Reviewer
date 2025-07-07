import requests
from pathlib import Path

# locate prompts folder
PROMPT_DIR = Path(__file__).parent.parent.parent / "prompts"
TEMPLATE = (PROMPT_DIR / "code_review.txt").read_text()

def review_code(code: str) -> str:
    # render the prompt
    prompt = TEMPLATE.format(code=code)

    url = "http://ollama:11434/generate"
    payload = {
        "model": "codellama:13b",
        "prompt": prompt,
        "stream": False,           # return a single JSON response
        # you can add "temperature", "max_tokens", etc. here too
    }

    resp = requests.post(url, json=payload)
    resp.raise_for_status()

    data = resp.json()
    # legacy generate returns { "model": ..., "response": "...", ... }
    return data.get("response", "")
