import requests
from pathlib import Path

# Locate the prompts folder (relative to this file)
PROMPT_DIR = Path(__file__).parent.parent.parent / "prompts"
TEMPLATE = (PROMPT_DIR / "code_review.txt").read_text()

def review_code(code: str) -> str:
    """
    Reads the code_review.txt template, injects the user's code,
    sends it to the Ollama CodeLlama model, and returns the AI's response.
    """
    # Fill in the {code} placeholder
    prompt = TEMPLATE.format(code=code)

    try:
        resp = requests.post(
            "http://ollama:11434/api/generate",
            json={
                "model": "codellama:13b",
                "prompt": prompt,
            },
        )
        resp.raise_for_status()
        return resp.json().get("response", "")
    except requests.RequestException as e:
        raise RuntimeError(f"Ollama API error: {e}")
