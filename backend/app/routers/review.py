from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.model import review_code

router = APIRouter()

class CodeRequest(BaseModel):
    code: str

@router.post("/review")
def review(request: CodeRequest):
    try:
        response = review_code(request.code)
        return {"result": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
